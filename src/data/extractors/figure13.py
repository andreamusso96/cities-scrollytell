from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

import numpy as np
import pandas as pd
from sqlalchemy import Engine, text

import config
from figure08 import validate_table_name


def fetch_projection_table(engine: Engine, table_name: str) -> pd.DataFrame:
    safe_table_name = validate_table_name(table_name)
    query = text(
        f"""
        SELECT
            year,
            country,
            population,
            total_population_share_cities_above_one_million
        FROM {safe_table_name}
        WHERE analysis_id = :analysis_id
        ORDER BY year, country
        """
    )
    return pd.read_sql(query, con=engine, params={"analysis_id": config.ANALYSIS_ID})


def aggregate_world_series(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        raise ValueError("Scenario source table returned no rows.")

    required_columns = {
        "year",
        "country",
        "population",
        "total_population_share_cities_above_one_million",
    }
    if not required_columns.issubset(df.columns):
        missing = sorted(required_columns.difference(df.columns))
        raise ValueError(f"Scenario source table is missing required columns: {missing!r}")

    working = df.copy()
    working["population_in_1m_plus_cities"] = (
        working["population"] * working["total_population_share_cities_above_one_million"]
    )

    aggregated = (
        working.groupby("year", as_index=False)
        .agg(
            totalPopulation=("population", "sum"),
            populationIn1MPlusCities=("population_in_1m_plus_cities", "sum"),
            countryCount=("country", "nunique"),
        )
        .sort_values("year")
        .reset_index(drop=True)
    )
    aggregated["shareIn1MPlusCities"] = (
        aggregated["populationIn1MPlusCities"] / aggregated["totalPopulation"]
    )
    aggregated["populationIn1MPlusCitiesBillions"] = (
        aggregated["populationIn1MPlusCities"] / 1_000_000_000.0
    )
    return aggregated


def build_spliced_series(
    history_series: pd.DataFrame,
    future_series: pd.DataFrame,
) -> pd.DataFrame:
    historical = history_series.loc[
        history_series["year"] <= config.FIGURE_13_SPLICE_YEAR
    ].copy()
    future = future_series.loc[
        future_series["year"] > config.FIGURE_13_SPLICE_YEAR
    ].copy()
    combined = pd.concat([historical, future], ignore_index=True)
    return combined.sort_values("year").reset_index(drop=True)


def build_x_axis(series_by_id: dict[str, pd.DataFrame]) -> dict[str, Any]:
    min_year = min(int(series["year"].min()) for series in series_by_id.values())
    max_year = max(int(series["year"].max()) for series in series_by_id.values())
    return {
        "domain": [min_year, max_year],
        "ticks": [
            {"value": tick_year, "label": str(tick_year)}
            for tick_year in config.FIGURE_13_X_TICKS
            if min_year <= tick_year <= max_year
        ],
        "label": config.FIGURE_13_X_AXIS_LABEL,
        "scale": "linear",
    }


def build_y_axis() -> dict[str, Any]:
    return {
        "domain": list(config.FIGURE_13_Y_DOMAIN),
        "ticks": [
            {"value": tick_value, "label": f"{tick_value}B"}
            for tick_value in config.FIGURE_13_Y_TICKS
        ],
        "label": config.FIGURE_13_Y_AXIS_LABEL,
    }


def build_lines(series_by_id: dict[str, pd.DataFrame]) -> list[dict[str, Any]]:
    lines = []
    for scenario in config.FIGURE_13_SCENARIOS:
        series = series_by_id[scenario["id"]]
        lines.append(
            {
                "id": scenario["id"],
                "color": scenario["color"],
                "width": config.LINE_WIDTH,
                "points": [
                    {
                        "x": int(row.year),
                        "y": float(row.populationIn1MPlusCitiesBillions),
                    }
                    for row in series.itertuples(index=False)
                ],
                "endLabel": {
                    "text": scenario["shortLabel"],
                    "placement": "right-column",
                    "dx": scenario["endLabelDx"],
                    "dy": scenario["endLabelDy"],
                    "anchor": "start",
                },
            }
        )
    return lines


def build_legend() -> list[dict[str, str]]:
    return [
        {
            "id": scenario["id"],
            "label": scenario["label"],
            "color": scenario["color"],
        }
        for scenario in config.FIGURE_13_SCENARIOS
    ]


def build_meta(
    raw_tables: dict[str, pd.DataFrame],
    aggregated_tables: dict[str, pd.DataFrame],
    series_by_id: dict[str, pd.DataFrame],
) -> dict[str, Any]:
    lifecycle_series = series_by_id["lifecycle"]
    splice_year = config.FIGURE_13_SPLICE_YEAR

    return {
        "analysisId": config.ANALYSIS_ID,
        "sourceTables": {
            "lifecycle": config.WORLD_TOT_POP_SHARE_CITIES_ABOVE_1M_TABLE,
            "extrapolation": config.WORLD_TOT_POP_SHARE_CITIES_ABOVE_1M_EXTR_TABLE,
            "runaway": config.WORLD_TOT_POP_SHARE_CITIES_ABOVE_1M_INC_RETURNS_TABLE,
            "proportional": config.WORLD_TOT_POP_SHARE_CITIES_ABOVE_1M_PROP_GROWTH_TABLE,
        },
        "generatedAt": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "rowCounts": {
            "raw": {key: int(len(table)) for key, table in raw_tables.items()},
            "aggregatedYears": {
                key: int(len(table))
                for key, table in aggregated_tables.items()
            },
        },
        "series": {
            "sharedHistoryThroughYear": splice_year,
            "years": {
                scenario_id: series["year"].astype(int).tolist()
                for scenario_id, series in series_by_id.items()
            },
            "valuesAtSpliceYearBillions": {
                scenario_id: float(
                    series.loc[
                        series["year"] == splice_year,
                        "populationIn1MPlusCitiesBillions",
                    ].iloc[0]
                )
                for scenario_id, series in series_by_id.items()
            },
            "valuesAt2100Billions": {
                scenario_id: float(
                    series.loc[
                        series["year"] == int(series["year"].max()),
                        "populationIn1MPlusCitiesBillions",
                    ].iloc[0]
                )
                for scenario_id, series in series_by_id.items()
            },
            "lifecycleShares": {
                "1975": float(
                    lifecycle_series.loc[
                        lifecycle_series["year"] == 1975,
                        "shareIn1MPlusCities",
                    ].iloc[0]
                ),
                "2025": float(
                    lifecycle_series.loc[
                        lifecycle_series["year"] == 2025,
                        "shareIn1MPlusCities",
                    ].iloc[0]
                ),
                "2100": float(
                    lifecycle_series.loc[
                        lifecycle_series["year"] == 2100,
                        "shareIn1MPlusCities",
                    ].iloc[0]
                ),
            },
        },
        "notes": {
            "scenarioConstruction": (
                "Historical values through 2025 come from the lifecycle table for every line. "
                "Scenario-specific projections are spliced in for years after 2025."
            )
        },
        "payloadId": "figure-13",
    }


def build_payload(
    raw_tables: dict[str, pd.DataFrame],
    aggregated_tables: dict[str, pd.DataFrame],
    series_by_id: dict[str, pd.DataFrame],
) -> dict[str, Any]:
    return {
        "id": "figure-13",
        "kind": config.FIGURE_13_KIND,
        "meta": build_meta(raw_tables, aggregated_tables, series_by_id),
        "legend": build_legend(),
        "graph": {
            "xAxis": build_x_axis(series_by_id),
            "yAxis": build_y_axis(),
            "lines": build_lines(series_by_id),
            "margins": config.FIGURE_13_GRAPH_MARGINS,
        },
    }


def validate_payload(payload: dict[str, Any]) -> None:
    graph = payload["graph"]
    actual_line_ids = [line["id"] for line in graph["lines"]]
    expected_line_ids = [scenario["id"] for scenario in config.FIGURE_13_SCENARIOS]
    if actual_line_ids != expected_line_ids:
        raise ValueError(f"Unexpected line order: {actual_line_ids!r}")

    y_domain = graph["yAxis"]["domain"]
    if y_domain[0] > 0:
        raise ValueError("Y-axis domain must include 0.")

    lifecycle_points: list[tuple[int, float]] | None = None
    for line in graph["lines"]:
        points = line["points"]
        if not points:
            raise ValueError(f"Line {line['id']} has no points.")

        x_values = np.asarray([point["x"] for point in points], dtype=float)
        y_values = np.asarray([point["y"] for point in points], dtype=float)
        if not np.all(np.isfinite(x_values)) or not np.all(np.isfinite(y_values)):
            raise ValueError(f"Line {line['id']} contains non-finite values.")
        if not np.all(np.diff(x_values) > 0):
            raise ValueError(f"Line {line['id']} x-values must be strictly increasing.")
        if int(x_values[0]) != 1975 or int(x_values[-1]) != 2100:
            raise ValueError(f"Line {line['id']} must span 1975 to 2100.")
        if "endLabel" not in line:
            raise ValueError(f"Line {line['id']} is missing an end label.")

        history_points = [
            (int(point["x"]), float(point["y"]))
            for point in points
            if int(point["x"]) <= config.FIGURE_13_SPLICE_YEAR
        ]
        if line["id"] == "lifecycle":
            lifecycle_points = history_points
        elif lifecycle_points is not None and history_points != lifecycle_points:
            raise ValueError(
                f"Scenario line {line['id']} does not share the lifecycle history through "
                f"{config.FIGURE_13_SPLICE_YEAR}."
            )


def build_figure_13_payload(engine: Engine) -> dict[str, Any]:
    raw_tables = {
        scenario["sourceKey"]: fetch_projection_table(engine, scenario["tableName"])
        for scenario in config.FIGURE_13_SCENARIOS
    }
    aggregated_tables = {
        key: aggregate_world_series(table)
        for key, table in raw_tables.items()
    }

    lifecycle_series = aggregated_tables["lifecycle"]
    series_by_id = {}
    for scenario in config.FIGURE_13_SCENARIOS:
        scenario_id = scenario["id"]
        source_key = scenario["sourceKey"]
        if scenario_id == "lifecycle":
            series_by_id[scenario_id] = lifecycle_series.copy()
        else:
            series_by_id[scenario_id] = build_spliced_series(
                lifecycle_series,
                aggregated_tables[source_key],
            )

    payload = build_payload(raw_tables, aggregated_tables, series_by_id)
    validate_payload(payload)
    return payload
