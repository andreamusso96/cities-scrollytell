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
OUTPUT_PATH_FIGURE_02 = Path("static/data/figures/figure-02.json")
OUTPUT_PATH_FIGURE_07 = Path("static/data/figures/figure-07.json")
OUTPUT_PATH_FIGURE_09 = Path("static/data/figures/figure-09.json")
OUTPUT_PATH_FIGURE_11 = Path("static/data/figures/figure-11.json")
OUTPUT_PATH_FIGURE_12 = Path("static/data/figures/figure-12.json")
OUTPUT_PATH_FIGURE_13 = Path("static/data/figures/figure-13.json")
OUTPUT_PATH_FIGURE_03 = Path("static/data/figures/figure-03.json")
OUTPUT_PATH_FIGURE_03_IMAGE = Path("static/data/figures/figure-03-satellite.png")

WORLD_CLUSTER_GROWTH_POPULATION_COUNTRY_ANALYSIS_TABLE = (
    "world_cluster_growth_population_country_analysis"
)
WORLD_CLUSTER_GROWTH_GEOM_TABLE = "world_cluster_growth_geom"
WORLD_URBAN_POPULATION_TABLE = "world_urban_population"
WORLD_POPULATION_RAW_TABLE = "world_population_raw"
WORLD_TOT_POP_SHARE_CITIES_ABOVE_1M_TABLE = "world_tot_pop_share_cities_above_1m"
WORLD_TOT_POP_SHARE_CITIES_ABOVE_1M_EXTR_TABLE = (
    "world_tot_pop_share_cities_above_1m_projections_extr"
)
WORLD_TOT_POP_SHARE_CITIES_ABOVE_1M_INC_RETURNS_TABLE = (
    "world_tot_pop_share_cities_above_1m_projections_inc_returns"
)
WORLD_TOT_POP_SHARE_CITIES_ABOVE_1M_PROP_GROWTH_TABLE = (
    "world_tot_pop_share_cities_above_1m_projections_prop_growth"
)

FIGURE_02_KIND = "future-distribution"
FIGURE_02_BASELINE_YEAR = 2025
FIGURE_02_REFERENCE_YEAR = 2050
FIGURE_02_TARGET_YEAR = 2100
FIGURE_02_BRICK_POPULATION = 200_000_000
FIGURE_02_BINS = [
    {
        "id": "lt-100k",
        "label": "<100K",
        "sublabel": "small cities",
        "minPopulation": 0,
        "maxPopulation": 100_000,
    },
    {
        "id": "100k-1m",
        "label": "100K-1M",
        "sublabel": "mid-size metros",
        "minPopulation": 100_000,
        "maxPopulation": 1_000_000,
    },
    {
        "id": "1m-10m",
        "label": "1M-10M",
        "sublabel": "large metros",
        "minPopulation": 1_000_000,
        "maxPopulation": 10_000_000,
    },
    {
        "id": "10m-plus",
        "label": "10M+",
        "sublabel": "megacities",
        "minPopulation": 10_000_000,
        "maxPopulation": None,
    },
]
FIGURE_02_SCENARIOS = [
    {
        "id": "today",
        "title": "Today",
        "futureColor": "#2d3844",
        "futureLabel": "no future residents added yet",
        "weightMode": "none",
    },
    {
        "id": "balanced",
        "title": "Balanced growth",
        "futureColor": "#67e0cc",
        "futureLabel": "incoming residents: proportional growth",
        "weightMode": "baseline-shares",
    },
    {
        "id": "giants",
        "title": "Giants win",
        "futureColor": "#ff8b67",
        "futureLabel": "incoming residents: concentrated in large metros",
        "weights": [0.1, 0.2, 0.4, 0.3],
    },
    {
        "id": "distributed",
        "title": "Smaller cities catch up",
        "futureColor": "#f0c66f",
        "futureLabel": "incoming residents: spread toward smaller cities",
        "weights": [0.4, 0.3, 0.2, 0.1],
    },
]
FIGURE_02_WEB_SOURCES = [
    {
        "label": "UN DESA World Urbanization Prospects 2025",
        "url": "https://www.un.org/development/desa/pd/world-urbanization-prospects-2025",
        "note": "Latest official public UN urbanization release; headline summary publishes projections to 2050.",
    },
    {
        "label": "UN Global Issues: Population",
        "url": "https://www.un.org/en/global-issues/population",
        "note": "Latest official UN population overview with century-end world population context.",
    },
]

