from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timezone
from typing import Any

from pyproj import CRS, Transformer
from shapely import wkb
from shapely.geometry import GeometryCollection, MultiPolygon, Polygon
from shapely.ops import transform as shapely_transform
from shapely.ops import unary_union
from sqlalchemy import Engine, text

import config
from figure08 import validate_table_name


DISPLAY_CRS = CRS.from_user_input(config.FIGURE_07_DISPLAY_CRS)
PROJECT_TO_54009 = Transformer.from_crs("EPSG:4326", "ESRI:54009", always_xy=True)
PROJECT_TO_DISPLAY = Transformer.from_crs("ESRI:54009", DISPLAY_CRS, always_xy=True)
LONLAT_TO_DISPLAY = Transformer.from_crs("EPSG:4326", DISPLAY_CRS, always_xy=True)


def _year_params() -> dict[str, Any]:
    params: dict[str, Any] = {
        "analysis_id": config.ANALYSIS_ID,
        "urban_threshold": config.FIGURE_07_URBAN_THRESHOLD,
        "min_lon": float(config.FIGURE_07_BBOX_LON_LAT[0]),
        "min_lat": float(config.FIGURE_07_BBOX_LON_LAT[1]),
        "max_lon": float(config.FIGURE_07_BBOX_LON_LAT[2]),
        "max_lat": float(config.FIGURE_07_BBOX_LON_LAT[3]),
    }
    for index, year in enumerate(config.FIGURE_07_YEARS):
        params[f"year_{index}"] = int(year)
    return params


def _year_placeholders() -> str:
    return ", ".join(f":year_{index}" for index, _ in enumerate(config.FIGURE_07_YEARS))


def fetch_prd_bbox_projected() -> Polygon:
    min_lon, min_lat, max_lon, max_lat = config.FIGURE_07_BBOX_LON_LAT
    minx, miny = PROJECT_TO_54009.transform(min_lon, min_lat)
    maxx, maxy = PROJECT_TO_54009.transform(max_lon, max_lat)
    return Polygon(
        [
            (minx, miny),
            (minx, maxy),
            (maxx, maxy),
            (maxx, miny),
            (minx, miny),
        ]
    )


def fetch_prd_bbox_display() -> Polygon:
    min_lon, min_lat, max_lon, max_lat = config.FIGURE_07_BBOX_LON_LAT
    corners = [
        LONLAT_TO_DISPLAY.transform(min_lon, min_lat),
        LONLAT_TO_DISPLAY.transform(min_lon, max_lat),
        LONLAT_TO_DISPLAY.transform(max_lon, max_lat),
        LONLAT_TO_DISPLAY.transform(max_lon, min_lat),
    ]
    return Polygon([*corners, corners[0]])


def fetch_yearly_prd_clusters(engine: Engine) -> list[dict[str, Any]]:
    geom_table = validate_table_name(config.WORLD_CLUSTER_GROWTH_GEOM_TABLE)
    pop_table = validate_table_name(config.WORLD_CLUSTER_GROWTH_POPULATION_COUNTRY_ANALYSIS_TABLE)
    query = text(
        f"""
        WITH bbox AS (
            SELECT ST_Transform(
                ST_MakeEnvelope(:min_lon, :min_lat, :max_lon, :max_lat, 4326),
                54009
            ) AS geom
        ),
        population AS (
            SELECT
                cluster_id,
                y1,
                y2,
                MAX(population_y1) AS population_y1
            FROM {pop_table}
            WHERE analysis_id = :analysis_id
              AND y1 = y2
              AND y1 IN ({_year_placeholders()})
            GROUP BY cluster_id, y1, y2
        )
        SELECT
            g.cluster_id,
            g.y1 AS year,
            p.population_y1,
            ST_Area(ST_Intersection(g.geom, b.geom)) / 1000000.0 AS clipped_area_km2,
            ST_AsBinary(ST_Intersection(g.geom, b.geom)) AS geom_wkb
        FROM {geom_table} g
        JOIN population p USING (cluster_id, y1, y2)
        JOIN bbox b ON ST_Intersects(g.geom, b.geom)
        WHERE g.y1 = g.y2
          AND g.y1 IN ({_year_placeholders()})
          AND g.urban_threshold = :urban_threshold
        ORDER BY g.y1, p.population_y1 DESC, g.cluster_id
        """
    )
    with engine.connect() as connection:
        rows = connection.execute(query, _year_params()).mappings().all()

    clusters_by_year: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        geom = normalize_polygonal_geometry(wkb.loads(bytes(row["geom_wkb"])))
        year = int(row["year"])
        clusters_by_year[year].append(
            {
                "clusterId": row["cluster_id"],
                "population": float(row["population_y1"]),
                "clippedAreaKm2": float(row["clipped_area_km2"]),
                "geometry": geom,
            }
        )

    yearly_clusters = []
    for year in config.FIGURE_07_YEARS:
        clusters = clusters_by_year.get(year, [])
        if not clusters:
            raise ValueError(f"Figure 07 returned no clusters for year {year}.")
        yearly_clusters.append({"year": int(year), "clusters": clusters})
    return yearly_clusters


