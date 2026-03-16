from __future__ import annotations

from pathlib import Path
from typing import Any

import geopandas as gpd
import numpy as np
import pandas as pd
import rasterio
from rasterio.mask import mask
from shapely import wkb
from shapely.geometry import MultiPolygon, Polygon, box
from shapely.ops import transform as shapely_transform
from sqlalchemy import Engine, text

import config


def validate_source_paths() -> None:
    required_paths = [
        config.FIGURE_03_SATELLITE_TIFF_PATH,
        config.FIGURE_03_AAV_XLSX_PATH,
        config.FIGURE_03_COMMUNES_GEOJSON_PATH,
        config.FIGURE_03_NOTEBOOK_PATH,
    ]
    missing = [str(path) for path in required_paths if not path.exists()]
    if missing:
        raise FileNotFoundError(f"Missing figure-03 source files: {missing}")


def load_admin_and_aav_shapes() -> tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]:
    aav_to_commune_2020 = pd.read_excel(
        config.FIGURE_03_AAV_XLSX_PATH,
        sheet_name="Composition_communale",
        header=5,
    )
    paris_aav_with_communes = aav_to_commune_2020[
        aav_to_commune_2020["LIBAAV2020"] == "Paris"
    ].copy()

    shape_communes = gpd.read_file(
        config.FIGURE_03_COMMUNES_GEOJSON_PATH,
        engine="pyogrio",
        columns=["INSEE_COM", "TYPE", "INSEE_DEP", "geometry"],
    )

    paris_aav_shape = shape_communes[
        shape_communes["INSEE_COM"].isin(paris_aav_with_communes["CODGEO"].unique())
    ][["geometry"]]
    paris_admin_area_shape = shape_communes[
        (shape_communes["TYPE"] == "ARM") & (shape_communes["INSEE_DEP"] == "75")
    ][["geometry"]]

    paris_aav_union = gpd.GeoDataFrame(
        geometry=pd.concat(
            [paris_aav_shape["geometry"], paris_admin_area_shape["geometry"]],
            ignore_index=True,
        ),
        crs=shape_communes.crs,
    ).dissolve()
    paris_admin_union = paris_admin_area_shape.dissolve()
    return paris_admin_union, paris_aav_union


def load_ghsl_shape(engine: Engine) -> tuple[gpd.GeoDataFrame, dict[str, Any]]:
    query = text(
        """
        WITH ranked_cities AS (
            SELECT g.cluster_id, g.urban_threshold, g.y1, g.y2, g.geom, p.population_y1,
                   ROW_NUMBER() OVER (
                       PARTITION BY g.y1, g.y2, gc.gwcode
                       ORDER BY p.population_y1 DESC, g.urban_threshold ASC, g.cluster_id ASC
                   ) AS rank
            FROM world_cluster_growth_geom g
            JOIN world_cluster_growth_geocoding gc USING (cluster_id, y1, y2, urban_threshold)
            JOIN world_cluster_growth_population_country_analysis p USING (cluster_id, y1, y2)
            WHERE g.y1 = :year AND g.y2 = :year AND gc.gwcode = :gwcode
        )
        SELECT
            cluster_id,
            urban_threshold,
            population_y1,
            ST_AsBinary(geom) AS geom_wkb
        FROM ranked_cities
        WHERE rank = 1
        """
    )
    with engine.connect() as conn:
        row = conn.execute(
            query,
            {"year": config.FIGURE_03_GHSL_YEAR, "gwcode": config.FIGURE_03_GHSL_GWCODE},
        ).mappings().one()

    ghsl_shape = gpd.GeoDataFrame(
        {"geometry": [wkb.loads(bytes(row["geom_wkb"]))]},
        crs="ESRI:54009",
    )
    return ghsl_shape, {
        "clusterId": row["cluster_id"],
        "urbanThreshold": int(row["urban_threshold"]),
        "population2015": float(row["population_y1"]),
    }


def build_crop_box(attraction_geom: Polygon | MultiPolygon) -> Polygon:
    minx, miny, maxx, maxy = attraction_geom.bounds
    pad_x = (maxx - minx) * config.FIGURE_03_SATELLITE_PADDING_RATIO
    pad_y = (maxy - miny) * config.FIGURE_03_SATELLITE_PADDING_RATIO
    return box(minx - pad_x, miny - pad_y, maxx + pad_x, maxy + pad_y)