LINE_ID = "world"
LINE_COLOR = "#67e0cc"
LINE_WIDTH = 5
LEGEND_LABEL = "World"

X_AXIS_LABEL = "City population"
Y_AXIS_LABEL = "Decade growth rate"

FIGURE_08_Y_DOMAIN = [-5, 40]
FIGURE_08_Y_TICKS = [0, 10, 20, 30, 40]

ANNOTATION_TEXT = {
    100_000: "100K",
    1_000_000: "1M",
    10_000_000: "10M",
}

ANNOTATION_LAYOUT = {
    100_000: {"orientation": "above", "dy": 56},
    1_000_000: {"orientation": "above", "dy": 76},
    10_000_000: {"orientation": "above", "dy": 94},
}

FIGURE_09_KIND = "xy-regions"
FIGURE_09_WORLD_OPACITY = 0.72
FIGURE_09_MARGINS = {"right": 88}
FIGURE_09_Y_DOMAIN = [-5, 40]
FIGURE_09_Y_TICKS = [0, 10, 20, 30, 40]
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
PERIODS_Y_DOMAIN = [-25, 35]
PERIODS_Y_TICKS = [-20, -10, 0, 10, 20, 30]

FIGURE_03_KIND = "layered-map-paris"
FIGURE_03_VIEWPORT_BACKGROUND = "#0b1016"
FIGURE_03_SATELLITE_TIFF_PATH = Path(
    "/Users/andrea/Downloads/2025-04-29-00_00_2025-04-29-23_59_Sentinel-2_L2A_True_color (4).tiff"
)
FIGURE_03_AAV_XLSX_PATH = Path("/Users/andrea/Downloads/AAV2020_au_01-01-2022.xlsx")
FIGURE_03_COMMUNES_GEOJSON_PATH = Path("/Users/andrea/Downloads/commune-frmetdrom.geojson")
FIGURE_03_NOTEBOOK_PATH = Path("/Users/andrea/Desktop/PhD/Projects/Current/ZipfLaw/ZipfLaw/v6/nb6.1.ipynb")
FIGURE_03_GHSL_GWCODE = 220
FIGURE_03_GHSL_YEAR = 2015
FIGURE_03_SATELLITE_PADDING_RATIO = 0.08
FIGURE_03_SIMPLIFY_TOLERANCE_METERS = {
    "proper": 25,
    "built": 75,
    "functional": 150,
}

FIGURE_07_KIND = "layered-map-prd"
FIGURE_07_VIEWPORT_BACKGROUND = "#0b1016"
FIGURE_07_VIEWPORT_SIZE = 1200
FIGURE_07_BBOX_LON_LAT = [112.5, 21.8, 114.8, 23.6]
FIGURE_07_PADDING_RATIO = 0.03
FIGURE_07_DISPLAY_CRS = "EPSG:4547"
FIGURE_07_YEARS = [1975, 1985, 1995, 2005, 2015, 2025]
FIGURE_07_URBAN_THRESHOLD = 21
FIGURE_07_SIMPLIFY_TOLERANCE_METERS = 500
FIGURE_07_LABELS = [
    {"id": "guangzhou", "text": "Guangzhou", "lon": 113.2644, "lat": 23.1291},
    {"id": "shenzhen", "text": "Shenzhen", "lon": 114.0579, "lat": 22.5431},
    {"id": "hong-kong", "text": "Hong Kong", "lon": 114.1694, "lat": 22.3193},
]
FIGURE_07_YEAR_STYLES = {
    1975: {"fill": "#2f3a47", "fillOpacity": 0.36, "stroke": "#7a8794", "strokeOpacity": 0.85},
    1985: {"fill": "#3c4958", "fillOpacity": 0.42, "stroke": "#93a2b2", "strokeOpacity": 0.88},
    1995: {"fill": "#556478", "fillOpacity": 0.46, "stroke": "#b2c0cf", "strokeOpacity": 0.92},
    2005: {"fill": "#5c8f97", "fillOpacity": 0.48, "stroke": "#7ed7cb", "strokeOpacity": 0.95},
    2015: {"fill": "#67b3ad", "fillOpacity": 0.54, "stroke": "#8cf0de", "strokeOpacity": 0.98},
    2025: {"fill": "#67e0cc", "fillOpacity": 0.62, "stroke": "#cffff2", "strokeOpacity": 1.0},
}
FIGURE_07_STROKE_WIDTH = 2

