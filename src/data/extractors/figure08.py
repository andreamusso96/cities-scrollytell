from __future__ import annotations

from datetime import datetime, timezone
import math
import re
from typing import Any

import numpy as np
import pandas as pd
from pygam import LinearGAM, s
from sqlalchemy import Engine, text

import config


TABLE_NAME_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def validate_table_name(table_name: str) -> str:
    if not TABLE_NAME_RE.match(table_name):
        raise ValueError(f"Unsafe table name: {table_name!r}")
    return table_name


def fetch_size_vs_growth(engine: Engine) -> pd.DataFrame:
    table_name = validate_table_name(config.WORLD_SIZE_VS_GROWTH_TABLE)
    query = text(
        f"""
        SELECT log_population, normalized_log_growth
        FROM {table_name}
        WHERE analysis_id = :analysis_id
        ORDER BY log_population
        """
    )
    return pd.read_sql(query, con=engine, params={"analysis_id": config.ANALYSIS_ID})


def fetch_average_growth(engine: Engine) -> pd.DataFrame:
    table_name = validate_table_name(config.WORLD_AVERAGE_GROWTH_TABLE)
    query = text(
        f"""
        SELECT log_average_growth
        FROM {table_name}
        WHERE analysis_id = :analysis_id
        """
    )
    return pd.read_sql(query, con=engine, params={"analysis_id": config.ANALYSIS_ID})


def fit_world_curve(
    df_size_vs_growth: pd.DataFrame,
    df_average_growth: pd.DataFrame,
) -> dict[str, np.ndarray | float]:
    if df_size_vs_growth.empty:
        raise ValueError("No rows returned from world size-vs-growth table.")
    if df_average_growth.empty:
        raise ValueError("No rows returned from world average-growth table.")

    x_values = df_size_vs_growth[["log_population"]].to_numpy()
    y_values = df_size_vs_growth["normalized_log_growth"].to_numpy()

    x_min = float(df_size_vs_growth["log_population"].min())
    x_max = float(df_size_vs_growth["log_population"].max())
    if x_min >= x_max:
        raise ValueError("Observed log-population range is invalid.")

    for population in config.ANNOTATION_POPULATIONS:
        log_population = math.log10(population)
        if log_population < x_min or log_population > x_max:
            raise ValueError(
                f"Annotation population {population} lies outside the fitted x-range "
                f"[{x_min}, {x_max}]."
            )

    model = LinearGAM(
        s(0, n_splines=config.N_SPLINES),
        lam=[config.PENALTY_SIZE_GROWTH_CURVE],
        fit_intercept=False,
    ).fit(x_values, y_values)

    x_grid = np.linspace(x_min, x_max, config.FIT_GRID_SIZE)
    x_grid_2d = x_grid.reshape(-1, 1)
    y_partial, confidence_interval = model.partial_dependence(term=0, X=x_grid_2d, width=0.95)

    average_log_growth = float(df_average_growth["log_average_growth"].mean())
    y_fitted = average_log_growth + y_partial
    ci_low = average_log_growth + confidence_interval[:, 0]
    ci_high = average_log_growth + confidence_interval[:, 1]

    return {
        "x_log": x_grid,
        "x_population": np.power(10.0, x_grid),
        "y_pct": y_fitted * 100.0,
        "ci_low_pct": ci_low * 100.0,
        "ci_high_pct": ci_high * 100.0,
        "average_log_growth": average_log_growth,
    }


def format_population_label(value: float) -> str:
    if value >= 1_000_000_000:
        unit = 1_000_000_000
        suffix = "B"
    elif value >= 1_000_000:
        unit = 1_000_000
        suffix = "M"
    elif value >= 1_000:
        unit = 1_000
        suffix = "K"
    else:
        return str(int(round(value)))

    scaled = value / unit
    if scaled >= 10 or math.isclose(scaled, round(scaled), abs_tol=0.05):
        return f"{int(round(scaled))}{suffix}"
    return f"{scaled:.1f}{suffix}"


