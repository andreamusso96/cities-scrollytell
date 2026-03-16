from __future__ import annotations

import json
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

import config
from figure07 import build_payload, fetch_yearly_prd_clusters, validate_payload


PROJECT_ROOT = Path(__file__).resolve().parents[3]


def resolve_output_path() -> Path:
    if config.OUTPUT_PATH_FIGURE_07.is_absolute():
        return config.OUTPUT_PATH_FIGURE_07
    return PROJECT_ROOT / config.OUTPUT_PATH_FIGURE_07


def validate_config() -> None:
    if not config.DATABASE_URL:
        raise ValueError("DATABASE_URL is not set. Export it before running the extractor.")
    if config.FIGURE_07_SIMPLIFY_TOLERANCE_METERS <= 0:
        raise ValueError("FIGURE_07_SIMPLIFY_TOLERANCE_METERS must be positive.")
    if len(config.FIGURE_07_BBOX_LON_LAT) != 4:
        raise ValueError("FIGURE_07_BBOX_LON_LAT must contain [min_lon, min_lat, max_lon, max_lat].")


def main() -> None:
    validate_config()

    engine = create_engine(config.DATABASE_URL)
    try:
        yearly_clusters = fetch_yearly_prd_clusters(engine)
    except OperationalError as exc:
        raise RuntimeError(
            "Could not connect to Postgres using DATABASE_URL. "
            "Start the database or point DATABASE_URL at a reachable instance."
        ) from exc

    payload = build_payload(yearly_clusters)
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