FIGURE_11_KIND = "xy-usa-periods"
FIGURE_11_PERIODS = [
    {
        "id": "usa-early",
        "label": "USA (1850-1930)",
        "shortLabel": "US1",
        "color": "#ff8b67",
        "linePattern": "solid",
        "endLabelDx": 18,
        "endLabelDy": -10,
        "yearsLabel": "1850-1930",
    },
    {
        "id": "usa-late",
        "label": "USA (1930-2020)",
        "shortLabel": "US2",
        "color": "#8ac6ff",
        "linePattern": "solid",
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
        "linePattern": "solid",
        "endLabelDx": 18,
        "endLabelDy": -14,
        "yearsLabel": "1850-1930",
    },
    {
        "id": "usa-late",
        "label": "USA (1930-2020)",
        "shortLabel": "US2",
        "color": "#8ac6ff",
        "linePattern": "solid",
        "endLabelDx": 18,
        "endLabelDy": -4,
        "yearsLabel": "1930-2020",
    },
    {
        "id": "korea-early",
        "label": "South Korea (1975-2000)",
        "shortLabel": "KR1",
        "color": "#ff8b67",
        "linePattern": "dotted",
        "endLabelDx": 18,
        "endLabelDy": 10,
        "yearsLabel": "1975-2000",
    },
    {
        "id": "korea-late",
        "label": "South Korea (2000-2025)",
        "shortLabel": "KR2",
        "color": "#8ac6ff",
        "linePattern": "dotted",
        "endLabelDx": 18,
        "endLabelDy": 12,
        "yearsLabel": "2000-2025",
    },
]

FIGURE_13_KIND = "xy-scenarios"
FIGURE_13_X_AXIS_LABEL = "Year"
FIGURE_13_Y_AXIS_LABEL = "World population in 1M+ cities"
FIGURE_13_X_TICKS = [1975, 2000, 2025, 2050, 2075, 2100]
FIGURE_13_Y_DOMAIN = [0, 5]
FIGURE_13_Y_TICKS = [0, 1, 2, 3, 4, 5]
FIGURE_13_SPLICE_YEAR = 2025
FIGURE_13_GRAPH_MARGINS = {"right": 88}
FIGURE_13_SCENARIOS = [
    {
        "id": "runaway",
        "label": "Runaway",
        "shortLabel": "RW",
        "color": "#ff8b67",
        "tableName": WORLD_TOT_POP_SHARE_CITIES_ABOVE_1M_INC_RETURNS_TABLE,
        "sourceKey": "runaway",
        "endLabelDx": 18,
        "endLabelDy": -16,
    },
    {
        "id": "extrapolation",
        "label": "Extrapolation",
        "shortLabel": "EX",
        "color": "#f1c56d",
        "tableName": WORLD_TOT_POP_SHARE_CITIES_ABOVE_1M_EXTR_TABLE,
        "sourceKey": "extrapolation",
        "endLabelDx": 18,
        "endLabelDy": -4,
    },
    {
        "id": "lifecycle",
        "label": "Lifecycle",
        "shortLabel": "LC",
        "color": "#67e0cc",
        "tableName": WORLD_TOT_POP_SHARE_CITIES_ABOVE_1M_TABLE,
        "sourceKey": "lifecycle",
        "endLabelDx": 18,
        "endLabelDy": 8,
    },
    {
        "id": "proportional",
        "label": "Proportional",
        "shortLabel": "PO",
        "color": "#8ac6ff",
        "tableName": WORLD_TOT_POP_SHARE_CITIES_ABOVE_1M_PROP_GROWTH_TABLE,
        "sourceKey": "proportional",
        "endLabelDx": 18,
        "endLabelDy": 18,
    },
]