def build_x_ticks(domain_min: float, domain_max: float) -> list[dict[str, float | str]]:
    tick_values: list[float] = []
    labeled_ticks = {
        10_000.0: "10K",
        100_000.0: "100K",
        1_000_000.0: "1M",
        10_000_000.0: "10M",
    }

    def add_tick(value: float) -> None:
        if not any(math.isclose(value, existing, rel_tol=1e-6, abs_tol=1e-6) for existing in tick_values):
            tick_values.append(value)

    add_tick(domain_min)
    min_power = math.ceil(math.log10(domain_min))
    max_power = math.floor(math.log10(domain_max))
    for power in range(min_power, max_power + 1):
        add_tick(10.0**power)
    add_tick(domain_max)

    tick_values.sort()
    ticks = []
    for value in tick_values:
        label = ""
        for labeled_value, labeled_text in labeled_ticks.items():
            if math.isclose(value, labeled_value, rel_tol=1e-6, abs_tol=1e-6):
                label = labeled_text
                break
        ticks.append({"value": value, "label": label})
    return ticks


def build_x_axis(x_population: np.ndarray) -> dict[str, Any]:
    domain_min = float(np.min(x_population))
    domain_max = float(np.max(x_population))
    return {
        "domain": [domain_min, domain_max],
        "ticks": build_x_ticks(domain_min, domain_max),
        "label": config.X_AXIS_LABEL,
        "scale": "log",
    }


def format_percent_label(value: int) -> str:
    if value > 0:
        return f"+{value}%"
    return f"{value}%"


def build_y_axis(y_pct: np.ndarray, ci_low_pct: np.ndarray, ci_high_pct: np.ndarray) -> dict[str, Any]:
    raw_min = min(float(np.min(y_pct)), float(np.min(ci_low_pct)), 0.0)
    raw_max = max(float(np.max(y_pct)), float(np.max(ci_high_pct)), 0.0)

    domain_min = int(2 * math.floor(raw_min / 2))
    domain_max = int(2 * math.ceil(raw_max / 2))
    if domain_min == domain_max:
        domain_min -= 2
        domain_max += 2

    tick_start = int(10 * math.floor(domain_min / 10))
    tick_end = int(10 * math.ceil(domain_max / 10))
    tick_values = [
        value for value in range(tick_start, tick_end + 10, 10) if domain_min <= value <= domain_max
    ]
    if 0 not in tick_values:
        tick_values.append(0)
        tick_values.sort()

    ticks = [{"value": value, "label": format_percent_label(value)} for value in tick_values]

    return {
        "domain": [domain_min, domain_max],
        "ticks": ticks,
        "label": config.Y_AXIS_LABEL,
    }


def build_line_points(x_population: np.ndarray, y_pct: np.ndarray) -> list[dict[str, float]]:
    return [
        {"x": float(population), "y": float(value)}
        for population, value in zip(x_population, y_pct, strict=True)
    ]


def format_annotation_subtitle(value: float) -> str:
    prefix = "+" if value > 0 else ""
    if math.isclose(value, 0.0, abs_tol=1e-9):
        prefix = ""
    return f"{prefix}{value:.1f}% next-decade growth"


def interpolate_annotation_values(
    x_log: np.ndarray,
    y_pct: np.ndarray,
    ci_low_pct: np.ndarray,
    ci_high_pct: np.ndarray,
) -> list[dict[str, float]]:
    values = []
    for population in config.ANNOTATION_POPULATIONS:
        population_log = math.log10(population)
        fitted_pct = float(np.interp(population_log, x_log, y_pct))
        ci_low = float(np.interp(population_log, x_log, ci_low_pct))
        ci_high = float(np.interp(population_log, x_log, ci_high_pct))
        values.append(
            {
                "population": float(population),
                "logPopulation": population_log,
                "fittedPct": fitted_pct,
                "ciLowPct": ci_low,
                "ciHighPct": ci_high,
            }
        )
    return values


def build_annotations(annotation_values: list[dict[str, float]]) -> list[dict[str, Any]]:
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
                "subtitle": format_annotation_subtitle(item["fittedPct"]),
                **layout,
            }
        )
    return annotations


