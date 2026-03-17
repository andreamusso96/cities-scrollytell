from __future__ import annotations

from datetime import datetime, timezone
import math
from typing import Any, Callable

import numpy as np
import pandas as pd
from pygam import LinearGAM, s
from sqlalchemy import Engine, text

import config
from figure08 import (
    build_line_points,
    build_x_axis,
    format_percent_label,
    log10_growth_to_percent,
    validate_table_name,
)


PeriodMapper = Callable[[int], str | None]


def fetch_normalized_table(engine: Engine, table_name: str, where: str = "") -> pd.DataFrame:
    safe_table_name = validate_table_name(table_name)
    where_clause = f" AND {where}" if where else ""
    query = text(
        f"""
        SELECT year, log_population, normalized_log_growth
        FROM {safe_table_name}
        WHERE analysis_id = :analysis_id{where_clause}
        ORDER BY year, log_population
        """
    )
    return pd.read_sql(query, con=engine, params={"analysis_id": config.ANALYSIS_ID})


def fetch_average_growth_table(engine: Engine, table_name: str, where: str = "") -> pd.DataFrame:
    safe_table_name = validate_table_name(table_name)
    where_clause = f" AND {where}" if where else ""
    query = text(
        f"""
        SELECT year, log_average_growth
        FROM {safe_table_name}
        WHERE analysis_id = :analysis_id{where_clause}
        ORDER BY year
        """
    )
    return pd.read_sql(query, con=engine, params={"analysis_id": config.ANALYSIS_ID})


def assign_periods(df: pd.DataFrame, mapper: PeriodMapper) -> pd.DataFrame:
    with_periods = df.copy()
    with_periods["periodId"] = with_periods["year"].apply(lambda year: mapper(int(year)))
    return with_periods


def fit_curve(
    df_size_vs_growth: pd.DataFrame,
    df_average_growth: pd.DataFrame,
) -> dict[str, np.ndarray | float]:
    if df_size_vs_growth.empty:
        raise ValueError("No rows returned for period size-vs-growth fit.")
    if df_average_growth.empty:
        raise ValueError("No rows returned for period average-growth fit.")

    x_values = df_size_vs_growth[["log_population"]].to_numpy()
    y_values = df_size_vs_growth["normalized_log_growth"].to_numpy()

    x_min = float(df_size_vs_growth["log_population"].min())
    x_max = float(df_size_vs_growth["log_population"].max())
    if x_min >= x_max:
        raise ValueError("Observed period log-population range is invalid.")

    model = LinearGAM(
        s(0, n_splines=config.N_SPLINES),
        lam=[config.PENALTY_SIZE_GROWTH_CURVE],
        fit_intercept=False,
    ).fit(x_values, y_values)

    x_grid = np.linspace(x_min, x_max, config.FIT_GRID_SIZE)
    y_partial, confidence_interval = model.partial_dependence(
        term=0,
        X=x_grid.reshape(-1, 1),
        width=0.95,
    )

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


def build_multi_curve_y_axis(curve_results: list[dict[str, np.ndarray | float]]) -> dict[str, Any]:
    if config.PERIODS_Y_DOMAIN and config.PERIODS_Y_TICKS:
        return {
            "domain": list(config.PERIODS_Y_DOMAIN),
            "ticks": [
                {"value": value, "label": format_percent_label(value)}
                for value in config.PERIODS_Y_TICKS
            ],
            "label": config.Y_AXIS_LABEL,
        }

    raw_min = 0.0
    raw_max = 0.0
    for result in curve_results:
        y_pct = result["y_pct"]
        if not isinstance(y_pct, np.ndarray):
            raise TypeError("Expected numpy arrays in curve results.")
        raw_min = min(raw_min, float(np.min(y_pct)))
        raw_max = max(raw_max, float(np.max(y_pct)))

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


