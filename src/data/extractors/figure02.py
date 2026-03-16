from __future__ import annotations

from datetime import datetime, timezone
import math
from typing import Any

import pandas as pd
from sqlalchemy import Engine, text

import config
from figure08 import validate_table_name


def _bin_config_by_id() -> dict[str, dict[str, Any]]:
    return {bin_config["id"]: bin_config for bin_config in config.FIGURE_02_BINS}


def _assign_bin_id(population: float) -> str:
    for bin_config in config.FIGURE_02_BINS:
        min_population = float(bin_config["minPopulation"])
        max_population = bin_config["maxPopulation"]
        if population < min_population:
            continue
        if max_population is None or population < float(max_population):
            return str(bin_config["id"])
    raise ValueError(f"Could not assign population {population} to a figure-02 bin.")


def fetch_yacc_clusters(engine: Engine) -> pd.DataFrame:
    table_name = validate_table_name(config.WORLD_CLUSTER_GROWTH_POPULATION_COUNTRY_ANALYSIS_TABLE)
    query = text(
        f"""
        SELECT DISTINCT ON (cluster_id)
            cluster_id,
            population_y1
        FROM {table_name}
        WHERE analysis_id = :analysis_id
          AND y1 = :baseline_year
          AND y2 = :baseline_year
        ORDER BY cluster_id
        """
    )
    return pd.read_sql(
        query,
        con=engine,
        params={
            "analysis_id": config.ANALYSIS_ID,
            "baseline_year": config.FIGURE_02_BASELINE_YEAR,
        },
    )


def fetch_yacc_country_count(engine: Engine) -> int:
    table_name = validate_table_name(config.WORLD_CLUSTER_GROWTH_POPULATION_COUNTRY_ANALYSIS_TABLE)
    query = text(
        f"""
        SELECT COUNT(DISTINCT country) AS country_count
        FROM {table_name}
        WHERE analysis_id = :analysis_id
          AND y1 = :baseline_year
          AND y2 = :baseline_year
        """
    )
    with engine.connect() as connection:
        row = connection.execute(
            query,
            {
                "analysis_id": config.ANALYSIS_ID,
                "baseline_year": config.FIGURE_02_BASELINE_YEAR,
            },
        ).mappings().one()
    return int(row["country_count"])


def fetch_world_urban_population(engine: Engine) -> pd.DataFrame:
    table_name = validate_table_name(config.WORLD_URBAN_POPULATION_TABLE)
    query = text(
        f"""
        SELECT year, SUM(urban_population) AS urban_population
        FROM {table_name}
        WHERE year IN (:baseline_year, :reference_year, :target_year)
        GROUP BY year
        ORDER BY year
        """
    )
    return pd.read_sql(
        query,
        con=engine,
        params={
            "baseline_year": config.FIGURE_02_BASELINE_YEAR,
            "reference_year": config.FIGURE_02_REFERENCE_YEAR,
            "target_year": config.FIGURE_02_TARGET_YEAR,
        },
    )


def fetch_world_population(engine: Engine) -> pd.DataFrame:
    table_name = validate_table_name(config.WORLD_POPULATION_RAW_TABLE)
    query = text(
        f"""
        SELECT
            "Year" AS year,
            COALESCE("Population (projections)", "Population (historical)") AS population
        FROM {table_name}
        WHERE "Entity" = 'World'
          AND "Year" IN (:baseline_year, :reference_year, :target_year)
        ORDER BY "Year"
        """
    )
    return pd.read_sql(
        query,
        con=engine,
        params={
            "baseline_year": config.FIGURE_02_BASELINE_YEAR,
            "reference_year": config.FIGURE_02_REFERENCE_YEAR,
            "target_year": config.FIGURE_02_TARGET_YEAR,
        },
    )


