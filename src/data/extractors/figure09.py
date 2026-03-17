from __future__ import annotations

from datetime import datetime, timezone
import math
from typing import Any

import numpy as np
import pandas as pd
from pygam import LinearGAM, s
from sqlalchemy import Engine, text

import config
from figure08 import (
    build_line_points,
    build_x_axis,
    fit_world_curve,
    format_percent_label,
    interpolate_annotation_values,
    log10_growth_to_percent,
    validate_table_name,
)


def _region_params() -> dict[str, Any]:
    params: dict[str, Any] = {"analysis_id": config.ANALYSIS_ID}
    for index, region in enumerate(config.FIGURE_09_REGION_ORDER):
        params[f"region_{index}"] = region
    return params


def _region_placeholders() -> str:
    return ", ".join(f":region_{index}" for index, _ in enumerate(config.FIGURE_09_REGION_ORDER))


def fetch_size_vs_growth_by_region(engine: Engine) -> pd.DataFrame:
    table_name = validate_table_name(config.WORLD_SIZE_VS_GROWTH_TABLE)
    query = text(
        f"""
        SELECT log_population, normalized_log_growth, region
        FROM {table_name}
        WHERE analysis_id = :analysis_id
          AND region IN ({_region_placeholders()})
        ORDER BY region, log_population
        """
    )
    return pd.read_sql(query, con=engine, params=_region_params())


def fetch_average_growth_by_region(engine: Engine) -> pd.DataFrame:
    table_name = validate_table_name(config.WORLD_AVERAGE_GROWTH_TABLE)
    query = text(
        f"""
        SELECT log_average_growth, region
        FROM {table_name}
        WHERE analysis_id = :analysis_id
          AND region IN ({_region_placeholders()})
        ORDER BY region
        """
    )
    return pd.read_sql(query, con=engine, params=_region_params())


def fit_region_curve(
    df_size_vs_growth: pd.DataFrame,
    df_average_growth: pd.DataFrame,
) -> dict[str, np.ndarray | float]:
    if df_size_vs_growth.empty:
        raise ValueError("No rows returned for regional size-vs-growth fit.")
    if df_average_growth.empty:
        raise ValueError("No rows returned for regional average-growth fit.")

    x_values = df_size_vs_growth[["log_population"]].to_numpy()
    y_values = df_size_vs_growth["normalized_log_growth"].to_numpy()

    x_min = float(df_size_vs_growth["log_population"].min())
    x_max = float(df_size_vs_growth["log_population"].max())
    if x_min >= x_max:
        raise ValueError("Observed regional log-population range is invalid.")

    model = LinearGAM(
        s(0, n_splines=config.N_SPLINES),
        lam=[config.PENALTY_SIZE_GROWTH_CURVE],
        fit_intercept=False,
    ).fit(x_values, y_values)

    x_grid = np.linspace(x_min, x_max, config.FIT_GRID_SIZE)
    x_grid_2d = x_grid.reshape(-1, 1)
    y_partial, confidence_interval = model.partial_dependence(term=0, X=x_grid_2d, width=0.95)

    average_log_growth = float(df_average_growth["log_average_growth"].mean())
    y_fitted_log = average_log_growth + y_partial
    ci_low_log = average_log_growth + confidence_interval[:, 0]
    ci_high_log = average_log_growth + confidence_interval[:, 1]

    return {
        "x_log": x_grid,
        "x_population": np.power(10.0, x_grid),
        "y_pct": log10_growth_to_percent(y_fitted_log),
        "ci_low_pct": log10_growth_to_percent(ci_low_log),
        "ci_high_pct": log10_growth_to_percent(ci_high_log),
        "average_log_growth": average_log_growth,
    }