def build_lines(
    period_specs: list[dict[str, Any]],
    fit_results: dict[str, dict[str, np.ndarray | float]],
) -> list[dict[str, Any]]:
    lines = []
    for period in period_specs:
        fit_result = fit_results[period["id"]]
        x_population = fit_result["x_population"]
        y_pct = fit_result["y_pct"]
        if not isinstance(x_population, np.ndarray):
            raise TypeError("Expected numpy arrays in fit result.")
        if not isinstance(y_pct, np.ndarray):
            raise TypeError("Expected numpy arrays in fit result.")

        lines.append(
            {
                "id": period["id"],
                "color": period["color"],
                "width": config.LINE_WIDTH,
                **({"linePattern": period["linePattern"]} if period.get("linePattern") else {}),
                "points": build_line_points(x_population, y_pct),
                "endLabel": {
                    "text": period["shortLabel"],
                    "placement": "right-column",
                    "dx": period["endLabelDx"],
                    "dy": period["endLabelDy"],
                    "anchor": "start",
                },
            }
        )
    return lines


def build_legend(period_specs: list[dict[str, str]]) -> list[dict[str, str]]:
    return [
        {
            "id": period["id"],
            "label": period["label"],
            "color": period["color"],
            **({"linePattern": period["linePattern"]} if period.get("linePattern") else {}),
        }
        for period in period_specs
    ]


def build_meta(
    payload_id: str,
    period_normalized_sources: dict[str, pd.DataFrame],
    period_average_sources: dict[str, pd.DataFrame],
    fit_results: dict[str, dict[str, np.ndarray | float]],
    period_specs: list[dict[str, Any]],
    period_years: dict[str, list[int]],
    source_tables: dict[str, str],
    source_row_counts: dict[str, int],
    extra_period_notes: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "analysisId": config.ANALYSIS_ID,
        "sourceTables": source_tables,
        "generatedAt": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "rowCounts": {
            **source_row_counts,
            "periods": {
                period["id"]: {
                    "normalizedRows": int(
                        (period_normalized_sources[period["sourceKey"]]["periodId"] == period["id"]).sum()
                    ),
                    "averageGrowthRows": int(
                        (period_average_sources[period["sourceKey"]]["periodId"] == period["id"]).sum()
                    ),
                }
                for period in period_specs
            },
        },
        "fit": {
            "penaltySizeGrowthCurve": config.PENALTY_SIZE_GROWTH_CURVE,
            "nSplines": config.N_SPLINES,
            "fitGridSize": config.FIT_GRID_SIZE,
            "periods": {
                period["id"]: {
                    "label": period["yearsLabel"],
                    "yearsIncluded": period_years[period["id"]],
                    "averageLogGrowth": float(fit_results[period["id"]]["average_log_growth"]),
                    "minPopulation": float(np.min(fit_results[period["id"]]["x_population"])),
                    "maxPopulation": float(np.max(fit_results[period["id"]]["x_population"])),
                }
                for period in period_specs
            },
            **({"notes": extra_period_notes} if extra_period_notes else {}),
        },
        "payloadId": payload_id,
    }


def build_payload(
    payload_id: str,
    kind: str,
    period_specs: list[dict[str, Any]],
    fit_results: dict[str, dict[str, np.ndarray | float]],
    meta: dict[str, Any],
) -> dict[str, Any]:
    lines = build_lines(period_specs, fit_results)
    x_population = np.concatenate(
        [np.asarray(fit_results[period["id"]]["x_population"], dtype=float) for period in period_specs]
    )
    return {
        "id": payload_id,
        "kind": kind,
        "meta": meta,
        "legend": build_legend(period_specs),
        "graph": {
            "xAxis": build_x_axis(x_population),
            "yAxis": build_multi_curve_y_axis([fit_results[period["id"]] for period in period_specs]),
            "lines": lines,
            "margins": config.PERIODS_GRAPH_MARGINS,
        },
    }


def validate_payload(payload: dict[str, Any], expected_line_ids: list[str]) -> None:
    graph = payload["graph"]
    lines = graph["lines"]
    actual_line_ids = [line["id"] for line in lines]
    if actual_line_ids != expected_line_ids:
        raise ValueError(f"Unexpected line order: {actual_line_ids!r}")

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
        if "endLabel" not in line:
            raise ValueError(f"Line {line['id']} is missing an end label.")

    y_domain = graph["yAxis"]["domain"]
    if y_domain[0] > 0 or y_domain[1] < 0:
        raise ValueError("Y-axis domain must include 0.")