def build_yacc_baseline(df_clusters: pd.DataFrame) -> dict[str, Any]:
    if df_clusters.empty:
        raise ValueError("No rows returned from the YACC cluster population table.")

    if df_clusters["cluster_id"].duplicated().any():
        raise ValueError("YACC cluster query still contains duplicate cluster_id values.")

    baseline = df_clusters.copy()
    baseline["population_y1"] = baseline["population_y1"].astype(float)
    baseline["binId"] = baseline["population_y1"].map(_assign_bin_id)

    total_population = float(baseline["population_y1"].sum())
    grouped = (
        baseline.groupby("binId", sort=False)["population_y1"]
        .sum()
        .rename("population")
        .to_dict()
    )

    bins = []
    for bin_config in config.FIGURE_02_BINS:
        bin_population = float(grouped.get(bin_config["id"], 0.0))
        bins.append(
            {
                "id": bin_config["id"],
                "label": bin_config["label"],
                "sublabel": bin_config["sublabel"],
                "population": bin_population,
                "share": bin_population / total_population,
            }
        )

    return {
        "bins": bins,
        "clusterCount": int(len(baseline)),
        "population": total_population,
    }


def _population_label(population: float) -> str:
    if population >= 1_000_000_000:
        return f"{population / 1_000_000_000:.1f}B people"
    if population >= 1_000_000:
        return f"{population / 1_000_000:.0f}M people"
    if population >= 1_000:
        return f"{population / 1_000:.0f}K people"
    return f"{population:.0f} people"


def _allocate_bricks(total_population: float, weights: list[float]) -> dict[str, Any]:
    if total_population < 0:
        raise ValueError("Population passed to brick allocation cannot be negative.")
    if not weights:
        raise ValueError("Brick allocation requires at least one weight.")

    total_weight = sum(weights)
    if not math.isclose(total_weight, 1.0, rel_tol=1e-9, abs_tol=1e-9):
        raise ValueError(f"Scenario weights must sum to 1.0, got {total_weight}.")

    population_per_brick = float(config.FIGURE_02_BRICK_POPULATION)
    total_bricks = int(round(total_population / population_per_brick))
    exact_bricks = [total_bricks * weight for weight in weights]
    floor_bricks = [math.floor(value) for value in exact_bricks]

    remaining = total_bricks - sum(floor_bricks)
    if remaining < 0:
        raise ValueError("Rounded brick allocation produced too many floor bricks.")

    remainders = [exact - floor for exact, floor in zip(exact_bricks, floor_bricks, strict=True)]
    remainder_order = sorted(
        range(len(remainders)),
        key=lambda index: (remainders[index], -index),
        reverse=True,
    )

    counts = floor_bricks[:]
    for index in remainder_order[:remaining]:
        counts[index] += 1

    represented_population = total_bricks * population_per_brick
    return {
        "counts": counts,
        "totalBricks": total_bricks,
        "exactBricks": exact_bricks,
        "representedPopulation": represented_population,
        "errorPopulation": represented_population - total_population,
    }