def normalize_polygonal_geometry(
    geom: Polygon | MultiPolygon | GeometryCollection,
) -> Polygon | MultiPolygon:
    if geom.is_empty:
        raise ValueError("Encountered an empty geometry while building figure 07.")

    if isinstance(geom, (Polygon, MultiPolygon)):
        return geom

    if isinstance(geom, GeometryCollection):
        polygon_parts = []
        for part in geom.geoms:
            if part.is_empty:
                continue
            if isinstance(part, Polygon):
                polygon_parts.append(part)
            elif isinstance(part, MultiPolygon):
                polygon_parts.extend(list(part.geoms))
        if not polygon_parts:
            raise ValueError("Geometry collection for figure 07 does not contain polygonal parts.")
        merged = unary_union(polygon_parts)
        if not isinstance(merged, (Polygon, MultiPolygon)):
            raise TypeError("Failed to normalize figure-07 geometry collection.")
        return merged

    raise TypeError(f"Unsupported geometry type for figure 07: {type(geom)!r}")


def pad_bounds(
    bounds: tuple[float, float, float, float],
    padding_ratio: float,
) -> tuple[float, float, float, float]:
    minx, miny, maxx, maxy = bounds
    span_x = maxx - minx
    span_y = maxy - miny
    pad_x = span_x * padding_ratio
    pad_y = span_y * padding_ratio
    return (
        minx - pad_x,
        miny - pad_y,
        maxx + pad_x,
        maxy + pad_y,
    )


def square_bounds(
    bounds: tuple[float, float, float, float],
) -> tuple[float, float, float, float]:
    minx, miny, maxx, maxy = bounds
    center_x = (minx + maxx) / 2
    center_y = (miny + maxy) / 2
    half_span = max(maxx - minx, maxy - miny) / 2
    return (
        center_x - half_span,
        center_y - half_span,
        center_x + half_span,
        center_y + half_span,
    )


def compute_square_viewport(
    bounds: tuple[float, float, float, float],
) -> dict[str, float | int | tuple[float, float, float, float]]:
    minx, miny, maxx, maxy = bounds
    size = int(config.FIGURE_07_VIEWPORT_SIZE)
    scale = size / (maxx - minx)
    return {
        "width": size,
        "height": size,
        "scale": scale,
        "bounds": bounds,
    }


def geometry_to_viewbox_space(
    geom: Polygon | MultiPolygon,
    viewport: dict[str, float | int | tuple[float, float, float, float]],
) -> Polygon | MultiPolygon:
    minx, miny, _, _ = viewport["bounds"]
    scale = float(viewport["scale"])
    height = float(viewport["height"])
    return shapely_transform(
        lambda x, y, z=None: ((x - minx) * scale, height - (y - miny) * scale),
        geom,
    )