def build_regional_y_axis(curve_results: list[dict[str, np.ndarray | float]]) -> dict[str, Any]:
    if config.FIGURE_09_Y_DOMAIN and config.FIGURE_09_Y_TICKS:
        return {
            "domain": list(config.FIGURE_09_Y_DOMAIN),
            "ticks": [
                {"value": value, "label": format_percent_label(value)}
                for value in config.FIGURE_09_Y_TICKS
            ],
            "label": config.Y_AXIS_LABEL,
        }

    raw_min = 0.0
    raw_max = 0.0
    for result in curve_results:
        y_pct = result["y_pct"]
        ci_low_pct = result["ci_low_pct"]
        ci_high_pct = result["ci_high_pct"]
        if not isinstance(y_pct, np.ndarray):
            raise TypeError("Expected numpy arrays in curve results.")
        if not isinstance(ci_low_pct, np.ndarray):
            raise TypeError("Expected numpy arrays in curve results.")
        if not isinstance(ci_high_pct, np.ndarray):
            raise TypeError("Expected numpy arrays in curve results.")
        raw_min = min(raw_min, float(np.min(y_pct)), float(np.min(ci_low_pct)))
        raw_max = max(raw_max, float(np.max(y_pct)), float(np.max(ci_high_pct)))

    domain_min = int(10 * math.floor(raw_min / 10))
    domain_max = int(10 * math.ceil(raw_max / 10))
    if domain_min == domain_max:
        domain_min -= 10
        domain_max += 10

    tick_values = list(range(domain_min, domain_max + 10, 10))
    if 0 not in tick_values:
        tick_values.append(0)
        tick_values.sort()

    return {
        "domain": [domain_min, domain_max],
        "ticks": [{"value": value, "label": format_percent_label(value)} for value in tick_values],
        "label": config.Y_AXIS_LABEL,
    }


def format_compact_percent(value: float) -> str:
    prefix = "+" if value > 0 else ""
    if math.isclose(value, 0.0, abs_tol=1e-9):
        prefix = ""
    return f"{prefix}{value:.1f}%"


def build_world_annotations(annotation_values: list[dict[str, float]]) -> list[dict[str, Any]]:
    annotations = []
    for item in annotation_values:
        population = int(item["population"])
        layout = config.ANNOTATION_LAYOUT.get(population, {})
        annotations.append(
            {
                "id": f"{config.LINE_ID}-{population}",
                "lineId": config.LINE_ID,
                "point": {"x": item["population"], "y": item["fittedPct"]},
                "title": config.ANNOTATION_TEXT.get(population, str(population)),
                "subtitle": format_compact_percent(item["fittedPct"]),
                **layout,
            }
        )
    return annotations


def build_lines(
    world_fit: dict[str, np.ndarray | float],
    region_fits: dict[str, dict[str, np.ndarray | float]],
) -> list[dict[str, Any]]:
    world_x_population = world_fit["x_population"]
    world_y_pct = world_fit["y_pct"]
    if not isinstance(world_x_population, np.ndarray):
        raise TypeError("Expected numpy arrays in world fit result.")
    if not isinstance(world_y_pct, np.ndarray):
        raise TypeError("Expected numpy arrays in world fit result.")

    lines = [
        {
            "id": config.LINE_ID,
            "color": config.LINE_COLOR,
            "width": config.LINE_WIDTH,
            "opacity": config.FIGURE_09_WORLD_OPACITY,
            "points": build_line_points(world_x_population, world_y_pct),
        }
    ]

    for region in config.FIGURE_09_REGION_ORDER:
        region_style = config.FIGURE_09_REGIONS[region]
        fit_result = region_fits[region]
        x_population = fit_result["x_population"]
        y_pct = fit_result["y_pct"]
        if not isinstance(x_population, np.ndarray):
            raise TypeError("Expected numpy arrays in region fit result.")
        if not isinstance(y_pct, np.ndarray):
            raise TypeError("Expected numpy arrays in region fit result.")

        lines.append(
            {
                "id": region_style["lineId"],
                "color": region_style["color"],
                "width": config.LINE_WIDTH,
                "points": build_line_points(x_population, y_pct),
                "endLabel": {
                    "text": region_style["shortLabel"],
                    "placement": "right-column",
                    "dx": region_style["endLabelDx"],
                    "dy": region_style["endLabelDy"],
                    "anchor": "start",
                },
            }
        )

    return lines


def build_legend() -> list[dict[str, str]]:
    legend = [{"id": config.LINE_ID, "label": config.LEGEND_LABEL, "color": config.LINE_COLOR}]
    for region in config.FIGURE_09_REGION_ORDER:
        region_style = config.FIGURE_09_REGIONS[region]
        legend.append(
            {
                "id": region_style["lineId"],
                "label": region_style["label"],
                "color": region_style["color"],
            }
        )
    return legend