def build_payload(
    df_yacc_clusters: pd.DataFrame,
    yacc_country_count: int,
    df_world_urban_population: pd.DataFrame,
    df_world_population: pd.DataFrame,
) -> dict[str, Any]:
    baseline = build_yacc_baseline(df_yacc_clusters)

    urban_population_by_year = {
        int(row["year"]): float(row["urban_population"])
        for _, row in df_world_urban_population.iterrows()
    }
    world_population_by_year = {
        int(row["year"]): float(row["population"])
        for _, row in df_world_population.iterrows()
    }

    required_years = {
        config.FIGURE_02_BASELINE_YEAR,
        config.FIGURE_02_REFERENCE_YEAR,
        config.FIGURE_02_TARGET_YEAR,
    }
    if set(urban_population_by_year) != required_years:
        raise ValueError("World urban population query did not return the expected years.")
    if set(world_population_by_year) != required_years:
        raise ValueError("World population query did not return the expected years.")

    baseline_year = config.FIGURE_02_BASELINE_YEAR
    reference_year = config.FIGURE_02_REFERENCE_YEAR
    target_year = config.FIGURE_02_TARGET_YEAR
    ordered_years = [baseline_year, reference_year, target_year]

    baseline_urban_population = urban_population_by_year[baseline_year]
    added_urban_population_2050 = urban_population_by_year[reference_year] - baseline_urban_population
    added_urban_population_2100 = urban_population_by_year[target_year] - baseline_urban_population

    baseline_weights = [float(bin_row["share"]) for bin_row in baseline["bins"]]
    baseline_bricks = _allocate_bricks(baseline_urban_population, baseline_weights)
    future_bricks_2050 = _allocate_bricks(added_urban_population_2050, baseline_weights)
    future_bricks_balanced = _allocate_bricks(added_urban_population_2100, baseline_weights)

    scenarios: list[dict[str, Any]] = []
    scenes: list[dict[str, Any]] = []
    max_future_by_bin = [0] * len(config.FIGURE_02_BINS)

    baseline_bins = []
    for index, bin_row in enumerate(baseline["bins"]):
        baseline_bins.append(
            {
                "id": bin_row["id"],
                "label": bin_row["label"],
                "sublabel": bin_row["sublabel"],
                "yaccPopulation2025": bin_row["population"],
                "yaccShare2025": bin_row["share"],
                "allocatedUrbanPopulation2025": baseline_urban_population * bin_row["share"],
                "baseCount": baseline_bricks["counts"][index],
                "baseExactBrickQuota": baseline_bricks["exactBricks"][index],
            }
        )

    for scenario in config.FIGURE_02_SCENARIOS:
        scenario_id = scenario["id"]
        weight_mode = scenario.get("weightMode")
        if weight_mode == "none":
            future_counts = [0] * len(config.FIGURE_02_BINS)
            scenario_weights = [0.0] * len(config.FIGURE_02_BINS)
            future_population_by_bin = [0.0] * len(config.FIGURE_02_BINS)
            future_exact_bricks = [0.0] * len(config.FIGURE_02_BINS)
            total_future_bricks = 0
            represented_population = 0.0
            error_population = 0.0
        else:
            if weight_mode == "baseline-shares":
                scenario_weights = baseline_weights
                allocation = future_bricks_balanced
            else:
                scenario_weights = [float(value) for value in scenario["weights"]]
                allocation = _allocate_bricks(added_urban_population_2100, scenario_weights)

            future_counts = allocation["counts"]
            future_population_by_bin = [
                added_urban_population_2100 * weight for weight in scenario_weights
            ]
            future_exact_bricks = allocation["exactBricks"]
            total_future_bricks = int(allocation["totalBricks"])
            represented_population = float(allocation["representedPopulation"])
            error_population = float(allocation["errorPopulation"])

        max_future_by_bin = [
            max(current_max, future_count)
            for current_max, future_count in zip(max_future_by_bin, future_counts, strict=True)
        ]

        scenarios.append(
            {
                "id": scenario_id,
                "title": scenario["title"],
                "weights": scenario_weights,
                "futurePopulation2100": future_population_by_bin,
                "futureCounts": future_counts,
                "futureExactBrickQuota": future_exact_bricks,
                "futureTotalBricks": total_future_bricks,
                "representedFuturePopulation2100": represented_population,
                "futurePopulationError": error_population,
            }
        )

        scenes.append(
            {
                "id": scenario_id,
                "title": scenario["title"],
                "bins": [
                    {"label": bin_config["label"], "sublabel": bin_config["sublabel"]}
                    for bin_config in config.FIGURE_02_BINS
                ],
                "baseCounts": baseline_bricks["counts"],
                "futureCounts": future_counts,
                "futureColor": scenario["futureColor"],
                "futureLabel": scenario["futureLabel"],
            }
        )

    return {
        "id": "figure-02",
        "kind": config.FIGURE_02_KIND,
        "meta": {
            "analysisId": config.ANALYSIS_ID,
            "generatedAt": datetime.now(timezone.utc).isoformat(),
            "sourceTables": {
                "yaccClusters": config.WORLD_CLUSTER_GROWTH_POPULATION_COUNTRY_ANALYSIS_TABLE,
                "worldUrbanPopulation": config.WORLD_URBAN_POPULATION_TABLE,
                "worldPopulation": config.WORLD_POPULATION_RAW_TABLE,
            },
            "webSources": config.FIGURE_02_WEB_SOURCES,
            "baselineYear": baseline_year,
            "referenceYear": reference_year,
            "targetYear": target_year,
            "notes": [
                "2025 size-bin shares come from YACC clusters deduplicated on cluster_id to avoid double-counting cross-border cities.",
                "Those YACC 2025 shares are applied to the warehouse's global urban-population series to get a world-scale brick baseline.",
                "The public UN web sources are used as external context; the 2100 brick horizon itself comes from the local world_urban_population series so it stays definitionally consistent with the warehouse.",
            ],
            "coverage": {
                "countryCount": yacc_country_count,
                "uniqueClusterCount": baseline["clusterCount"],
                "yaccPopulation2025": baseline["population"],
            },
            "urbanPopulation": {
                str(baseline_year): baseline_urban_population,
                str(reference_year): urban_population_by_year[reference_year],
                str(target_year): urban_population_by_year[target_year],
                f"{baseline_year}To{reference_year}Added": added_urban_population_2050,
                f"{baseline_year}To{target_year}Added": added_urban_population_2100,
            },
            "worldPopulation": {
                str(baseline_year): world_population_by_year[baseline_year],
                str(reference_year): world_population_by_year[reference_year],
                str(target_year): world_population_by_year[target_year],
            },
            "urbanShareOfWorldPopulation": {
                str(year): urban_population_by_year[year] / world_population_by_year[year]
                for year in ordered_years
            },
            "brick": {
                "populationPerBrick": config.FIGURE_02_BRICK_POPULATION,
                "populationPerBrickLabel": _population_label(config.FIGURE_02_BRICK_POPULATION),
                "allocationMethod": "largest remainder from exact brick quotas",
                "baselineTotalBricks": baseline_bricks["totalBricks"],
                "baselineRepresentedPopulation": baseline_bricks["representedPopulation"],
                "baselinePopulationError": baseline_bricks["errorPopulation"],
                "futureTotalBricks2050": future_bricks_2050["totalBricks"],
                "futureRepresentedPopulation2050": future_bricks_2050["representedPopulation"],
                "futurePopulationError2050": future_bricks_2050["errorPopulation"],
                "futureTotalBricks2100": future_bricks_balanced["totalBricks"],
                "futureRepresentedPopulation2100": future_bricks_balanced["representedPopulation"],
                "futurePopulationError2100": future_bricks_balanced["errorPopulation"],
                "maxFutureByBin": max_future_by_bin,
            },
            "baselineBins": baseline_bins,
            "scenarios": scenarios,
        },
        "scenes": scenes,
    }