def geometry_to_pixel_space(geom: Polygon | MultiPolygon, transform: rasterio.Affine) -> Polygon | MultiPolygon:
    inverse_transform = ~transform
    return shapely_transform(lambda x, y, z=None: inverse_transform * (x, y), geom)


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
    raise TypeError(f"Unsupported geometry type: {type(geom)!r}")


def build_scenes() -> list[dict[str, Any]]:
    return [
        {
            "id": "basemap-only",
            "kicker": "Boundary problem",
            "title": "Basemap only",
            "body": "Start with the Paris region as a fixed spatial frame. Do not move the camera.",
            "tone": "neutral",
            "visibleLayerIds": [],
        },
        {
            "id": "proper",
            "kicker": "Administrative boundary",
            "title": "Draw the legal core",
            "body": "Paris proper: the compact legal city around the historic core.",
            "tone": "proper",
            "visibleLayerIds": ["proper-boundary"],
        },
        {
            "id": "built",
            "kicker": "Morphological footprint",
            "title": "Reveal the built city",
            "body": "Built-up Paris: the dense contiguous urban fabric most people would recognize as the city.",
            "tone": "built",
            "visibleLayerIds": ["proper-boundary", "built-fill"],
        },
        {
            "id": "functional",
            "kicker": "Attraction area",
            "title": "Reveal the attraction area",
            "body": "Wider commuting region: the same city suddenly covers far more territory.",
            "tone": "functional",
            "visibleLayerIds": [
                "proper-boundary",
                "built-fill",
                "attraction-fill",
                "attraction-boundary",
            ],
        },
        {
            "id": "comparison",
            "kicker": "Measurement problem",
            "title": "The border changes the city",
            "body": "Same city, radically different extents depending on the border. Nothing moved on the map. Only the border changed.",
            "tone": "neutral",
            "visibleLayerIds": [
                "proper-boundary",
                "built-fill",
                "attraction-fill",
                "attraction-boundary",
            ],
        },
    ]


def build_payload(
    image_width: int,
    image_height: int,
    proper_path: str,
    built_path: str,
    attraction_path: str,
    crop_bounds: tuple[float, float, float, float],
    ghsl_info: dict[str, Any],
    proper_area_km2: float,
    built_area_km2: float,
    attraction_area_km2: float,
) -> dict[str, Any]:
    return {
        "id": "figure-03",
        "kind": config.FIGURE_03_KIND,
        "meta": {
            "generatedFrom": {
                "notebook": str(config.FIGURE_03_NOTEBOOK_PATH),
                "satelliteTiff": str(config.FIGURE_03_SATELLITE_TIFF_PATH),
                "aavWorkbook": str(config.FIGURE_03_AAV_XLSX_PATH),
                "communesGeojson": str(config.FIGURE_03_COMMUNES_GEOJSON_PATH),
            },
            "crop": {
                "width": image_width,
                "height": image_height,
                "bounds3857": [float(value) for value in crop_bounds],
                "paddingRatio": config.FIGURE_03_SATELLITE_PADDING_RATIO,
            },
            "stats": {
                "proper": {"areaKm2": proper_area_km2},
                "built": {
                    "areaKm2": built_area_km2,
                    "population2015": ghsl_info["population2015"],
                    "clusterId": ghsl_info["clusterId"],
                    "urbanThreshold": ghsl_info["urbanThreshold"],
                },
                "functional": {"areaKm2": attraction_area_km2},
            },
            "simplifyToleranceMeters": config.FIGURE_03_SIMPLIFY_TOLERANCE_METERS,
        },
        "scenes": build_scenes(),
        "map": {
            "viewport": {
                "viewBox": [0, 0, image_width, image_height],
                "background": config.FIGURE_03_VIEWPORT_BACKGROUND,
            },
            "layers": [
                {
                    "id": "satellite",
                    "kind": "image",
                    "href": "/data/figures/figure-03-satellite.png",
                    "x": 0,
                    "y": 0,
                    "width": image_width,
                    "height": image_height,
                    "opacity": 1,
                },
                {
                    "id": "attraction-fill",
                    "kind": "paths",
                    "items": [
                        {
                            "id": "attraction-fill-shape",
                            "d": attraction_path,
                            "fill": "#67e0cc",
                            "fillOpacity": 0.10,
                        }
                    ],
                },
                {
                    "id": "built-fill",
                    "kind": "paths",
                    "items": [
                        {
                            "id": "built-fill-shape",
                            "d": built_path,
                            "fill": "#cfd6dd",
                            "fillOpacity": 0.22,
                        }
                    ],
                },
                {
                    "id": "proper-boundary",
                    "kind": "paths",
                    "items": [
                        {
                            "id": "proper-boundary-shape",
                            "d": proper_path,
                            "stroke": "#ff8b67",
                            "strokeWidth": 6,
                        }
                    ],
                },
                {
                    "id": "attraction-boundary",
                    "kind": "paths",
                    "items": [
                        {
                            "id": "attraction-boundary-shape",
                            "d": attraction_path,
                            "stroke": "#67e0cc",
                            "strokeWidth": 4,
                        }
                    ],
                },
            ],
        },
    }