def build_graph_payload(fit_result: dict[str, np.ndarray | float]) -> dict[str, Any]:
    x_log = fit_result["x_log"]
    x_population = fit_result["x_population"]
    y_pct = fit_result["y_pct"]
    ci_low_pct = fit_result["ci_low_pct"]
    ci_high_pct = fit_result["ci_high_pct"]

    if not isinstance(x_log, np.ndarray):
        raise TypeError("Expected numpy arrays in fit result.")
    if not isinstance(x_population, np.ndarray):
        raise TypeError("Expected numpy arrays in fit result.")
    if not isinstance(y_pct, np.ndarray):
        raise TypeError("Expected numpy arrays in fit result.")
    if not isinstance(ci_low_pct, np.ndarray):
        raise TypeError("Expected numpy arrays in fit result.")
    if not isinstance(ci_high_pct, np.ndarray):
        raise TypeError("Expected numpy arrays in fit result.")

    annotation_values = interpolate_annotation_values(x_log, y_pct, ci_low_pct, ci_high_pct)

    graph = {
        "xAxis": build_x_axis(x_population),
        "yAxis": build_y_axis(y_pct, ci_low_pct, ci_high_pct),
        "lines": [
            {
                "id": config.LINE_ID,
                "color": config.LINE_COLOR,
                "width": config.LINE_WIDTH,
                "points": build_line_points(x_population, y_pct),
            }
        ],
        "annotations": build_annotations(annotation_values),
    }
    return {"graph": graph, "annotationValues": annotation_values}


def build_payload(
    df_size_vs_growth: pd.DataFrame,
    df_average_growth: pd.DataFrame,
    fit_result: dict[str, np.ndarray | float],
) -> dict[str, Any]:
    graph_payload = build_graph_payload(fit_result)
    annotation_values = graph_payload.pop("annotationValues")

    return {
        "id": "figure-08",
        "kind": "xy-world",
        "meta": {
            "analysisId": config.ANALYSIS_ID,
            "sourceTables": {
                "worldSizeVsGrowth": config.WORLD_SIZE_VS_GROWTH_TABLE,
                "worldAverageGrowth": config.WORLD_AVERAGE_GROWTH_TABLE,
            },
            "generatedAt": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "rowCounts": {
                "worldSizeVsGrowth": int(len(df_size_vs_growth)),
                "worldAverageGrowth": int(len(df_average_growth)),
            },
            "fit": {
                "penaltySizeGrowthCurve": config.PENALTY_SIZE_GROWTH_CURVE,
                "nSplines": config.N_SPLINES,
                "fitGridSize": config.FIT_GRID_SIZE,
                "averageLogGrowth": float(fit_result["average_log_growth"]),
            },
            "annotationValues": annotation_values,
        },
        "graph": graph_payload["graph"],
    }


def validate_payload(payload: dict[str, Any]) -> None:
    graph = payload["graph"]
    lines = graph["lines"]
    annotations = graph["annotations"]

    if len(lines) != 1:
        raise ValueError(f"Expected 1 line, found {len(lines)}.")
    if len(annotations) != 3:
        raise ValueError(f"Expected 3 annotations, found {len(annotations)}.")

    points = lines[0]["points"]
    if not points:
        raise ValueError("Line points are empty.")

    x_values = np.array([point["x"] for point in points], dtype=float)
    y_values = np.array([point["y"] for point in points], dtype=float)
    if not np.all(np.isfinite(x_values)) or not np.all(np.isfinite(y_values)):
        raise ValueError("Line points contain non-finite values.")
    if not np.all(np.diff(x_values) > 0):
        raise ValueError("Line point x-values must be strictly increasing.")

    y_domain = graph["yAxis"]["domain"]
    if y_domain[0] > 0 or y_domain[1] < 0:
        raise ValueError("Y-axis domain must include 0.")

    x_domain = graph["xAxis"]["domain"]
    annotation_values = payload["meta"]["annotationValues"]
    for item in annotation_values:
        if not (x_domain[0] <= item["population"] <= x_domain[1]):
            raise ValueError("Annotation population lies outside the x-axis domain.")
        if not (item["ciLowPct"] <= item["fittedPct"] <= item["ciHighPct"]):
            raise ValueError("Annotation fitted value lies outside its confidence interval.")
