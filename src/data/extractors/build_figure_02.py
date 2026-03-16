from __future__ import annotations

import json
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

import config
from figure02 import (
    build_payload,
    fetch_world_population,
    fetch_world_urban_population,
    fetch_yacc_clusters,
    fetch_yacc_country_count,
    validate_payload,
)


PROJECT_ROOT = Path(__file__).resolve().parents[3]


def resolve_output_path() -> Path:
    if config.OUTPUT_PATH_FIGURE_02.is_absolute():
        return config.OUTPUT_PATH_FIGURE_02
    return PROJECT_ROOT / config.OUTPUT_PATH_FIGURE_02


def validate_config() -> None:
    if not config.DATABASE_URL:
        raise ValueError("DATABASE_URL is not set. Export it before running the extractor.")
    if config.FIGURE_02_BRICK_POPULATION <= 0:
        raise ValueError("FIGURE_02_BRICK_POPULATION must be positive.")
    if config.FIGURE_02_BASELINE_YEAR >= config.FIGURE_02_TARGET_YEAR:
        raise ValueError("Figure-02 baseline year must be earlier than the target year.")


def main() -> None:
    validate_config()

    engine = create_engine(config.DATABASE_URL)
    try:
        df_yacc_clusters = fetch_yacc_clusters(engine)
        yacc_country_count = fetch_yacc_country_count(engine)
        df_world_urban_population = fetch_world_urban_population(engine)
        df_world_population = fetch_world_population(engine)
    except OperationalError as exc:
        raise RuntimeError(
            "Could not connect to Postgres using DATABASE_URL. "
            "Start the database or point DATABASE_URL at a reachable instance."
        ) from exc

    payload = build_payload(
        df_yacc_clusters=df_yacc_clusters,
        yacc_country_count=yacc_country_count,
        df_world_urban_population=df_world_urban_population,
        df_world_population=df_world_population,
    )
    validate_payload(payload)

    output_path = resolve_output_path()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(payload, file, ensure_ascii=True, separators=(",", ":"))
        file.write("\n")

    print(output_path)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        raise SystemExit(str(exc)) from exc