def build_figure_03_payload(engine: Engine) -> tuple[dict[str, Any], np.ndarray]:
    validate_source_paths()

    paris_admin_union, paris_aav_union = load_admin_and_aav_shapes()
    paris_ghsl_shape, ghsl_info = load_ghsl_shape(engine)

    proper_area_km2 = float(paris_admin_union.to_crs(2154).geometry.iloc[0].area / 1_000_000)
    attraction_area_km2 = float(paris_aav_union.to_crs(2154).geometry.iloc[0].area / 1_000_000)
    built_area_km2 = float(paris_ghsl_shape.to_crs(2154).geometry.iloc[0].area / 1_000_000)

    with rasterio.open(config.FIGURE_03_SATELLITE_TIFF_PATH) as raster:
        paris_admin_union = paris_admin_union.to_crs(raster.crs)
        paris_aav_union = paris_aav_union.to_crs(raster.crs)
        paris_ghsl_shape = paris_ghsl_shape.to_crs(raster.crs)

        crop_box = build_crop_box(paris_aav_union.geometry.iloc[0])
        out_image, out_transform = mask(raster, [crop_box], crop=True)

    proper_geom = geometry_to_pixel_space(
        paris_admin_union.geometry.iloc[0].simplify(
            config.FIGURE_03_SIMPLIFY_TOLERANCE_METERS["proper"],
            preserve_topology=True,
        ),
        out_transform,
    )
    built_geom = geometry_to_pixel_space(
        paris_ghsl_shape.geometry.iloc[0].simplify(
            config.FIGURE_03_SIMPLIFY_TOLERANCE_METERS["built"],
            preserve_topology=True,
        ),
        out_transform,
    )
    attraction_geom = geometry_to_pixel_space(
        paris_aav_union.geometry.iloc[0].simplify(
            config.FIGURE_03_SIMPLIFY_TOLERANCE_METERS["functional"],
            preserve_topology=True,
        ),
        out_transform,
    )

    image_uint8 = np.clip(out_image * 255.0, 0, 255).astype(np.uint8)
    image_height, image_width = int(image_uint8.shape[1]), int(image_uint8.shape[2])
    crop_bounds = rasterio.transform.array_bounds(image_height, image_width, out_transform)

    payload = build_payload(
        image_width=image_width,
        image_height=image_height,
        proper_path=geometry_to_svg_path(proper_geom),
        built_path=geometry_to_svg_path(built_geom),
        attraction_path=geometry_to_svg_path(attraction_geom),
        crop_bounds=crop_bounds,
        ghsl_info=ghsl_info,
        proper_area_km2=proper_area_km2,
        built_area_km2=built_area_km2,
        attraction_area_km2=attraction_area_km2,
    )
    validate_payload(payload)
    return payload, image_uint8


def validate_payload(payload: dict[str, Any]) -> None:
    if payload["id"] != "figure-03":
        raise ValueError("Unexpected figure-03 payload id.")
    map_payload = payload["map"]
    layers = map_payload["layers"]
    if len(layers) != 5:
        raise ValueError(f"Expected 5 map layers, found {len(layers)}.")
    if layers[0]["kind"] != "image":
        raise ValueError("First layer must be the satellite image.")
    path_layer_ids = [layer["id"] for layer in layers[1:]]
    expected_ids = [
        "attraction-fill",
        "built-fill",
        "proper-boundary",
        "attraction-boundary",
    ]
    if path_layer_ids != expected_ids:
        raise ValueError(f"Unexpected layer ids: {path_layer_ids!r}")
