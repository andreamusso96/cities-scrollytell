from __future__ import annotations

from typing import Any

from sqlalchemy import Engine

import config
from figure_periods import (
    assign_periods,
    build_meta,
    build_payload,
    fetch_average_growth_table,
    fetch_normalized_table,
    fit_curve,
    validate_payload,
)


def map_usa_year_to_period(year: int) -> str | None:
    if year >= 1850 and year < 1930:
        return "usa-early"
    if year >= 1930 and year <= 2020:
        return "usa-late"
    return None


def build_period_specs() -> list[dict[str, Any]]:
    return [
        {**config.FIGURE_11_PERIODS[0], "sourceKey": "usa"},
        {**config.FIGURE_11_PERIODS[1], "sourceKey": "usa"},
    ]


def build_figure_11_payload(engine: Engine) -> dict[str, Any]:
    df_usa_normalized = fetch_normalized_table(engine, config.USA_SIZE_VS_GROWTH_NORMALIZED_TABLE)
    df_usa_average = fetch_average_growth_table(engine, config.USA_AVERAGE_GROWTH_TABLE)

    df_usa_normalized = assign_periods(df_usa_normalized, map_usa_year_to_period)
    df_usa_average = assign_periods(df_usa_average, map_usa_year_to_period)

    period_specs = build_period_specs()
    fit_results = {
        period["id"]: fit_curve(
            df_usa_normalized[df_usa_normalized["periodId"] == period["id"]].copy(),
            df_usa_average[df_usa_average["periodId"] == period["id"]].copy(),
        )
        for period in period_specs
    }
    period_years = {
        period["id"]: sorted(
            df_usa_normalized.loc[df_usa_normalized["periodId"] == period["id"], "year"].unique().tolist()
        )
        for period in period_specs
    }

    meta = build_meta(
        payload_id="figure-11",
        period_normalized_sources={"usa": df_usa_normalized},
        period_average_sources={"usa": df_usa_average},
        fit_results=fit_results,
        period_specs=period_specs,
        period_years=period_years,
        source_tables={
            "usaSizeVsGrowthNormalized": config.USA_SIZE_VS_GROWTH_NORMALIZED_TABLE,
            "usaAverageGrowth": config.USA_AVERAGE_GROWTH_TABLE,
        },
        source_row_counts={
            "usaSizeVsGrowthNormalized": int(len(df_usa_normalized)),
            "usaAverageGrowth": int(len(df_usa_average)),
        },
    )
    payload = build_payload(
        payload_id="figure-11",
        kind=config.FIGURE_11_KIND,
        period_specs=period_specs,
        fit_results=fit_results,
        meta=meta,
    )
    validate_payload(payload, expected_line_ids=[period["id"] for period in period_specs])
    return payload