def validate_payload(payload: dict[str, Any]) -> None:
    if payload["id"] != "figure-02":
        raise ValueError("Figure-02 payload id is invalid.")

    scenes = payload["scenes"]
    if len(scenes) != len(config.FIGURE_02_SCENARIOS):
        raise ValueError("Figure-02 payload scene count is invalid.")

    base_counts = scenes[0]["baseCounts"]
    if not all(scene["baseCounts"] == base_counts for scene in scenes):
        raise ValueError("All figure-02 scenes must share the same baseline counts.")

    expected_base_total = payload["meta"]["brick"]["baselineTotalBricks"]
    if sum(base_counts) != expected_base_total:
        raise ValueError("Figure-02 baseline bricks do not sum to the configured total.")

    max_future_by_bin = payload["meta"]["brick"]["maxFutureByBin"]
    for scene in scenes:
        if len(scene["bins"]) != len(config.FIGURE_02_BINS):
            raise ValueError("Every figure-02 scene must contain exactly four bins.")
        if len(scene["futureCounts"]) != len(config.FIGURE_02_BINS):
            raise ValueError("Every figure-02 scene must contain exactly four future counts.")
        for index, count in enumerate(scene["futureCounts"]):
            if count > max_future_by_bin[index]:
                raise ValueError("Figure-02 maxFutureByBin is smaller than a scene count.")

    scenario_meta = payload["meta"]["scenarios"]
    if len(scenario_meta) != len(scenes):
        raise ValueError("Figure-02 scenario metadata and scene counts differ.")

    for scenario in scenario_meta:
        weights = scenario["weights"]
        if weights and any(weight < 0 for weight in weights):
            raise ValueError("Figure-02 scenario weights cannot be negative.")
        if any(weight > 0 for weight in weights):
            if not math.isclose(sum(weights), 1.0, rel_tol=1e-9, abs_tol=1e-9):
                raise ValueError("Figure-02 scenario weights must sum to 1.")
