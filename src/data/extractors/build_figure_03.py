from __future__ import annotations

import json
from pathlib import Path

import rasterio
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

import config
from figure03 import build_figure_03_payload


PROJECT_ROOT = Path(__file__).resolve().parents[3]


def resolve_output_path(path: Path) -> Path:
    if path.is_absolute():
        return path
    return PROJECT_ROOT / path


def validate_config() -> None:
    if not config.DATABASE_URL:
        raise ValueError("DATABASE_URL is not set. Export it before running the extractor.")


def write_png(output_path: Path, image_data) -> None:
    with rasterio.open(
        output_path,
        "w",
        driver="PNG",
        width=image_data.shape[2],
        height=image_data.shape[1],
        count=image_data.shape[0],
        dtype=image_data.dtype,
    ) as dst:
        dst.write(image_data)


def main() -> None:
    validate_config()

    engine = create_engine(config.DATABASE_URL)
    try:
        payload, image_data = build_figure_03_payload(engine)
    except OperationalError as exc:
        raise RuntimeError(
            "Could not connect to Postgres using DATABASE_URL. "
            "Start the database or point DATABASE_URL at a reachable instance."
        ) from exc

    json_output_path = resolve_output_path(config.OUTPUT_PATH_FIGURE_03)
    image_output_path = resolve_output_path(config.OUTPUT_PATH_FIGURE_03_IMAGE)
    json_output_path.parent.mkdir(parents=True, exist_ok=True)
    image_output_path.parent.mkdir(parents=True, exist_ok=True)

    write_png(image_output_path, image_data)
    with json_output_path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=True, separators=(",", ":"))
        f.write("\n")

    print(json_output_path)
    print(image_output_path)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        raise SystemExit(str(exc)) from exc
