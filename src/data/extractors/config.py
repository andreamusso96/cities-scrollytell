from pathlib import Path
import os


DATABASE_URL = os.getenv("DATABASE_URL", "")

ANALYSIS_ID = 1

WORLD_SIZE_VS_GROWTH_TABLE = "world_size_vs_growth_normalized"
WORLD_AVERAGE_GROWTH_TABLE = "world_average_growth"
USA_SIZE_VS_GROWTH_NORMALIZED_TABLE = "usa_size_vs_growth_normalized"
USA_AVERAGE_GROWTH_TABLE = "usa_average_growth"

PENALTY_SIZE_GROWTH_CURVE = 100
N_SPLINES = 20
FIT_GRID_SIZE = 100

ANNOTATION_POPULATIONS = [100_000, 1_000_000, 10_000_000]

OUTPUT_PATH = Path("static/data/figures/figure-08.json")
OUTPUT_PATH_FIGURE_09 = Path("static/data/figures/figure-09.json")
OUTPUT_PATH_FIGURE_11 = Path("static/data/figures/figure-11.json")
OUTPUT_PATH_FIGURE_12 = Path("static/data/figures/figure-12.json")

LINE_ID = "world"
LINE_COLOR = "#67e0cc"
LINE_WIDTH = 5
LEGEND_LABEL = "World"

X_AXIS_LABEL = "City population"
Y_AXIS_LABEL = "Growth relative to national urban average"

ANNOTATION_TEXT = {
    100_000: "100K",
    1_000_000: "1M",
    10_000_000: "10M",
}

ANNOTATION_LAYOUT = {
    100_000: {"orientation": "above"},
    1_000_000: {"orientation": "above"},
    10_000_000: {"orientation": "above", "align": "end", "dx": -12},
}

FIGURE_09_KIND = "xy-regions"
FIGURE_09_WORLD_OPACITY = 0.72
FIGURE_09_MARGINS = {"right": 88}
FIGURE_09_REGION_ORDER = ["Asia", "Africa", "Europe", "Americas"]
FIGURE_09_REGIONS = {
    "Asia": {
        "lineId": "asia",
        "label": "Asia",
        "shortLabel": "AS",
        "color": "#ff8b67",
        "endLabelDx": 18,
        "endLabelDy": -4,
    },
    "Africa": {
        "lineId": "africa",
        "label": "Africa",
        "shortLabel": "AF",
        "color": "#f1c56d",
        "endLabelDx": 18,
        "endLabelDy": 0,
    },
    "Europe": {
        "lineId": "europe",
        "label": "Europe",
        "shortLabel": "EU",
        "color": "#8ac6ff",
        "endLabelDx": 18,
        "endLabelDy": 4,
    },
    "Americas": {
        "lineId": "americas",
        "label": "Americas",
        "shortLabel": "AM",
        "color": "#b6dc7c",
        "endLabelDx": 18,
        "endLabelDy": 10,
    },
}

PERIODS_GRAPH_MARGINS = {"right": 88}

FIGURE_11_KIND = "xy-usa-periods"
FIGURE_11_PERIODS = [
    {
        "id": "usa-early",
        "label": "USA (1850-1930)",
        "shortLabel": "US1",
        "color": "#ff8b67",
        "endLabelDx": 18,
        "endLabelDy": -10,
        "yearsLabel": "1850-1930",
    },
    {
        "id": "usa-late",
        "label": "USA (1930-2020)",
        "shortLabel": "US2",
        "color": "#8ac6ff",
        "endLabelDx": 18,
        "endLabelDy": 8,
        "yearsLabel": "1930-2020",
    },
]

FIGURE_12_KIND = "xy-usa-korea-periods"
FIGURE_12_PERIODS = [
    {
        "id": "usa-early",
        "label": "USA (1850-1930)",
        "shortLabel": "US1",
        "color": "#ff8b67",
        "endLabelDx": 18,
        "endLabelDy": -14,
        "yearsLabel": "1850-1930",
    },
    {
        "id": "usa-late",
        "label": "USA (1930-2020)",
        "shortLabel": "US2",
        "color": "#8ac6ff",
        "endLabelDx": 18,
        "endLabelDy": -4,
        "yearsLabel": "1930-2020",
    },
    {
        "id": "korea-early",
        "label": "South Korea (1975-2000)",
        "shortLabel": "KR1",
        "color": "#f1c56d",
        "endLabelDx": 18,
        "endLabelDy": 10,
        "yearsLabel": "1975-2000",
    },
    {
        "id": "korea-late",
        "label": "South Korea (2000-2025)",
        "shortLabel": "KR2",
        "color": "#b6dc7c",
        "endLabelDx": 18,
        "endLabelDy": 12,
        "yearsLabel": "2000-2025",
    },
]
