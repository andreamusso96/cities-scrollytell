from __future__ import annotations

import json
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

import config
from figure12 import build_figure_12_payload


PROJECT_ROOT = Path(__file__).resolve().parents[3]


def resolve_output_path() -> Path:
    if config.OUTPUT_PATH_FIGURE_12.is_absolute():
        return config.OUTPUT_PATH_FIGURE_12
    return PROJECT_ROOT / config.OUTPUT_PATH_FIGURE_12


def validate_config() -> None:
    if not config.DATABASE_URL:
        raise ValueError("DATABASE_URL is not set. Export it before running the extractor.")
    if config.PENALTY_SIZE_GROWTH_CURVE <= 0:
        raise ValueError("PENALTY_SIZE_GROWTH_CURVE must be positive.")
    if config.N_SPLINES < 4:
        raise ValueError("N_SPLINES must be at least 4.")
    if config.FIT_GRID_SIZE < 10:
        raise ValueError("FIT_GRID_SIZE must be at least 10.")


def main() -> None:
    validate_config()

    engine = create_engine(config.DATABASE_URL)
    try:
        payload = build_figure_12_payload(engine)
    except OperationalError as exc:
        raise RuntimeError(
            "Could not connect to Postgres using DATABASE_URL. "
            "Start the database or point DATABASE_URL at a reachable instance."
        ) from exc

    output_path = resolve_output_path()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=True, separators=(",", ":"))
        f.write("\n")

    print(output_path)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        raise SystemExit(str(exc)) from exc