def point_to_viewbox_space(
    x: float,
    y: float,
    viewport: dict[str, float | int | tuple[float, float, float, float]],
) -> tuple[float, float]:
    minx, miny, _, _ = viewport["bounds"]
    scale = float(viewport["scale"])
    height = float(viewport["height"])
    return ((x - minx) * scale, height - (y - miny) * scale)


def ring_to_svg_path(coords: list[tuple[float, float]]) -> str:
    commands = []
    for index, (x, y) in enumerate(coords):
        commands.append(f"{'M' if index == 0 else 'L'} {x:.1f} {y:.1f}")
    commands.append("Z")
    return " ".join(commands)


def geometry_to_svg_path(geom: Polygon | MultiPolygon) -> str:
    if isinstance(geom, Polygon):
        parts = [ring_to_svg_path(list(geom.exterior.coords))]
        for interior in geom.interiors:
            parts.append(ring_to_svg_path(list(interior.coords)))
        return " ".join(parts)

    if isinstance(geom, MultiPolygon):
        return " ".join(geometry_to_svg_path(part) for part in geom.geoms)

    raise TypeError(f"Unsupported geometry type for SVG conversion: {type(geom)!r}")


def build_scenes() -> list[dict[str, Any]]:
    visible_layer_ids = ["place-labels"]
    scenes = []
    for year in config.FIGURE_07_YEARS:
        visible_layer_ids = [*visible_layer_ids, f"prd-{year}"]
        scenes.append(
            {
                "id": f"prd-{year}",
                "kicker": "Pearl River Delta growth",
                "title": str(year),
                "body": f"Reveal the Pearl River Delta cluster field in {year}.",
                "visibleLayerIds": visible_layer_ids[:],
            }
        )
    return scenes


def build_label_layer(
    viewport: dict[str, float | int | tuple[float, float, float, float]],
) -> dict[str, Any]:
    items = []
    for label in config.FIGURE_07_LABELS:
        display_x, display_y = LONLAT_TO_DISPLAY.transform(label["lon"], label["lat"])
        x_view, y_view = point_to_viewbox_space(display_x, display_y, viewport)
        items.append(
            {
                "id": label["id"],
                "x": round(x_view, 1),
                "y": round(y_view, 1),
                "text": label["text"],
                "fill": "#cdd7e1",
                "opacity": 0.9,
                "fontSize": 44,
                "fontWeight": 800,
                "anchor": "middle",
                "letterSpacing": "0.02em",
            }
        )
    return {"id": "place-labels", "kind": "labels", "items": items, "opacity": 1}


def build_year_layers(
    yearly_clusters: list[dict[str, Any]],
    viewport: dict[str, float | int | tuple[float, float, float, float]],
) -> list[dict[str, Any]]:
    layers = []
    for year_data in yearly_clusters:
        year = int(year_data["year"])
        style = config.FIGURE_07_YEAR_STYLES[year]
        sorted_clusters = sorted(
            year_data["clusters"],
            key=lambda cluster: cluster["clippedAreaKm2"],
            reverse=True,
        )
        items = []
        for cluster in sorted_clusters:
            simplified = cluster["geometry"].simplify(
                config.FIGURE_07_SIMPLIFY_TOLERANCE_METERS,
                preserve_topology=True,
            )
            display_geom = shapely_transform(PROJECT_TO_DISPLAY.transform, simplified)
            items.append(
                {
                    "id": cluster["clusterId"],
                    "d": geometry_to_svg_path(geometry_to_viewbox_space(display_geom, viewport)),
                    "fill": style["fill"],
                    "fillOpacity": style["fillOpacity"],
                    "stroke": style["stroke"],
                    "strokeOpacity": style["strokeOpacity"],
                    "strokeWidth": config.FIGURE_07_STROKE_WIDTH,
                }
            )
        layers.append(
            {
                "id": f"prd-{year}",
                "kind": "paths",
                "items": items,
            }
        )
    return layers


