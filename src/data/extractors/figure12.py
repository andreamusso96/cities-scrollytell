from __future__ import annotations

from typing import Any

from sqlalchemy import Engine

import config
from figure11 import map_usa_year_to_period
from figure_periods import (
    assign_periods,
    build_meta,
    build_payload,
    fetch_average_growth_table,
    fetch_normalized_table,
    fit_curve,
    validate_payload,
)


def map_korea_year_to_period(year: int) -> str | None:
    if year >= 1975 and year < 1995:
        return "korea-early"
    if year >= 2000 and year < 2025:
        return "korea-late"
    return None


def build_period_specs() -> list[dict[str, Any]]:
    return [
        {**config.FIGURE_12_PERIODS[0], "sourceKey": "usa"},
        {**config.FIGURE_12_PERIODS[1], "sourceKey": "usa"},
        {**config.FIGURE_12_PERIODS[2], "sourceKey": "korea"},
        {**config.FIGURE_12_PERIODS[3], "sourceKey": "korea"},
    ]


def build_figure_12_payload(engine: Engine) -> dict[str, Any]:
    df_usa_normalized = fetch_normalized_table(engine, config.USA_SIZE_VS_GROWTH_NORMALIZED_TABLE)
    df_usa_average = fetch_average_growth_table(engine, config.USA_AVERAGE_GROWTH_TABLE)
    df_korea_normalized = fetch_normalized_table(
        engine,
        config.WORLD_SIZE_VS_GROWTH_TABLE,
        where="country = 'KOR'",
    )
    df_korea_average = fetch_average_growth_table(
        engine,
        config.WORLD_AVERAGE_GROWTH_TABLE,
        where="country = 'KOR'",
    )

    df_usa_normalized = assign_periods(df_usa_normalized, map_usa_year_to_period)
    df_usa_average = assign_periods(df_usa_average, map_usa_year_to_period)
    df_korea_normalized = assign_periods(df_korea_normalized, map_korea_year_to_period)
    df_korea_average = assign_periods(df_korea_average, map_korea_year_to_period)

    period_specs = build_period_specs()
    fit_results = {}
    period_years = {}
    for period in period_specs:
        if period["sourceKey"] == "usa":
            normalized_source = df_usa_normalized
            average_source = df_usa_average
        else:
            normalized_source = df_korea_normalized
            average_source = df_korea_average

        fit_results[period["id"]] = fit_curve(
            normalized_source[normalized_source["periodId"] == period["id"]].copy(),
            average_source[average_source["periodId"] == period["id"]].copy(),
        )
        period_years[period["id"]] = sorted(
            normalized_source.loc[normalized_source["periodId"] == period["id"], "year"].unique().tolist()
        )

    korea_all_years = sorted(df_korea_normalized["year"].unique().tolist())
    korea_included_years = sorted(
        df_korea_normalized.loc[df_korea_normalized["periodId"].notna(), "year"].unique().tolist()
    )
    korea_excluded_years = [year for year in korea_all_years if year not in korea_included_years]

    meta = build_meta(
        payload_id="figure-12",
        period_normalized_sources={
            "usa": df_usa_normalized,
            "korea": df_korea_normalized,
        },
        period_average_sources={
            "usa": df_usa_average,
            "korea": df_korea_average,
        },
        fit_results=fit_results,
        period_specs=period_specs,
        period_years=period_years,
        source_tables={
            "usaSizeVsGrowthNormalized": config.USA_SIZE_VS_GROWTH_NORMALIZED_TABLE,
            "usaAverageGrowth": config.USA_AVERAGE_GROWTH_TABLE,
            "koreaSizeVsGrowthNormalized": config.WORLD_SIZE_VS_GROWTH_TABLE,
            "koreaAverageGrowth": config.WORLD_AVERAGE_GROWTH_TABLE,
        },
        source_row_counts={
            "usaSizeVsGrowthNormalized": int(len(df_usa_normalized)),
            "usaAverageGrowth": int(len(df_usa_average)),
            "koreaSizeVsGrowthNormalized": int(len(df_korea_normalized)),
            "koreaAverageGrowth": int(len(df_korea_average)),
        },
        extra_period_notes={
            "koreaLegacyMapping": {
                "label": "1975-2000 vs 2000-2025",
                "yearsExcluded": korea_excluded_years,
            }
        },
    )
    payload = build_payload(
        payload_id="figure-12",
        kind=config.FIGURE_12_KIND,
        period_specs=period_specs,
        fit_results=fit_results,
        meta=meta,
    )
    validate_payload(payload, expected_line_ids=[period["id"] for period in period_specs])
    return payload