def build_payload(
    df_size_vs_growth_by_region: pd.DataFrame,
    df_average_growth_by_region: pd.DataFrame,
    world_fit: dict[str, np.ndarray | float],
    region_fits: dict[str, dict[str, np.ndarray | float]],
) -> dict[str, Any]:
    world_annotation_values = interpolate_annotation_values(
        world_fit["x_log"],
        world_fit["y_pct"],
        world_fit["ci_low_pct"],
        world_fit["ci_high_pct"],
    )
    lines = build_lines(world_fit, region_fits)
    all_curve_results = [world_fit, *[region_fits[region] for region in config.FIGURE_09_REGION_ORDER]]

    return {
        "id": "figure-09",
        "kind": config.FIGURE_09_KIND,
        "meta": {
            "analysisId": config.ANALYSIS_ID,
            "sourceTables": {
                "worldSizeVsGrowth": config.WORLD_SIZE_VS_GROWTH_TABLE,
                "worldAverageGrowth": config.WORLD_AVERAGE_GROWTH_TABLE,
            },
            "generatedAt": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "rowCounts": {
                "worldSizeVsGrowth": int(len(df_size_vs_growth_by_region)),
                "worldAverageGrowth": int(len(df_average_growth_by_region)),
                "sizeVsGrowthByRegion": {
                    region: int((df_size_vs_growth_by_region["region"] == region).sum())
                    for region in config.FIGURE_09_REGION_ORDER
                },
                "averageGrowthByRegion": {
                    region: int((df_average_growth_by_region["region"] == region).sum())
                    for region in config.FIGURE_09_REGION_ORDER
                },
            },
            "fit": {
                "penaltySizeGrowthCurve": config.PENALTY_SIZE_GROWTH_CURVE,
                "nSplines": config.N_SPLINES,
                "fitGridSize": config.FIT_GRID_SIZE,
                "worldAverageLogGrowth": float(world_fit["average_log_growth"]),
                "regions": {
                    region: {
                        "averageLogGrowth": float(region_fits[region]["average_log_growth"]),
                        "minPopulation": float(np.min(region_fits[region]["x_population"])),
                        "maxPopulation": float(np.max(region_fits[region]["x_population"])),
                    }
                    for region in config.FIGURE_09_REGION_ORDER
                },
            },
            "annotationValues": world_annotation_values,
        },
        "legend": build_legend(),
        "graph": {
            "xAxis": build_x_axis(world_fit["x_population"]),
            "yAxis": build_regional_y_axis(all_curve_results),
            "lines": lines,
            "annotations": build_world_annotations(world_annotation_values),
            "margins": config.FIGURE_09_MARGINS,
        },
    }


def validate_payload(payload: dict[str, Any]) -> None:
    graph = payload["graph"]
    lines = graph["lines"]
    annotations = graph["annotations"]

    expected_line_ids = [
        config.LINE_ID,
        *[config.FIGURE_09_REGIONS[region]["lineId"] for region in config.FIGURE_09_REGION_ORDER],
    ]
    actual_line_ids = [line["id"] for line in lines]
    if actual_line_ids != expected_line_ids:
        raise ValueError(f"Unexpected figure-09 line order: {actual_line_ids!r}")

    if len(annotations) != 3:
        raise ValueError(f"Expected 3 world annotations, found {len(annotations)}.")

    for line in lines:
        points = line["points"]
        if not points:
            raise ValueError(f"Line {line['id']} has no points.")
        x_values = np.array([point["x"] for point in points], dtype=float)
        y_values = np.array([point["y"] for point in points], dtype=float)
        if not np.all(np.isfinite(x_values)) or not np.all(np.isfinite(y_values)):
            raise ValueError(f"Line {line['id']} contains non-finite values.")
        if not np.all(np.diff(x_values) > 0):
            raise ValueError(f"Line {line['id']} x-values must be strictly increasing.")

    y_domain = graph["yAxis"]["domain"]
    if y_domain[0] > 0 or y_domain[1] < 0:
        raise ValueError("Y-axis domain must include 0.")

    world_annotation_values = payload["meta"]["annotationValues"]
    x_domain = graph["xAxis"]["domain"]
    for item in world_annotation_values:
        if not (x_domain[0] <= item["population"] <= x_domain[1]):
            raise ValueError("World annotation population lies outside the x-axis domain.")
        if not (item["ciLowPct"] <= item["fittedPct"] <= item["ciHighPct"]):
            raise ValueError("World annotation fitted value lies outside its confidence interval.")

    for region in config.FIGURE_09_REGION_ORDER:
        line_id = config.FIGURE_09_REGIONS[region]["lineId"]
        line = next(line for line in lines if line["id"] == line_id)
        if "endLabel" not in line:
            raise ValueError(f"Regional line {line_id} is missing an end label.")