def build_payload(yearly_clusters: list[dict[str, Any]]) -> dict[str, Any]:
    if len(yearly_clusters) != len(config.FIGURE_07_YEARS):
        raise ValueError("Figure 07 did not return the expected number of yearly cluster slices.")

    bbox_projected = fetch_prd_bbox_projected()
    display_bbox = fetch_prd_bbox_display()
    padded_display_bounds = square_bounds(
        pad_bounds(display_bbox.bounds, config.FIGURE_07_PADDING_RATIO)
    )
    viewport = compute_square_viewport(padded_display_bounds)

    year_stats = []
    for year_data in yearly_clusters:
        union_area_km2 = float(
            unary_union([cluster["geometry"] for cluster in year_data["clusters"]]).area / 1_000_000.0
        )
        year_stats.append(
            {
                "year": int(year_data["year"]),
                "clusterCount": int(len(year_data["clusters"])),
                "totalPopulation": float(
                    sum(cluster["population"] for cluster in year_data["clusters"])
                ),
                "maxClusterPopulation": float(
                    max(cluster["population"] for cluster in year_data["clusters"])
                ),
                "clippedAreaKm2": float(
                    sum(cluster["clippedAreaKm2"] for cluster in year_data["clusters"])
                ),
                "unionAreaKm2": union_area_km2,
            }
        )

    return {
        "id": "figure-07",
        "kind": config.FIGURE_07_KIND,
        "meta": {
            "analysisId": config.ANALYSIS_ID,
            "generatedAt": datetime.now(timezone.utc).isoformat(),
            "sourceTables": {
                "geometry": config.WORLD_CLUSTER_GROWTH_GEOM_TABLE,
                "population": config.WORLD_CLUSTER_GROWTH_POPULATION_COUNTRY_ANALYSIS_TABLE,
            },
            "urbanThreshold": config.FIGURE_07_URBAN_THRESHOLD,
            "bboxLonLat": [float(value) for value in config.FIGURE_07_BBOX_LON_LAT],
            "paddingRatio": config.FIGURE_07_PADDING_RATIO,
            "displayCrs": config.FIGURE_07_DISPLAY_CRS,
            "simplifyToleranceMeters": config.FIGURE_07_SIMPLIFY_TOLERANCE_METERS,
            "viewport": {
                "width": int(viewport["width"]),
                "height": int(viewport["height"]),
                "boundsDisplay": [float(value) for value in padded_display_bounds],
                "clipBounds54009": [float(value) for value in bbox_projected.bounds],
            },
            "years": [int(year) for year in config.FIGURE_07_YEARS],
            "yearStats": year_stats,
            "labels": config.FIGURE_07_LABELS,
        },
        "scenes": build_scenes(),
        "map": {
            "viewport": {
                "viewBox": [0, 0, int(viewport["width"]), int(viewport["height"])],
                "background": config.FIGURE_07_VIEWPORT_BACKGROUND,
            },
            "layers": [
                *build_year_layers(yearly_clusters, viewport),
                build_label_layer(viewport),
            ],
        },
    }


def validate_payload(payload: dict[str, Any]) -> None:
    if payload["id"] != "figure-07":
        raise ValueError("Figure-07 payload id is invalid.")

    if payload["kind"] != config.FIGURE_07_KIND:
        raise ValueError("Figure-07 payload kind is invalid.")

    scenes = payload["scenes"]
    if len(scenes) != len(config.FIGURE_07_YEARS):
        raise ValueError("Figure-07 payload scene count is invalid.")

    layers = payload["map"]["layers"]
    year_layers = [layer for layer in layers if layer["id"].startswith("prd-")]
    if len(year_layers) != len(config.FIGURE_07_YEARS):
        raise ValueError("Figure-07 payload year-layer count is invalid.")

    returned_years = [item["year"] for item in payload["meta"]["yearStats"]]
    if returned_years != list(config.FIGURE_07_YEARS):
        raise ValueError("Figure-07 year stats are out of order.")

    for scene in scenes:
        if "place-labels" not in scene["visibleLayerIds"]:
            raise ValueError("Figure-07 scenes must keep place labels visible.")
