<script lang="ts">
  import { onMount } from "svelte";
  import DotComparisonCanvas from "$lib/components/dot-comparison/DotComparisonCanvas.svelte";
  import type { DotComparisonScene } from "$lib/components/dot-comparison/types";
  import FutureDistributionCanvas from "$lib/components/future-distribution/FutureDistributionCanvas.svelte";
  import type { FutureDistributionScene } from "$lib/components/future-distribution/types";
  import LayeredMapCanvas from "$lib/components/layered-map/LayeredMapCanvas.svelte";
  import type { LayeredMapScene } from "$lib/components/layered-map/types";
  import CitedParagraph from "$lib/components/CitedParagraph.svelte";
  import PlaceholderCanvas from "$lib/components/PlaceholderCanvas.svelte";
  import ProseSection from "$lib/components/ProseSection.svelte";
  import StickyScene from "$lib/components/StickyScene.svelte";
  import XYGraphCanvas from "$lib/components/xy-graph/XYGraphCanvas.svelte";
  import type { XYGraph, XYLinePattern } from "$lib/components/xy-graph/types";
  import type { PageData } from "./$types";

  type SceneKind =
    | "dot-comparison"
    | "future-distribution"
    | "xy-world"
    | "xy-regions"
    | "xy-usa-periods"
    | "xy-usa-korea-periods"
    | "xy-scenarios"
    | "map-paris"
    | "map-prd"
    | "map-ghsl"
    | "map-allocation"
    | "placeholder";

  type LegendItem = {
    label: string;
    color: string;
    shape?: "line" | "fill" | "outline";
    linePattern?: XYLinePattern;
  };

  type GeneratedLegend = {
    id: string;
    label: string;
    color: string;
    linePattern?: XYLinePattern;
  };

  type GeneratedXYFigure = {
    id: string;
    kind: SceneKind;
    graph: XYGraph;
    legend?: GeneratedLegend[];
  };

  type GeneratedLayeredMapStep = {
    id: string;
    visibleLayerIds: string[];
  };

  type GeneratedLayeredMapFigure = {
    id: string;
    kind: "layered-map-paris" | "layered-map-prd";
    map: LayeredMapScene;
    scenes: GeneratedLayeredMapStep[];
  };

  type GeneratedFutureDistributionScene = Omit<FutureDistributionScene, "maxFutureByBin"> & {
    id: string;
    title: string;
  };

  type GeneratedFutureDistributionFigure = {
    id: string;
    kind: "future-distribution";
    meta: {
      brick: {
        maxFutureByBin: number[];
      };
    };
    scenes: GeneratedFutureDistributionScene[];
  };

  type GeneratedFigures = {
    figure02: GeneratedFutureDistributionFigure;
    figure03: GeneratedLayeredMapFigure;
    figure07: GeneratedLayeredMapFigure;
    figure08: GeneratedXYFigure;
    figure09: GeneratedXYFigure;
    figure11: GeneratedXYFigure;
    figure12: GeneratedXYFigure;
    figure13: GeneratedXYFigure;
  };

  type CitationRef = {
    ref: number;
  };

  type ParagraphToken = string | CitationRef;
  type CitedParagraphValue = string | ParagraphToken[];

  export let data: PageData;

  $: generatedFigures = data.generatedFigures as GeneratedFigures;

  let articleProgress = 0;

  function updateArticleProgress() {
    if (typeof window === "undefined") {
      return;
    }

    const scrollTop = window.scrollY || document.documentElement.scrollTop || 0;
    const scrollableHeight = document.documentElement.scrollHeight - window.innerHeight;

    articleProgress =
      scrollableHeight <= 0 ? 0 : Math.min(Math.max(scrollTop / scrollableHeight, 0), 1);
  }

  onMount(() => {
    updateArticleProgress();
  });

  const cite = (ref: number): CitationRef => ({ ref });

  const introParagraphs: CitedParagraphValue[] = [
    "Take two cities. One has 100,000 people. The other has 10 million. The large one is not just an inflated version of the small ones. It's different. Its people are different. They produce more: they earn 74% higher salaries. They connect more: their social networks are three times as dense. They innovate more: they are 3.5 times more likely to produce a patent.",
    "That 3.5 times more patents figure is the average. But for frontier fields, the multiplier is actually much bigger. For example, people in large cities are 14 times more likely to produce patents in computer hardware and software, and 40 times more likely to publish a paper in neuroscience.",
    [
      "The general idea is that of nonlinear scaling laws.",
      cite(6),
      cite(9),
      " As cities get bigger, outcomes do not just increase: they change qualitatively. The upsides grow: people become more innovative, more productive, more connected. But the downsides grow too. People in big cities are 5 times more likely to be robbed. They are 8 times more likely to contract syphilis. They spend 4 times longer in traffic. Cities amplify everything: the good and the bad alike."
    ],
    "So, whether we all end up living in megacities is not just a curiosity. It is an important determinant of how much wealth we can produce, where our technological frontier sits, and how heavily we draw on the planet's resources."
  ];

  const proseSections: Array<{ heading?: string; paragraphs: CitedParagraphValue[] }> = [
    {
      paragraphs: [
        "Cities are growing fast. Every two months, the global urban population grows by 20 million people. That is one New York City worth of people. Every two months.",
        "It was not always like this. In the 1800s, urbanization was a thing of few countries. England industrialized and urbanized first. The rest of Western Europe and the US followed. Then Latin America. Then everyone else. Today, most countries are either already urban or rapidly urbanizing. Well over half of humanity lives in cities. And in the next 75 years, cities are projected to add about 2.4 billion residents.",
        "Where will these people go? Small towns or sprawling megacities? Three scenarios are possible.",
        [
          "In the first, new urban residents spread across large and small cities alike, and the overall shape of the urban system stays roughly intact. That means a majority of the population (i.e., above 50%) will continue to live in cities with fewer than 1 million people.",
          cite(10)
        ],
        "In the second scenario, the biggest cities absorb a disproportionate share of growth. People move to these urban behemoths. They grow faster than the rest and gobble up an every increasing share of the population. If today less than two billion people live in 1M+ cities, in 2100 it could be four billion or even more. Eventually, a handful of massive cities could dominate the world population.",
        "In a third, growth leans toward smaller cities, producing a more distributed urban future. The small cities get more of the pie. They grow faster than the big ones. Their over 50% share today becomes larger over time. And although they might grow larger, the population remains distributed across many places instead of piling up in a handful of winners."
      ]
    },
    {
      paragraphs: [
        "So, which of these futures is more likely? The world is urbanizing fast, but which cities are absorbing that growth?",
        "Answering this question is hard. And the reason might not be what you expect. It wasn't what I expected. We use the word 'city' as if everyone agrees on what it means. But the more I ponder the question \"what is a city\" the more it becomes hard to answer. Its one of those abstractions that sweep all the complexity under the rug. But lift the rug, and it's a total mess",
        "Take, for example, Paris. If you ask the French government what is Paris they might point you to the legal borders of the city. This is an area of just 105.4 square kilometers with about 2 million residents. Pull up a satellite image of Paris and a it tells a different story. The built-up area has spilled way beyond the border of the historical core, and much of the banlieue is physically continuous with it: one built mass, no gap. The legal border starts to look like a fossil of historical accident.",
        "And it doesn't stop there. Consider not just the physical city, but the attraction area: the area from which people flow into Paris for work, shopping, family, connected by invisible ties. That area covers most of northern France. It stretches across 18,940.7 square kilometers and holds 13.24 million people. You see the problem: What is Paris? The legal borders? The physical city? The attraction area? This question is hard to answer for Paris. But to understand where the world population is headed, we have to answer it for every single city on the planet!"
      ]
    },
    {
      paragraphs: [
        "For most of history, answering this question was impossible. Not hard. Impossible. You would need every statistical agency on the planet to agree on what a city is, and then maintain that agreement across time. Good luck with that.",
        "Then satellites started quietly building a memory of the planet. Landsat has been observing the Earth since the 1970s. Sentinel-2 added much sharper optical imagery in the 2010s. Today, the planet is photographed continuously by dozens of satellites. This imagery made it possible to skip all the agreement. It created a picture of the Earth that is comparable across all places and, at the right resolution, across all times.",
        [
          "The basic idea is simple. You start from the pictures. You break them into small cells. For each cell, you estimate how much of it is physically built up: the material footprint of settlement: roofs, roads, blocks, industrial surfaces. With this data you can trace the boundaries of physical cities. The result is a grid of 1km x 1km cells covering the whole planet, and for each one it's fairly easy to say: urban or not. This is the work of the GHSL (Global Human Settlement Layer), a European initiative.",
          cite(2)
        ],
        "In my work, I use these grids to construct cities. First, I identify which cells count as urban. Then, I connect neighboring urban cells into clusters. Each cluster is a city. This definition is far from perfect. For instance, it fails to capture the gravity a big city exerts on its nearby towns. But it is easy to define and easy to compare across the whole planet. That makes it the only viable candidate for a global analysis."
      ]
    },
    {
      paragraphs: [
        "Next, I need to assign each city a population. After all, we are interested in population growth. Doing that requires quite a bit of extra effort. You start again by tiling the world into 1km by 1km cells. You then estimate the physical volume of buildings in each cell through a series of complex calculations that I will kindly spare you from.",
        "Alongside the building volumes, you collect census totals reported for administrative areas. These are small subdivisions that tile the whole world. Their size varies by country, which makes them hard to compare. You redistribute the populations of these areas across grid cells, proportional to each cell's built volume. Where there is more volume, more people are assigned. Tada: with this simple trick you now have a pretty educated guess of how many people live in each 1km by 1km cell on the planet. Again, shoutout to GHSL for this amazing work.",
        "I then overlay my city boundaries and sum up population counts inside them. This yields the population of each city. I then repeat this across years to get a time series of city growth (the actual thing I do is slightly more advanced, can you guess what's the problem with the above approach?)"
      ]
    },
    {
      paragraphs: [
        [
          "Using the above procedure, I build one of the most comprehensive city-population datasets in existence. It covers 50 years (1975-2025), 99 countries, about 94% of the world's population, with 1,604,593 city-year observations.",
          cite(1)
        ],
        "The data shows the rise of massive giants. Nowhere is this more visible than in the Pearl River Delta. In 1975 the Pearl River Delta: home of Shenzhen, Hong Kong, and Guangzhou: was a largely rural Chinese region. Then Deng Xiaoping set up special economic zones in the area, and the region boomed. But when I say boomed, I mean it exploded. In less than 50 years, a bunch of medium-sized urban agglomerations thickened, merged, and started behaving like one enormous urban machine. Today, over 64 million people live in this delta. Innovation runs at a breakneck pace. Firms are at the cutting edge of robotics and automation: DJI, BYD, and a growing roster of companies pushing the frontier of what machines can do. I think this delta is on track to overtake Silicon Valley as the world's leading technology hub in the 21st century."
      ]
    },
    {
      paragraphs: [
        "But is the Pearl River Delta the exception or the rule? Across the global data, larger cities often appear to outpace smaller ones. Plot city size on the horizontal axis and decade growth on the vertical axis, and the curve slopes upward. 10M people cities grew almost 10% faster than 100K people cities.",
        "It is important to notice that this logic is self-reinforcing. If larger cities grow faster, they become larger, which leads them to grow even faster, which makes them larger still. A small lead turns into a large lead. Follow that logic far enough and the future starts to look like a world increasingly dominated by giant cities."
      ]
    },
    {
      paragraphs: [
        "Yet, when you split the data, a different pattern appears. In Asia and Africa, the largest cities still post very high decade growth rates. In Europe the curve is much flatter, and in the Americas it can even bend negative at the top end.",
        "At first, that looks like a geographic divide: perhaps Asia and Africa are giant-city regions, while Europe and the Americas are not. But there is another possibility: timing matters. What looks like a map of regional difference is, to a large extent, a map of countries sitting at different stages of the same process.",
        "One way to test this is to order countries by their level of urbanization on the x-axis, and on the y-axis plot how much faster their large cities grow relative to the rest. When we do this, we see a clean downward-sloping relationship. The more urbanized a country, the less its large cities outgrow the rest."
      ]
    },
    {
      paragraphs: [
        "This gives us a hypothesis. Maybe whether large cities outgrow small ones is not universal. Maybe it depends on where a country sits in the urbanization process. The later the stage, the less the giants pull ahead. This is consistent with the cross-sectional evidence. But a snapshot is not enough to prove it. We need to watch the same countries over time.",
        [
          "The United States provides one of the few longitudinal records long enough to capture this. Long before satellites, long before digital maps, long before any of the tools I described earlier, the United States was already collecting census material rich enough to reconstruct a map of urban development. Census officers went around the country, counted people in their homes, every ten years. These handwritten documents were passed down in libraries through generations, until recently a massive effort transformed those old records into machine-readable format: linked across years, matched to places. The result is IPUMS Full Count, which now makes available over 800 million individual-level census records for 1850-1950.",
          cite(3),
          cite(5)
        ],
        [
          "I took those records, supplemented them with modern NHGIS place estimates, and reconstructed cities from 1850 to today. First I built population grids, then aggregated them into clusters using the same method as before. Surprisingly, this incredible long-run dataset shows exactly the pattern the global data hint at. Early on, large U.S. cities had a strong growth advantage. Over time, that advantage weakened dramatically, until today it's roughly flat.",
          cite(4)
        ]
      ]
    },
    {
      paragraphs: [
        "Another case lets us dig deeper: South Korea's economic miracle. Korea's postwar transformation was not merely fast. It was historically extreme. From 1965 to 1995, annual real income growth averaged over 8%. Urbanization rose from 28% in 1960 to 79% by 1996. GDP per person climbed from about $158 to above $31,000. That is development in fast-forward. And it means our 1975-2025 dataset captures much of Korea's transformation in real time. No other country in the data offers anything comparable.",
        [
          "And the result is striking. Korea traces the same arc in just a few decades. Early on, Seoul and the largest Korean cities pull away hard. Later, the advantage fades. Put differently, we continue to see evidence of an urban lifecycle: big cities take the lead early but then lose their growth premium later.",
          cite(8)
        ]
      ]
    },
    {
      paragraphs: [
        [
          "Why would that be? The causes are likely many. Here is my take. Early in development, distance is expensive, markets are thin, and much of the economy is still tied tightly to land. Then transport improves. Manufacturing scales. Rail, ports, power, finance, universities, and state capacity reward concentration. Once one place gets ahead, the feedback loops start. Firms want access to customers. Workers go where the jobs are. Suppliers follow firms. Infrastructure follows everyone. A city that got a little ahead can suddenly get far ahead. The arrival of modern technology opens vast new opportunities, and large cities are the first to seize them.",
          cite(7)
        ],
        "Then the system starts hitting its limits. The rural reservoir shrinks. Transport and infrastructure spread outward. Secondary cities become capable of supporting their own deep labor markets. Land and housing costs bite harder in the biggest cores. Some growth spills into suburbs and satellites. All these forces conspire to slow the giants down.",
        "So where does this leave us by 2100? Today, about 1.9 billion people live in cities of a million or more. If current 1975-2025 size-growth patterns were simply extended forward, that number would reach about 3.9 billion by 2100. The self-reinforcing logic could push it even higher, to 4.3 billion. But the lifecycle model suggests something lower: around 3.4 billion. That is about 410 million fewer people in million-plus cities than the straight extrapolation, and 890 million fewer than the runaway scenario."
      ]
    },
    {
      paragraphs: [
        "That is not a bookkeeping difference. The same scaling logic applies. Those hundreds of millions of people who will not move to large cities will generate less wealth and less invention, but also less disease, less crime, and less pressure on infrastructure. The difference will show up everywhere, from global economic growth to the speed at which pandemics spread.",
        "So, are we all going to live in giant cities?",
        "Probably not. At least not in the runaway sense that a first look at global city growth would suggest. But the giants forged in the early phases of urbanization will remain, amplifying wealth, invention, ambition, inequality, and climate risk for the rest of the century."
      ]
    }
  ];

  const references = [
    {
      id: 1,
      label: "Paper",
      citation:
        "Musso, A., Rybski, D., Helbing, D., Neffke, F.: Large cities lose their growth advantage as countries urbanize. arXiv:2510.12417v3 (2026).",
      href: "https://doi.org/10.48550/arXiv.2510.12417"
    },
    {
      id: 2,
      label: "Global Human Settlement Layer",
      citation:
        "Schiavina, M., Melchiorri, M., Pesaresi, M., Politis, P., Carneiro Freire, S.M., Maffenini, L., Florio, P., Ehrlich, D., Goch, K., Carioli, A., Uhl, J., Tommasi, P., Kemper, T.: GHSL Data Package 2023. Publications Office of the European Union, Luxembourg (2023).",
      href: "https://doi.org/10.2760/098587"
    },
    {
      id: 3,
      label: "IPUMS full count",
      citation:
        "Ruggles, S., Nelson, M.A., Sobek, M., Fitch, C.A., Goeken, R., Hacker, J.D., Roberts, E., Warren, J.R.: IPUMS ancestry full count data: Version 4.0 (2024).",
      href: "https://doi.org/10.18128/D014.V4.0"
    },
    {
      id: 4,
      label: "IPUMS NHGIS",
      citation:
        "Manson, S., Schroeder, J., Riper, D.V., Knowles, K., Kugler, T., Roberts, F., Ruggles, S.: IPUMS National Historical Geographic Information System: Version 19.0. IPUMS, Minneapolis, MN (2024).",
      href: "https://doi.org/10.18128/D050.V19.0"
    },
    {
      id: 5,
      label: "Census Place Project",
      citation:
        "Berkes, E., Karger, E., Nencka, P.: The census place project: A method for geolocating unstructured place names. Explorations in Economic History 87, 101477 (2023).",
      href: "https://doi.org/10.1016/j.eeh.2022.101477"
    },
    {
      id: 6,
      label: "Urban scaling",
      citation:
        "Bettencourt, L.M.A., Lobo, J., Helbing, D., Kuhnert, C., West, G.B.: Growth, innovation, scaling, and the pace of life in cities. Proceedings of the National Academy of Sciences 104(17), 7301-7306 (2007).",
      href: "https://doi.org/10.1073/pnas.0610172104"
    },
    {
      id: 7,
      label: "Increasing returns",
      citation:
        "Krugman, P.: Increasing Returns and Economic Geography. Journal of Political Economy 99(3), 483-499 (1991).",
      href: "https://doi.org/10.1086/261763"
    },
    {
      id: 8,
      label: "Urban systems",
      citation:
        "Pumain, D., Paulus, F., Vacchiani-Marcuzzo, C., Lobo, J.: An evolutionary theory for interpreting urban scaling laws. Cybergeo: European Journal of Geography (2006).",
      href: "https://doi.org/10.4000/cybergeo.2519"
    },
    {
      id: 9,
      label: "Urban scaling overview",
      citation:
        "Rybski, D., Arcaute, E., Batty, M.: Urban scaling laws. Environment and Planning B: Urban Analytics and City Science 46(9), 1605-1610 (2019).",
      href: "https://doi.org/10.1177/2399808319886125"
    },
    {
      id: 10,
      label: "City-size distributions",
      citation:
        "Gabaix, X.: Zipf's Law for Cities: An Explanation. The Quarterly Journal of Economics 114(3), 739-767 (1999).",
      href: "https://doi.org/10.1162/003355399556133"
    }
  ];
  const introScrollHint = "The data and story unfold as you scroll down.";

  const stickyScenes: Array<{
    id: string;
    kind: SceneKind;
    ariaLabel: string;
    pinDurationVh: number;
    tailHoldVh?: number;
    stepHeightMultipliers?: number[];
    placeholderLabel?: string;
    placeholderNote?: string;
    steps: Array<{
      id: string;
      kicker: string;
      title: string;
      body: string;
      accentColor?: string;
    }>;
  }> = [
    {
      id: "figure-01",
      kind: "dot-comparison",
      ariaLabel: "Figure 1",
      pinDurationVh: 360,
      tailHoldVh: 96,
      stepHeightMultipliers: [1.5, 1, 1, 1, 1],
      steps: [
        { id: "dot-a", kicker: "City comparison", title: "Same people, different urban machine", body: "A city with 10 million residents is not just a scaled-up small town. It changes the outcomes for the people inside it.", accentColor: "#67e0cc" },
        { id: "dot-b", kicker: "Output", title: "Bigger cities raise the baseline", body: "Dense cities make it easier for skills, firms, and opportunities to find each other. That pushes output per person upward.", accentColor: "#8ac6ff" },
        { id: "dot-c", kicker: "Innovation", title: "Ideas scale even faster", body: "The inventive payoff is steeper than the economic one. Big cities do not just host more ideas; they help ideas meet.", accentColor: "#67e0cc" },
        { id: "dot-d", kicker: "Crime", title: "Scale amplifies the downsides too", body: "The same closeness that makes big cities productive also makes them dangerous. People are five times more likely to be robbed.", accentColor: "#ff8d6b" },
        { id: "dot-e", kicker: "Disease", title: "Proximity has a biological cost", body: "Dense networks do not just transmit ideas. They transmit pathogens, making the contraction of diseases much more likely.", accentColor: "#f2c56f" }
      ]
    },
    {
      id: "figure-02",
      kind: "future-distribution",
      ariaLabel: "Figure 2",
      pinDurationVh: 340,
      tailHoldVh: 96,
      steps: [
        { id: "future-a", kicker: "Urbanization futures", title: "The world already leans big", body: "Start with the current distribution. Large metros already hold a huge share of urban life (circa 40%), but today's shape does not tell you tomorrow's.", accentColor: "#2d3844" },
        { id: "future-b", kicker: "Urbanization futures", title: "Balanced growth keeps the shape", body: "If every size class absorbs newcomers in roughly today's proportions, the whole distribution gets taller without changing much.", accentColor: "#67e0cc" },
        { id: "future-c", kicker: "Urbanization futures", title: "A megacity future bends right", body: "If the largest metros outgrow the rest, the right-hand side swells fast and urban growth becomes more concentrated.", accentColor: "#ff8b67" },
        { id: "future-d", kicker: "Urbanization futures", title: "A distributed future bends left", body: "If smaller and mid-sized places absorb more of the next wave, the world still urbanizes, just less through runaway concentration.", accentColor: "#f0c66f" }
      ]
    },
    {
      id: "figure-03",
      kind: "map-paris",
      ariaLabel: "Figure 3",
      pinDurationVh: 360,
      steps: [
        { id: "paris-a", kicker: "Boundary problem", title: "Hold the map still", body: "Nothing on the ground changes from one step to the next. Only the definition does." },
        { id: "paris-b", kicker: "Administrative city", title: "The legal city is the narrowest city", body: "Paris proper is a compact official core. It is real, but it is only one way to draw the city." },
        { id: "paris-c", kicker: "Built city", title: "The city people actually recognize is larger", body: "Once you follow the built-up area, Paris spills well beyond its legal edge." },
        { id: "paris-d", kicker: "Attraction area", title: "The functional city is larger again", body: "Commutes, labour markets, and daily ties pull the city far past the visible core." },
        { id: "paris-e", kicker: "Measurement problem", title: "The border is doing the work", body: "Same landscape, different boundary, different answer. That is exactly why city measurement is hard." }
      ]
    },
    {
      id: "figure-04",
      kind: "map-ghsl",
      ariaLabel: "Figure 4",
      pinDurationVh: 420,
      tailHoldVh: 132,
      steps: [
        { id: "ghsl-a", kicker: "Input surface", title: "Satellites do not see city names", body: "They see roofs, roads, blocks, empty land, and everything in between. The raw input is physical surface." },
        { id: "ghsl-b", kicker: "Built-up signal", title: "Every cell gets an urban score", body: "Some cells are barely settled. Others are intensely built. The grid turns a landscape into a comparable surface." },
        { id: "ghsl-c", kicker: "Urban cutoff", title: "A threshold creates an urban footprint", body: "At some point a place stops reading as scattered settlement and starts reading as urban." },
        { id: "ghsl-d", kicker: "City clustering", title: "Adjacency turns footprint into cities", body: "Once neighbouring urban cells are connected, city boundaries emerge from the pattern itself." }
      ]
    },
    {
      id: "figure-05",
      kind: "map-allocation",
      ariaLabel: "Figure 5",
      pinDurationVh: 360,
      tailHoldVh: 112,
      steps: [
        { id: "alloc-a", kicker: "Residential signal", title: "To count people, look for residential mass", body: "Built volume is a better clue than raw land area. A dense cell full of housing is not the same as a low-rise fringe." },
        { id: "alloc-b", kicker: "Population weights", title: "Volume becomes weight", body: "The more residential mass a cell contains, the larger the share of population it is likely to receive." },
        { id: "alloc-c", kicker: "Census anchor", title: "Administrative counts keep the map honest", body: "Census totals fix how many people must be allocated. The spatial surface decides where within those areas they most likely live." }
      ]
    },
    {
      id: "figure-07",
      kind: "map-prd",
      ariaLabel: "Figure 7",
      pinDurationVh: 380,
      steps: [
        { id: "prd-a", kicker: "Pearl River Delta", title: "1975: a constellation, not yet a corridor", body: "The delta is urban, but in fragments. The major centres still read as separate places.", accentColor: "#7a8794" },
        { id: "prd-b", kicker: "Pearl River Delta", title: "1985: the gaps start closing", body: "Urban land spreads outward, but the system is still mostly a set of distinct clusters.", accentColor: "#93a2b2" },
        { id: "prd-c", kicker: "Pearl River Delta", title: "1995: growth thickens the field", body: "By the mid-1990s the delta is no longer a loose scatter. Expansion begins to fill the spaces between the major centres.", accentColor: "#b2c0cf" },
        { id: "prd-d", kicker: "Pearl River Delta", title: "2005: separate cities start behaving like one region", body: "The largest clusters are now pushing into each other. Distance within the delta is becoming less decisive.", accentColor: "#7ed7cb" },
        { id: "prd-e", kicker: "Pearl River Delta", title: "2015: continuity becomes the new fact", body: "What used to be separated by open land increasingly reads as one continuous urban fabric.", accentColor: "#8cf0de" },
        { id: "prd-f", kicker: "Pearl River Delta", title: "2025: the winner is the region", body: "By 2025 the Pearl River Delta feels less like a handful of cities and more like a mega-region built from their fusion.", accentColor: "#67e0cc" }
      ]
    },
    {
      id: "figure-08",
      kind: "xy-world",
      ariaLabel: "Figure 8",
      pinDurationVh: 300,
      steps: [
        { id: "step-1", kicker: "Global pattern", title: "Read the curve from left to right", body: "Small cities sit on the left, giant ones on the right. The whole question is whether the line rises with size." },
        { id: "step-2", kicker: "Global pattern", title: "Globally, it does", body: "Across the full sample, larger cities tend to post higher decade growth rates." },
        { id: "step-3", kicker: "Global pattern", title: "That is the runaway logic", body: "If size is associated with faster growth, today's large cities become tomorrow's giants, and the giants keep compounding." }
      ]
    },
    {
      id: "figure-09",
      kind: "xy-regions",
      ariaLabel: "Figure 9",
      pinDurationVh: 320,
      steps: [
        { id: "p9-a", kicker: "Regional split", title: "In Asia, scale still pays clearly", body: "The line rises with size. Larger cities still enjoy a visible growth premium.", accentColor: "#ff8b67" },
        { id: "p9-b", kicker: "Regional split", title: "Africa points the same way", body: "The direction is similar: large cities also post high decade growth rates.", accentColor: "#f1c56d" },
        { id: "p9-c", kicker: "Regional split", title: "Europe is much flatter", body: "Big cities still matter, but the extra growth associated with size is much weaker.", accentColor: "#8ac6ff" },
        { id: "p9-d", kicker: "Regional split", title: "The Americas can even bend back down", body: "At the top end, some very large cities no longer outgrow the rest. Size stops being an automatic advantage.", accentColor: "#b6dc7c" }
      ]
    },
    {
      id: "figure-11",
      kind: "xy-usa-periods",
      ariaLabel: "Figure 11",
      pinDurationVh: 260,
      steps: [
        { id: "p11-a", kicker: "U.S. lifecycle", title: "Early urban America favored the biggest cities", body: "In the nineteenth and early twentieth centuries, the size-growth curve rises strongly with city size.", accentColor: "#ff8b67" },
        { id: "p11-b", kicker: "U.S. lifecycle", title: "Later urban America looks flatter", body: "Once the system matures, the extra growth associated with size becomes much weaker.", accentColor: "#8ac6ff" }
      ]
    },
    {
      id: "figure-12",
      kind: "xy-usa-korea-periods",
      ariaLabel: "Figure 12",
      pinDurationVh: 260,
      steps: [
        { id: "p12-a", kicker: "South Korea", title: "Early on, the giants surge", body: "In the first phase, the largest Korean cities enjoy a strong growth premium.", accentColor: "#ff8b67" },
        { id: "p12-b", kicker: "South Korea", title: "Then maturity arrives fast", body: "In just a few decades, Korea shifts toward the flatter later-stage pattern that took much longer in the United States.", accentColor: "#8ac6ff" }
      ]
    },
    {
      id: "figure-13",
      kind: "xy-scenarios",
      ariaLabel: "Figure 13",
      pinDurationVh: 320,
      steps: [
        { id: "step-a", kicker: "Competing futures", title: "All four lines share the same history", body: "Up to the present, every scenario starts from the same observed rise in million-plus cities.", accentColor: "#cfd6dd" },
        { id: "step-b", kicker: "Competing futures", title: "Runaway is the upper bound", body: "If the big-city premium never fades, concentration keeps climbing hard.", accentColor: "#ff8b67" },
        { id: "step-c", kicker: "Competing futures", title: "Simple extrapolation is not neutral", body: "Just extending today's pattern forward still produces a sharply more concentrated world.", accentColor: "#f1c56d" },
        { id: "step-d", kicker: "Competing futures", title: "Lifecycle is the middle path", body: "The most plausible future is neither flat nor runaway: giants keep growing, but their edge gradually weakens.", accentColor: "#67e0cc" }
      ]
    }
  ];

  const dotComparisonMetrics = {
    gdp: {
      title: "GDP",
      verb: "earns",
      delta: "24%",
      tail: "more",
      color: "#8ac6ff",
      smallActive: [6, 8, 15, 17, 24, 26, 33, 35, 42, 44, 51, 53, 60, 62, 69, 71],
      largeActive: Array.from({ length: 240 }, (_, index) => index),
      smallFade: 0.1,
      largeFade: 0.08,
      glow: 0.24,
      warning: 0,
      co2: 0
    },
    patents: {
      title: "Patents",
      verb: "produces",
      delta: "109%",
      tail: "more patents",
      color: "#67e0cc",
      smallActive: [2, 6, 13, 20, 28, 35, 44, 51, 63],
      largeActive: Array.from({ length: 160 }, (_, index) => index),
      smallFade: 0.08,
      largeFade: 0.07,
      glow: 0.2,
      warning: 0,
      co2: 0
    },
    housing: {
      title: "Housing",
      verb: "pays",
      delta: "41%",
      tail: "more for housing",
      color: "#ff8d6b",
      smallActive: [0, 1, 8, 9, 17, 18, 26, 27, 35, 36, 44, 45, 53, 54, 62, 63, 70, 71],
      largeFilter: {
        mode: "outer-ring",
        minDist: 0.72
      },
      smallFade: 0.12,
      largeFade: 0.1,
      glow: 0.08,
      warning: 0.22,
      co2: 0
    },
    co2: {
      title: "CO2",
      verb: "consumes",
      delta: "32%",
      tail: "more CO2",
      color: "#f2c56f",
      smallActive: [0, 3, 8, 12, 17, 21, 26, 30, 35, 39, 44, 48, 53, 57, 62, 66, 69, 71],
      largeActive: Array.from({ length: 560 }, (_, index) => index).filter((index) => index % 2 === 0),
      smallFade: 0.12,
      largeFade: 0.1,
      glow: 0.12,
      warning: 0.08,
      co2: 0.14
    }
  } satisfies Record<string, DotComparisonScene["metric"] & NonNullable<DotComparisonScene["metric"]>>;

  function svgDataUri(svg: string) {
    return `data:image/svg+xml;charset=UTF-8,${encodeURIComponent(svg)}`;
  }

  const ghslBaseImage = svgDataUri(`
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
      <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#0b1014"/>
          <stop offset="100%" stop-color="#091016"/>
        </linearGradient>
        <filter id="blur" x="-10%" y="-10%" width="120%" height="120%">
          <feGaussianBlur stdDeviation="10"/>
        </filter>
      </defs>
      <rect width="800" height="600" fill="url(#bg)"/>
      <g opacity="0.9" filter="url(#blur)">
        <path d="M100 238 C212 186, 338 186, 460 218 S628 248, 704 226" fill="none" stroke="#e6dac1" stroke-width="22" stroke-linecap="round" opacity="0.18"/>
        <path d="M184 96 C240 170, 272 264, 296 386 S334 492, 358 560" fill="none" stroke="#e0d4be" stroke-width="18" stroke-linecap="round" opacity="0.16"/>
        <path d="M162 132 C186 164, 194 214, 182 260 C168 306, 166 344, 194 384 C230 438, 298 448, 326 488 C352 526, 344 572, 324 600" fill="none" stroke="#6ea7dc" stroke-width="18" stroke-linecap="round" opacity="0.2"/>
      </g>
      <g opacity="0.62">
        <path d="M472 126 C538 112, 596 148, 624 206 C596 236, 536 248, 486 234 C456 202, 452 152, 472 126 Z" fill="#22372a"/>
        <path d="M450 430 C524 398, 612 424, 644 490 C616 538, 536 558, 468 528 C438 494, 432 458, 450 430 Z" fill="#27392d"/>
        <path d="M114 432 C180 402, 256 424, 278 486 C248 534, 180 552, 130 522 C104 488, 98 454, 114 432 Z" fill="#26382c"/>
      </g>
    </svg>
  `);

  type SquareGrid = {
    x: number;
    y: number;
    size: number;
    cells: number;
    cellWidth: number;
    cellHeight: number;
  };

  function buildParisAlignedGrid(cells: number): SquareGrid {
    const [, , mapWidth, mapHeight] = generatedFigures.figure03.map.viewport.viewBox;
    const size = Math.min(mapWidth, mapHeight);
    const x = (mapWidth - size) / 2;
    const y = (mapHeight - size) / 2;

    return {
      x,
      y,
      size,
      cells,
      cellWidth: size / cells,
      cellHeight: size / cells
    };
  }

  type GhslCell = {
    row: number;
    col: number;
    value: number;
    urban: boolean;
    clusterId?: number;
    x: number;
    y: number;
    cx: number;
    cy: number;
  };

  function builtValue(col: number, row: number) {
    const x = col + 0.5;
    const y = row + 0.5;
    const centers = [
      { x: 6.2, y: 5.9, amp: 0.92, spread: 2.0 },
      { x: 10.7, y: 4.5, amp: 0.78, spread: 1.45 },
      { x: 3.7, y: 11.1, amp: 0.72, spread: 1.4 },
      { x: 11.8, y: 11.0, amp: 0.58, spread: 1.2 }
    ];

    const influence = (x1: number, y1: number, x2: number, y2: number, amp: number, width: number) => {
      const dx = x2 - x1;
      const dy = y2 - y1;
      const t = Math.min(
        1,
        Math.max(0, ((x - x1) * dx + (y - y1) * dy) / (dx * dx + dy * dy))
      );
      const px = x1 + dx * t;
      const py = y1 + dy * t;
      const dist = Math.hypot(x - px, y - py);
      return amp * Math.exp(-(dist * dist) / (2 * width * width));
    };

    let value = 0.04;

    centers.forEach((center) => {
      const dist2 = (x - center.x) ** 2 + (y - center.y) ** 2;
      value += center.amp * Math.exp(-dist2 / (2 * center.spread * center.spread));
    });

    value += influence(3.1, 2.8, 8.5, 8.1, 0.12, 0.75);
    value += influence(8.3, 9.1, 12.4, 12.5, 0.08, 0.72);
    value += (Math.sin(col * 1.6 + row * 0.7) + Math.cos(col * 0.8 - row * 1.2)) * 0.018;

    return Math.min(1, Math.max(0, value));
  }

  function buildGhslCells(grid: SquareGrid) {
    const { x, y, cells, cellWidth, cellHeight } = grid;
    const threshold = 0.52;
    const result: GhslCell[] = [];

    for (let row = 0; row < cells; row += 1) {
      for (let col = 0; col < cells; col += 1) {
        const value = builtValue(col, row);
        result.push({
          row,
          col,
          value,
          urban: value >= threshold,
          x: x + col * cellWidth,
          y: y + row * cellHeight,
          cx: x + col * cellWidth + cellWidth / 2,
          cy: y + row * cellHeight + cellHeight / 2
        });
      }
    }

    return { cells: result, threshold };
  }

  function clusterGhslCells(cells: GhslCell[], gridCount: number) {
    const palette = ["#7ab6a7", "#c8a264", "#c68678", "#8eaac3"];
    const grid = new Map(cells.map((cell) => [`${cell.row}-${cell.col}`, cell]));
    const visited = new Set<string>();
    const clusters: Array<{ id: number; color: string; label: string; cx: number; cy: number; members: GhslCell[] }> = [];

    cells.forEach((cell) => {
      const key = `${cell.row}-${cell.col}`;
      if (!cell.urban || visited.has(key)) {
        return;
      }

      const stack = [cell];
      const members: GhslCell[] = [];
      visited.add(key);

      while (stack.length > 0) {
        const current = stack.pop();

        if (!current) {
          continue;
        }

        members.push(current);

        [
          [current.row + 1, current.col],
          [current.row - 1, current.col],
          [current.row, current.col + 1],
          [current.row, current.col - 1]
        ].forEach(([row, col]) => {
          if (row < 0 || row >= gridCount || col < 0 || col >= gridCount) {
            return;
          }

          const neighborKey = `${row}-${col}`;
          const neighbor = grid.get(neighborKey);

          if (!neighbor || !neighbor.urban || visited.has(neighborKey)) {
            return;
          }

          visited.add(neighborKey);
          stack.push(neighbor);
        });
      }

      clusters.push({
        id: clusters.length,
        color: palette[clusters.length % palette.length],
        label: `C${String(clusters.length + 1).padStart(2, "0")}`,
        cx: members.reduce((sum, member) => sum + member.cx, 0) / members.length,
        cy: members.reduce((sum, member) => sum + member.cy, 0) / members.length,
        members
      });
    });

    clusters.sort((a, b) => b.members.length - a.members.length);

    clusters.forEach((cluster, index) => {
      cluster.id = index;
      cluster.color = palette[index % palette.length];
      cluster.label = `C${String(index + 1).padStart(2, "0")}`;
      cluster.members.forEach((member) => {
        member.clusterId = index;
      });
    });

    return clusters;
  }

  const allocationBaseImage = svgDataUri(`
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
      <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#0b1014"/>
          <stop offset="100%" stop-color="#091016"/>
        </linearGradient>
        <filter id="blur" x="-10%" y="-10%" width="120%" height="120%">
          <feGaussianBlur stdDeviation="8"/>
        </filter>
      </defs>
      <rect width="800" height="600" fill="url(#bg)"/>
      <g opacity="0.9" filter="url(#blur)">
        <path d="M118 274 C218 246, 320 260, 428 300 S608 336, 684 304" fill="none" stroke="#dfd5be" stroke-width="18" stroke-linecap="round" opacity="0.18"/>
        <path d="M198 126 C246 210, 278 302, 308 436 S362 532, 418 598" fill="none" stroke="#d9cfbc" stroke-width="14" stroke-linecap="round" opacity="0.16"/>
      </g>
      <g opacity="0.84">
        <path d="M522 156 C568 144, 624 176, 648 224 C622 252, 572 262, 526 248 C500 220, 500 178, 522 156 Z" fill="#384138"/>
        <path d="M468 458 C544 426, 632 454, 658 520 C626 574, 544 592, 480 566 C450 532, 444 488, 468 458 Z" fill="#364535"/>
      </g>
    </svg>
  `);

  type AllocationCell = {
    row: number;
    col: number;
    x: number;
    y: number;
    cx: number;
    cy: number;
    surface: number;
    volume: number;
    district: number;
    population: number;
  };

  function buildDistrictConfigs(grid: SquareGrid) {
    const allocationMidX = grid.x + grid.size / 2;
    const allocationMidY = grid.y + grid.size * 0.56;
    const allocationBottom = grid.y + grid.size;
    const allocationRight = grid.x + grid.size;

    return [
      {
        key: "A",
        color: "#7ab6a7",
        points: [
          [grid.x, grid.y],
          [allocationMidX, grid.y],
          [allocationMidX, allocationMidY],
          [grid.x, allocationBottom]
        ] as Array<[number, number]>,
        anchorX: grid.x + grid.size * 0.24,
        anchorY: grid.y + grid.size * 0.2,
        linkDirection: "down" as const
      },
      {
        key: "B",
        color: "#c8a264",
        points: [
          [allocationMidX, grid.y],
          [allocationRight, grid.y],
          [allocationRight, allocationBottom],
          [allocationMidX, allocationMidY]
        ] as Array<[number, number]>,
        anchorX: grid.x + grid.size * 0.76,
        anchorY: grid.y + grid.size * 0.2,
        linkDirection: "down" as const
      },
      {
        key: "C",
        color: "#c68678",
        points: [
          [grid.x, allocationBottom],
          [allocationMidX, allocationMidY],
          [allocationRight, allocationBottom]
        ] as Array<[number, number]>,
        anchorX: allocationMidX,
        anchorY: grid.y + grid.size * 0.84,
        linkDirection: "up" as const
      }
    ];
  }

  function pointsToPath(points: Array<[number, number]>) {
    return `M ${points.map((point) => `${point[0]} ${point[1]}`).join(" L ")} Z`;
  }

  function pointInPolygon(x: number, y: number, points: Array<[number, number]>) {
    let inside = false;

    for (let i = 0, j = points.length - 1; i < points.length; j = i, i += 1) {
      const xi = points[i][0];
      const yi = points[i][1];
      const xj = points[j][0];
      const yj = points[j][1];
      const intersects = yi > y !== yj > y && x < ((xj - xi) * (y - yi)) / (yj - yi) + xi;

      if (intersects) {
        inside = !inside;
      }
    }

    return inside;
  }

  function districtIndexForPoint(
    x: number,
    y: number,
    districtConfigs: ReturnType<typeof buildDistrictConfigs>
  ) {
    for (let index = 0; index < districtConfigs.length; index += 1) {
      if (pointInPolygon(x, y, districtConfigs[index].points)) {
        return index;
      }
    }

    return districtConfigs.length - 1;
  }

  function gauss(x: number, y: number, cx: number, cy: number, amp: number, spread: number) {
    const dist2 = (x - cx) ** 2 + (y - cy) ** 2;
    return amp * Math.exp(-dist2 / (2 * spread * spread));
  }

  function allocationSurface(col: number, row: number) {
    const x = col + 0.5;
    const y = row + 0.5;

    let value = 0.05;
    value += gauss(x, y, 4.4, 3.7, 0.82, 1.8);
    value += gauss(x, y, 8.1, 4.2, 0.72, 1.6);
    value += gauss(x, y, 3.2, 8.4, 0.56, 1.5);
    value += gauss(x, y, 8.6, 8.0, 0.6, 1.7);
    value += gauss(x, y, 6.6, 6.3, 0.22, 3.0);
    value += (Math.sin(col * 1.4 + row * 0.7) + Math.cos(col * 0.8 - row * 1.1)) * 0.03;

    return Math.min(1, Math.max(0, value));
  }

  function allocationVolume(col: number, row: number) {
    const x = col + 0.5;
    const y = row + 0.5;

    let value = allocationSurface(col, row) * 0.68;
    value += gauss(x, y, 4.4, 3.7, 0.32, 1.4);
    value += gauss(x, y, 8.2, 4.0, 0.26, 1.2);
    value += gauss(x, y, 3.1, 8.6, 0.28, 1.25);
    value -= gauss(x, y, 8.8, 8.0, 0.32, 1.3);
    value -= gauss(x, y, 10.3, 8.8, 0.12, 0.9);

    return Math.min(1, Math.max(0, value));
  }

  function mixTriplet(a: [number, number, number], b: [number, number, number], amount: number) {
    const t = Math.min(1, Math.max(0, amount));
    return a.map((value, index) => Math.round(value + (b[index] - value) * t)) as [number, number, number];
  }

  function rgb(values: [number, number, number]) {
    return `rgb(${values[0]}, ${values[1]}, ${values[2]})`;
  }

  function buildAllocationCells(
    grid: SquareGrid,
    districtConfigs: ReturnType<typeof buildDistrictConfigs>
  ) {
    const { x, y, cells, cellWidth, cellHeight } = grid;
    const result: AllocationCell[] = [];

    for (let row = 0; row < cells; row += 1) {
      for (let col = 0; col < cells; col += 1) {
        const cx = x + col * cellWidth + cellWidth / 2;
        const cy = y + row * cellHeight + cellHeight / 2;
        result.push({
          row,
          col,
          x: x + col * cellWidth,
          y: y + row * cellHeight,
          cx,
          cy,
          surface: allocationSurface(col, row),
          volume: allocationVolume(col, row),
          district: districtIndexForPoint(cx, cy, districtConfigs),
          population: 0
        });
      }
    }

    const totals = districtConfigs.map(() => ({ volume: 0, population: 0 }));
    result.forEach((cell) => {
      totals[cell.district].volume += cell.volume;
    });

    totals.forEach((district, index) => {
      district.population = Math.round((district.volume * 15000) / 1000) * 1000;
      result
        .filter((cell) => cell.district === index)
        .forEach((cell) => {
          const share = district.volume > 0 ? cell.volume / district.volume : 0;
          cell.population = district.population * share;
        });
    });

    return { cells: result, totals };
  }

  function isoBarPaths(x: number, y: number, width: number, height: number, lift: number) {
    const inset = Math.max(3, Math.min(width, height) * 0.08);
    const left = x + inset;
    const right = x + width - inset;
    const top = y + inset;
    const bottom = y + height - inset;
    const dx = Math.min(width, height) * 0.12;
    const effectiveLift = Math.max(8, lift);

    const front = `M ${left} ${bottom} L ${right} ${bottom} L ${right} ${bottom - effectiveLift} L ${left} ${bottom - effectiveLift} Z`;
    const side = `M ${right} ${bottom} L ${right + dx} ${bottom - dx} L ${right + dx} ${bottom - effectiveLift - dx} L ${right} ${bottom - effectiveLift} Z`;
    const roof = `M ${left} ${bottom - effectiveLift} L ${right} ${bottom - effectiveLift} L ${right + dx} ${bottom - effectiveLift - dx} L ${left + dx} ${bottom - effectiveLift - dx} Z`;

    return { front, side, roof };
  }

  function rangeProgress(progress: number, start: number, end: number) {
    if (progress <= start) {
      return 0;
    }

    if (progress >= end) {
      return 1;
    }

    return (progress - start) / (end - start);
  }

  function stepReveal(activeStepIndex: number, targetStep: number, stepProgress: number) {
    if (activeStepIndex < targetStep) {
      return 0;
    }

    if (activeStepIndex > targetStep) {
      return 1;
    }

    return stepProgress;
  }

  function cloneGraph(graph: XYGraph): XYGraph {
    return {
      xAxis: {
        ...graph.xAxis,
        ticks: graph.xAxis.ticks.map((tick) => ({ ...tick }))
      },
      yAxis: {
        ...graph.yAxis,
        ticks: graph.yAxis.ticks.map((tick) => ({ ...tick }))
      },
      lines: graph.lines.map((line) => ({
        ...line,
        endLabel: line.endLabel ? { ...line.endLabel } : undefined
      })),
      annotations: graph.annotations?.map((annotation) => ({
        ...annotation,
        point: { ...annotation.point }
      })),
      margins: graph.margins ? { ...graph.margins } : undefined
    };
  }

  function cloneMap(map: LayeredMapScene): LayeredMapScene {
    return {
      viewport: {
        ...map.viewport,
        viewBox: [...map.viewport.viewBox] as [number, number, number, number]
      },
      layers: map.layers.map((layer) => {
        if (layer.kind === "image") {
          return { ...layer };
        }

        if (layer.kind === "paths") {
          return {
            ...layer,
            items: layer.items.map((item) => ({ ...item }))
          };
        }

        if (layer.kind === "rects") {
          return {
            ...layer,
            items: layer.items.map((item) => ({ ...item }))
          };
        }

        return {
          ...layer,
          items: layer.items.map((item) => ({ ...item }))
        };
      })
    };
  }

  function setLineReveal(graph: XYGraph, lineId: string, drawTo: number, opacity?: number) {
    graph.lines = graph.lines.map((line) =>
      line.id === lineId
        ? {
            ...line,
            drawTo,
            opacity: opacity ?? line.opacity
          }
        : line
    );
  }

  function linearAxisReveal(axis: XYGraph["xAxis"], value: number) {
    const [min, max] = axis.domain;

    if (max <= min) {
      return 1;
    }

    return Math.min(Math.max((value - min) / (max - min), 0), 1);
  }

  function buildWorldCurveGraph(activeStepIndex: number, stepProgress: number): XYGraph {
    const graph = cloneGraph(generatedFigures.figure08.graph);

    graph.xAxis.opacity = activeStepIndex === 0 ? stepProgress : 1;
    graph.yAxis.opacity = activeStepIndex < 1 ? 0 : activeStepIndex === 1 ? stepProgress : 1;
    setLineReveal(graph, "world", activeStepIndex < 2 ? 0 : activeStepIndex === 2 ? stepProgress : 1);

    return graph;
  }

  function buildRegionGraph(activeStepIndex: number, stepProgress: number): XYGraph {
    const graph = cloneGraph(generatedFigures.figure09.graph);
    const lineSteps = [
      { id: "asia", step: 0 },
      { id: "africa", step: 1 },
      { id: "europe", step: 2 },
      { id: "americas", step: 3 }
    ];

    setLineReveal(graph, "world", 1, graph.lines.find((line) => line.id === "world")?.opacity ?? 0.72);

    lineSteps.forEach(({ id, step }) => {
      const drawTo = activeStepIndex < step ? 0 : activeStepIndex === step ? stepProgress : 1;
      setLineReveal(graph, id, drawTo);
    });

    return graph;
  }

  function buildUsaPeriodsGraph(activeStepIndex: number, stepProgress: number): XYGraph {
    const graph = cloneGraph(generatedFigures.figure11.graph);

    setLineReveal(graph, "usa-early", activeStepIndex === 0 ? stepProgress : 1);
    setLineReveal(graph, "usa-late", activeStepIndex < 1 ? 0 : activeStepIndex === 1 ? stepProgress : 1);

    return graph;
  }

  function buildUsaKoreaPeriodsGraph(activeStepIndex: number, stepProgress: number): XYGraph {
    const graph = cloneGraph(generatedFigures.figure12.graph);

    setLineReveal(graph, "usa-early", 1);
    setLineReveal(graph, "usa-late", 1);
    setLineReveal(graph, "korea-early", activeStepIndex === 0 ? stepProgress : 1);
    setLineReveal(graph, "korea-late", activeStepIndex < 1 ? 0 : activeStepIndex === 1 ? stepProgress : 1);

    return graph;
  }

  function buildScenarioGraph(activeStepIndex: number, stepProgress: number): XYGraph {
    const graph = cloneGraph(generatedFigures.figure13.graph);
    const sharedHistoryDrawTo = linearAxisReveal(graph.xAxis, 2025);

    graph.xAxis.opacity = 1;
    graph.yAxis.opacity = 1;

    if (activeStepIndex === 0) {
      const historyReveal = sharedHistoryDrawTo * stepProgress;
      setLineReveal(graph, "runaway", historyReveal);
      setLineReveal(graph, "extrapolation", historyReveal, 0.6);
      setLineReveal(graph, "lifecycle", historyReveal, 0.6);
      setLineReveal(graph, "proportional", historyReveal, 0.6);
      return graph;
    }

    setLineReveal(graph, "runaway", activeStepIndex === 1 ? sharedHistoryDrawTo + (1 - sharedHistoryDrawTo) * stepProgress : 1);
    setLineReveal(graph, "extrapolation", activeStepIndex >= 2 ? (activeStepIndex === 2 ? sharedHistoryDrawTo + (1 - sharedHistoryDrawTo) * stepProgress : 1) : sharedHistoryDrawTo, activeStepIndex >= 2 ? undefined : 0.6);
    setLineReveal(graph, "lifecycle", activeStepIndex < 3 ? sharedHistoryDrawTo : sharedHistoryDrawTo + (1 - sharedHistoryDrawTo) * rangeProgress(stepProgress, 0, 0.7), activeStepIndex < 3 ? 0.6 : undefined);
    setLineReveal(graph, "proportional", activeStepIndex < 3 ? sharedHistoryDrawTo : sharedHistoryDrawTo + (1 - sharedHistoryDrawTo) * rangeProgress(stepProgress, 0.25, 1), activeStepIndex < 3 ? 0.6 : undefined);

    return graph;
  }

  const dotComparisonScenes: DotComparisonScene[] = [
    {
      smallLabel: "100K metro",
      largeLabel: "10M metro",
      metric: null,
      baseGlow: 0.1,
      baseWarning: 0,
      baseCo2: 0
    },
    {
      smallLabel: "100K metro",
      largeLabel: "10M metro",
      metric: dotComparisonMetrics.gdp,
      baseGlow: 0.1,
      baseWarning: 0,
      baseCo2: 0
    },
    {
      smallLabel: "100K metro",
      largeLabel: "10M metro",
      metric: dotComparisonMetrics.patents,
      baseGlow: 0.1,
      baseWarning: 0,
      baseCo2: 0
    },
    {
      smallLabel: "100K metro",
      largeLabel: "10M metro",
      metric: dotComparisonMetrics.housing,
      baseGlow: 0.1,
      baseWarning: 0,
      baseCo2: 0
    },
    {
      smallLabel: "100K metro",
      largeLabel: "10M metro",
      metric: dotComparisonMetrics.co2,
      baseGlow: 0.1,
      baseWarning: 0,
      baseCo2: 0
    }
  ];

  function buildFutureDistributionScene(activeStepIndex: number): FutureDistributionScene {
    const scenes = generatedFigures.figure02.scenes;
    const state = scenes[Math.min(activeStepIndex, scenes.length - 1)];

    return {
      bins: state.bins.map((bin) => ({ ...bin })),
      baseCounts: [...state.baseCounts],
      futureCounts: [...state.futureCounts],
      maxFutureByBin: [...generatedFigures.figure02.meta.brick.maxFutureByBin],
      futureColor: state.futureColor,
      futureLabel: state.futureLabel
    };
  }

  function buildParisMap(activeStepIndex: number, stepProgress: number): LayeredMapScene {
    const map = cloneMap(generatedFigures.figure03.map);
    const scenes = generatedFigures.figure03.scenes;
    const currentScene = scenes[Math.min(activeStepIndex, scenes.length - 1)];
    const previousScene = activeStepIndex > 0 ? scenes[Math.min(activeStepIndex - 1, scenes.length - 1)] : null;
    const currentVisible = new Set(currentScene?.visibleLayerIds ?? []);
    const previousVisible = new Set(previousScene?.visibleLayerIds ?? []);

    map.layers = map.layers.map((layer) => {
      if (layer.id === "satellite") {
        return {
          ...layer,
          opacity: 1
        };
      }

      const isVisible = currentVisible.has(layer.id);
      const isNewlyVisible = isVisible && !previousVisible.has(layer.id);
      const layerOpacity = !isVisible ? 0 : isNewlyVisible ? stepProgress : 1;

      if (layer.kind !== "paths") {
        return {
          ...layer,
          opacity: layerOpacity
        };
      }

      const drawTo = layer.id.includes("boundary") ? layerOpacity : undefined;
      const isBuiltFill = layer.id === "built-fill";

      return {
        ...layer,
        opacity: layerOpacity,
        items: layer.items.map((item) => ({
          ...item,
          fill: isBuiltFill ? "#d4d9df" : item.fill,
          fillOpacity: isBuiltFill ? 0.4 : item.fillOpacity,
          drawTo
        }))
      };
    });

    return map;
  }

  function buildPrdMap(activeStepIndex: number, stepProgress: number): LayeredMapScene {
    const map = cloneMap(generatedFigures.figure07.map);
    map.viewport.background = "#050607";
    const scenes = generatedFigures.figure07.scenes;
    const currentScene = scenes[Math.min(activeStepIndex, scenes.length - 1)];
    const previousScene = activeStepIndex > 0 ? scenes[Math.min(activeStepIndex - 1, scenes.length - 1)] : null;
    const currentVisible = new Set(currentScene?.visibleLayerIds ?? []);
    const previousVisible = new Set(previousScene?.visibleLayerIds ?? []);

    map.layers = map.layers.map((layer) => {
      const isVisible = currentVisible.has(layer.id);
      const isNewlyVisible = isVisible && !previousVisible.has(layer.id);
      const layerOpacity = !isVisible ? 0 : isNewlyVisible ? stepProgress : 1;

      return {
        ...layer,
        opacity: layerOpacity
      };
    });

    return map;
  }

  function buildGhslMap(activeStepIndex: number, stepProgress: number): LayeredMapScene {
    const squareGrid = buildParisAlignedGrid(15);
    const ghslPrepared = buildGhslCells(squareGrid);
    const ghslCells = ghslPrepared.cells;
    const ghslClusters = clusterGhslCells(ghslCells, squareGrid.cells);
    const builtReveal = stepReveal(activeStepIndex, 1, stepProgress);
    const urbanReveal = stepReveal(activeStepIndex, 2, stepProgress);
    const clusterReveal =
      activeStepIndex < 3 ? 0 : activeStepIndex > 3 ? 1 : rangeProgress(stepProgress, 0, 0.22);
    const parisBaseLayer = generatedFigures.figure03.map.layers.find((layer) => layer.kind === "image");
    const baseHref = parisBaseLayer?.kind === "image" ? parisBaseLayer.href : ghslBaseImage;
    const [minX, minY, mapWidth, mapHeight] = generatedFigures.figure03.map.viewport.viewBox;
    const baseOpacity = Math.max(0.52, 0.9 - builtReveal * 0.18 - urbanReveal * 0.08 - clusterReveal * 0.06);

    return {
      viewport: {
        viewBox: [minX, minY, mapWidth, mapHeight],
        background: "#050607"
      },
      layers: [
        {
          id: "base-image",
          kind: "image",
          href: baseHref,
          x: minX,
          y: minY,
          width: mapWidth,
          height: mapHeight,
          opacity: baseOpacity
        },
        {
          id: "frame-backdrop",
          kind: "rects",
          items: [
            {
              x: squareGrid.x,
              y: squareGrid.y,
              width: squareGrid.size,
              height: squareGrid.size,
              rx: 16,
              ry: 16,
              fill: "#091015",
              fillOpacity: builtReveal > 0 ? 0.34 : 0.06,
              stroke: "rgba(255,255,255,0.16)",
              strokeOpacity: 1,
              strokeWidth: 2
            }
          ]
        },
        {
          id: "built-fraction-grid",
          kind: "rects",
          opacity: builtReveal,
          items: ghslCells.map((cell) => ({
            x: cell.x + 1.2,
            y: cell.y + 1.2,
            width: squareGrid.cellWidth - 2.4,
            height: squareGrid.cellHeight - 2.4,
            fill: "#d7aa72",
            fillOpacity: 0.08 + cell.value * 0.82,
            stroke: "rgba(255,255,255,0.03)",
            strokeOpacity: 1,
            strokeWidth: 0.8
          }))
        },
        {
          id: "urban-grid",
          kind: "rects",
          opacity: urbanReveal,
          items: ghslCells.map((cell) => ({
            x: cell.x + 1.2,
            y: cell.y + 1.2,
            width: squareGrid.cellWidth - 2.4,
            height: squareGrid.cellHeight - 2.4,
            fill: cell.urban ? "#efe7db" : "#182027",
            fillOpacity: cell.urban ? 0.92 : 0.22,
            stroke: "rgba(255,255,255,0.04)",
            strokeOpacity: 1,
            strokeWidth: 0.8
          }))
        },
        {
          id: "cluster-grid",
          kind: "rects",
          opacity: clusterReveal,
          items: ghslCells
            .filter((cell) => cell.urban && cell.clusterId != null && cell.clusterId < 4)
            .map((cell) => ({
              x: cell.x + 1.2,
              y: cell.y + 1.2,
              width: squareGrid.cellWidth - 2.4,
              height: squareGrid.cellHeight - 2.4,
              fill: ghslClusters[cell.clusterId ?? 0]?.color ?? "#7ab6a7",
              fillOpacity: 0.92,
              stroke: "rgba(255,255,255,0.08)",
              strokeOpacity: 1,
              strokeWidth: 0.8
            }))
        },
        {
          id: "cluster-labels",
          kind: "labels",
          opacity: clusterReveal,
          items: ghslClusters.slice(0, 3).map((cluster) => ({
            x: cluster.cx,
            y: cluster.cy,
            text: `C${cluster.id}`,
            fill: "#f5efe5",
            fontSize: 34,
            fontWeight: 800,
            anchor: "middle" as const,
            opacity: 0.98
          }))
        }
      ]
    };
  }

  function buildAllocationMap(activeStepIndex: number, stepProgress: number): LayeredMapScene {
    const squareGrid = buildParisAlignedGrid(12);
    const districtConfigs = buildDistrictConfigs(squareGrid);
    const allocationPrepared = buildAllocationCells(squareGrid, districtConfigs);
    const allocationCells = allocationPrepared.cells;
    const allocationDistrictTotals = allocationPrepared.totals;
    const volumeReveal = activeStepIndex < 1 ? 0 : activeStepIndex > 1 ? 1 : rangeProgress(stepProgress, 0, 0.7);
    const censusReveal = activeStepIndex < 2 ? 0 : activeStepIndex > 2 ? 1 : rangeProgress(stepProgress, 0, 0.24);
    const parisBaseLayer = generatedFigures.figure03.map.layers.find((layer) => layer.kind === "image");
    const baseHref = parisBaseLayer?.kind === "image" ? parisBaseLayer.href : allocationBaseImage;
    const [minX, minY, mapWidth, mapHeight] = generatedFigures.figure03.map.viewport.viewBox;

    const volumeFrontA: [number, number, number] = [84, 126, 142];
    const volumeFrontB: [number, number, number] = [160, 205, 222];
    const volumeSideA: [number, number, number] = [61, 93, 110];
    const volumeSideB: [number, number, number] = [120, 164, 182];
    const volumeTopA: [number, number, number] = [190, 220, 232];
    const volumeTopB: [number, number, number] = [227, 241, 247];
    const popFrontA: [number, number, number] = [154, 118, 88];
    const popFrontB: [number, number, number] = [237, 190, 124];
    const popSideA: [number, number, number] = [122, 88, 64];
    const popSideB: [number, number, number] = [196, 151, 104];
    const popTopA: [number, number, number] = [222, 193, 151];
    const popTopB: [number, number, number] = [255, 232, 184];

    const districtLabelWidth = 212;
    const districtLabelHeight = 104;

    const groundRects = allocationCells.map((cell) => ({
      x: cell.x + 0.8,
      y: cell.y + 0.8,
      width: squareGrid.cellWidth - 1.6,
      height: squareGrid.cellHeight - 1.6,
      fill: censusReveal > 0 ? districtConfigs[cell.district].color : "#433d33",
      fillOpacity: censusReveal > 0 ? 0.18 : 0.12,
      stroke: "rgba(255,255,255,0.06)",
      strokeOpacity: 1,
      strokeWidth: 0.8
    }));

    const volumeBars = allocationCells.flatMap((cell, index) => {
      if (cell.volume <= 0.08) {
        return [];
      }

      const paths = isoBarPaths(
        cell.x,
        cell.y,
        squareGrid.cellWidth,
        squareGrid.cellHeight,
        cell.volume * 54
      );
      const front = rgb(mixTriplet(volumeFrontA, volumeFrontB, cell.volume));
      const side = rgb(mixTriplet(volumeSideA, volumeSideB, cell.volume));
      const roof = rgb(mixTriplet(volumeTopA, volumeTopB, cell.volume));

      return [
        { id: `bar-front-${index}`, d: paths.front, fill: front, fillOpacity: 0.96, opacity: 1 },
        { id: `bar-side-${index}`, d: paths.side, fill: side, fillOpacity: 0.96, opacity: 1 },
        { id: `bar-roof-${index}`, d: paths.roof, fill: roof, fillOpacity: 0.98, opacity: 1 }
      ];
    });

    const districtAreas = districtConfigs.map((district, index) => ({
      id: `district-area-${district.key}`,
      d: pointsToPath(district.points),
      fill: district.color,
      fillOpacity: 0.14,
      stroke: district.color,
      strokeOpacity: 0.4,
      strokeWidth: 2,
      opacity: censusReveal
    }));

    const districtBoundaries = districtConfigs.map((district) => ({
      id: `district-boundary-${district.key}`,
      d: pointsToPath(district.points),
      stroke: "rgba(248,242,231,0.88)",
      strokeWidth: 4,
      opacity: censusReveal,
      drawTo: censusReveal
    }));

    const districtLabelBackgrounds = districtConfigs.map((district) => ({
      x: district.anchorX - districtLabelWidth / 2,
      y: district.anchorY - districtLabelHeight / 2,
      width: districtLabelWidth,
      height: districtLabelHeight,
      rx: 14,
      ry: 14,
      fill: district.color,
      fillOpacity: 0.92,
      opacity: censusReveal
    }));

    const districtLabels = districtConfigs.flatMap((district, index) => ([
      {
        id: `district-name-${district.key}`,
        x: district.anchorX,
        y: district.anchorY - 16,
        text: `ADMIN ${district.key}`,
        fill: "#f5efe5",
        fontSize: 30,
        fontWeight: 800,
        anchor: "middle" as const,
        letterSpacing: "0.06em",
        opacity: censusReveal
      },
      {
        id: `district-total-${district.key}`,
        x: district.anchorX,
        y: district.anchorY + 28,
        text: `${Math.round(allocationDistrictTotals[index].population / 1000)}K`,
        fill: "#f5efe5",
        fontSize: 36,
        fontWeight: 800,
        anchor: "middle" as const,
        opacity: censusReveal
      }
    ]));

    const flowLines = allocationCells
      .filter((cell) => cell.volume > 0.08)
      .map((cell, index) => {
        const district = districtConfigs[cell.district];
        const labelEdgeY =
          district.linkDirection === "up"
            ? district.anchorY - districtLabelHeight / 2 + 6
            : district.anchorY + districtLabelHeight / 2 - 6;

        return {
          id: `flow-${index}`,
          d: `M ${district.anchorX} ${labelEdgeY} L ${cell.cx} ${cell.cy}`,
          stroke: district.color,
          strokeOpacity: 0.38,
          strokeWidth: 2,
          opacity: censusReveal
        };
      });

    return {
      viewport: {
        viewBox: [minX, minY, mapWidth, mapHeight],
        background: "#050607"
      },
      layers: [
        {
          id: "allocation-base",
          kind: "image",
          href: baseHref,
          x: minX,
          y: minY,
          width: mapWidth,
          height: mapHeight,
          opacity: 0.56
        },
        {
          id: "allocation-frame",
          kind: "rects",
          items: [
            {
              x: squareGrid.x,
              y: squareGrid.y,
              width: squareGrid.size,
              height: squareGrid.size,
              rx: 16,
              ry: 16,
              fill: "#10161b",
              fillOpacity: 0.12,
              stroke: "rgba(255,255,255,0.14)",
              strokeOpacity: 1,
              strokeWidth: 2
            }
          ]
        },
        {
          id: "ground-grid",
          kind: "rects",
          items: groundRects
        },
        {
          id: "district-areas",
          kind: "paths",
          opacity: censusReveal,
          items: districtAreas
        },
        {
          id: "volume-bars",
          kind: "paths",
          opacity: volumeReveal,
          items: volumeBars
        },
        {
          id: "district-boundaries",
          kind: "paths",
          opacity: censusReveal,
          items: districtBoundaries
        },
        {
          id: "allocation-flows",
          kind: "paths",
          opacity: censusReveal,
          items: flowLines
        },
        {
          id: "district-label-bgs",
          kind: "rects",
          opacity: censusReveal,
          items: districtLabelBackgrounds
        },
        {
          id: "district-labels",
          kind: "labels",
          opacity: censusReveal,
          items: districtLabels
        }
      ]
    };
  }

  function getXYGraph(kind: SceneKind, activeStepIndex: number, stepProgress: number): XYGraph {
    if (kind === "xy-world") {
      return buildWorldCurveGraph(activeStepIndex, stepProgress);
    }

    if (kind === "xy-regions") {
      return buildRegionGraph(activeStepIndex, stepProgress);
    }

    if (kind === "xy-usa-periods") {
      return buildUsaPeriodsGraph(activeStepIndex, stepProgress);
    }

    if (kind === "xy-usa-korea-periods") {
      return buildUsaKoreaPeriodsGraph(activeStepIndex, stepProgress);
    }

    return buildScenarioGraph(activeStepIndex, stepProgress);
  }

  function getLayeredMap(kind: SceneKind, activeStepIndex: number, stepProgress: number): LayeredMapScene {
    if (kind === "map-ghsl") {
      return buildGhslMap(activeStepIndex, stepProgress);
    }

    if (kind === "map-allocation") {
      return buildAllocationMap(activeStepIndex, stepProgress);
    }

    if (kind === "map-prd") {
      return buildPrdMap(activeStepIndex, stepProgress);
    }

    return buildParisMap(activeStepIndex, stepProgress);
  }

  function getDotComparison(kind: SceneKind, activeStepIndex: number): DotComparisonScene {
    return dotComparisonScenes[Math.min(activeStepIndex, dotComparisonScenes.length - 1)];
  }

  function getFutureDistribution(
    kind: SceneKind,
    activeStepIndex: number
  ): FutureDistributionScene {
    return buildFutureDistributionScene(activeStepIndex);
  }

  function legendItemsFromGenerated(legend: GeneratedLegend[]): LegendItem[] {
    return legend.map((item) => ({
      label: item.label,
      color: item.color,
      shape: "line",
      linePattern: item.linePattern
    }));
  }

  function getLegendItems(kind: SceneKind, activeStepIndex = 0): LegendItem[] {
    if (kind === "dot-comparison") {
      return [
        { label: "GDP", color: "#8ac6ff", shape: "fill" },
        { label: "Patents", color: "#67e0cc", shape: "fill" },
        { label: "Housing", color: "#ff8d6b", shape: "fill" },
        { label: "CO2", color: "#f2c56f", shape: "fill" }
      ];
    }

    if (kind === "future-distribution") {
      const scene = buildFutureDistributionScene(activeStepIndex);
      return [
        { label: "Current urban population", color: "#2d3844", shape: "fill" },
        { label: "Incoming future residents", color: scene.futureColor, shape: "fill" }
      ];
    }

    if (kind === "xy-world") {
      return [{ label: "World", color: "#67e0cc", shape: "line" }];
    }

    if (kind === "xy-regions") {
      const visibleIds = ["world", "asia", "africa", "europe", "americas"].slice(0, activeStepIndex + 2);
      return legendItemsFromGenerated(
        (generatedFigures.figure09.legend ?? []).filter((item) => visibleIds.includes(item.id))
      );
    }

    if (kind === "xy-usa-periods") {
      const visibleIds = ["usa-early", "usa-late"].slice(0, activeStepIndex + 1);
      return legendItemsFromGenerated(
        (generatedFigures.figure11.legend ?? []).filter((item) => visibleIds.includes(item.id))
      );
    }

    if (kind === "xy-usa-korea-periods") {
      const visibleIds = ["usa-early", "usa-late", "korea-early", "korea-late"].slice(0, activeStepIndex + 3);
      return legendItemsFromGenerated(
        (generatedFigures.figure12.legend ?? []).filter((item) => visibleIds.includes(item.id))
      );
    }

    if (kind === "xy-scenarios") {
      const visibleIds =
        activeStepIndex === 0
          ? []
          : activeStepIndex === 1
            ? ["runaway"]
            : activeStepIndex === 2
              ? ["runaway", "extrapolation"]
              : ["runaway", "extrapolation", "lifecycle", "proportional"];
      return legendItemsFromGenerated(
        (generatedFigures.figure13.legend ?? []).filter((item) => visibleIds.includes(item.id))
      );
    }

    if (kind === "map-prd") {
      const visibleIds = new Set(
        generatedFigures.figure07.scenes[Math.min(activeStepIndex, generatedFigures.figure07.scenes.length - 1)]
          ?.visibleLayerIds ?? []
      );

      return generatedFigures.figure07.map.layers.flatMap((layer) => {
        if (layer.kind !== "paths" || !visibleIds.has(layer.id) || !layer.id.startsWith("prd-")) {
          return [];
        }

        return [{
          label: layer.id.replace("prd-", ""),
          color: layer.items[0]?.fill ?? "#67e0cc",
          shape: "fill" as const
        }];
      });
    }

    if (kind === "map-ghsl") {
      return [
        { label: "Built-up area", color: "#d7aa72", shape: "fill" },
        { label: "Urban cells", color: "#efe7db", shape: "fill" },
        { label: "Clusters", color: "#7ab6a7", shape: "fill" }
      ];
    }

    if (kind === "map-allocation") {
      return [
        { label: "Volume", color: "#8db8ca", shape: "fill" },
        { label: "Admin area", color: "#efc684", shape: "fill" }
      ];
    }

    if (kind === "placeholder") {
      return [];
    }

    return [
      { label: "Paris proper", color: "#ff8b67", shape: "outline" },
      { label: "Built-up area", color: "#cfd6dd", shape: "fill" },
      { label: "Attraction area", color: "#67e0cc", shape: "outline" }
    ];
  }

  function getPrdTimelineItems(activeStepIndex: number) {
    return generatedFigures.figure07.map.layers.flatMap((layer, index) => {
      if (layer.kind !== "paths" || !layer.id.startsWith("prd-")) {
        return [];
      }

      return [{
        id: layer.id,
        label: layer.id.replace("prd-", ""),
        color: layer.items[0]?.fill ?? "#67e0cc",
        state:
          index < activeStepIndex
            ? "past"
            : index === activeStepIndex
              ? "current"
              : "future"
      }];
    });
  }
</script>

<svelte:head>
  <title>Are we all going to live in megacities?</title>
  <meta
    name="description"
    content="Template scroll built from outline5 with the current mock figure components in their article order."
  />
</svelte:head>

<svelte:window on:scroll={updateArticleProgress} on:resize={updateArticleProgress} />

<div class="article-progress" aria-hidden="true">
  <div class="article-progress-fill" style={`transform: scaleX(${articleProgress})`}></div>
</div>

<main class="page">
  <article class="article intro">
    <h1>Are we all going to live in megacities?</h1>
    <div class="prose">
      {#each introParagraphs as paragraph}
        <CitedParagraph {paragraph} />
      {/each}
    </div>
  </article>

  {#each stickyScenes as scene, index (scene.id)}
    <StickyScene
      sceneId={scene.id}
      ariaLabel={scene.ariaLabel}
      pinDurationVh={scene.pinDurationVh}
      tailHoldVh={scene.tailHoldVh}
      stepHeightMultipliers={scene.stepHeightMultipliers}
      steps={scene.steps}
      let:activeStepIndex
      let:stepProgress
    >
      <svelte:fragment slot="overlay" let:activeStepIndex let:stepProgress>
        {#if scene.id === "figure-01" && activeStepIndex === 0}
          <div
            class="scene-intro-overlay"
            style={`opacity: ${Math.max(0, 1 - stepProgress * 1.35)}`}
            aria-hidden="true"
          >
            <div class="scene-intro-overlay-copy">
              <div class="scene-intro-overlay-title">Scroll down to continue</div>
              <div class="scene-intro-overlay-body">{introScrollHint}</div>
            </div>
            <div class="scene-intro-overlay-arrow">
              <svg
                class="scene-intro-overlay-arrow-svg"
                viewBox="0 0 80 120"
                aria-hidden="true"
                focusable="false"
              >
                <path d="M40 12 V88"></path>
                <path d="M18 66 L40 90 L62 66"></path>
              </svg>
            </div>
          </div>
        {/if}
      </svelte:fragment>

      {#if scene.kind === "dot-comparison"}
        <DotComparisonCanvas scene={getDotComparison(scene.kind, activeStepIndex)} />
      {:else if scene.kind === "future-distribution"}
        <FutureDistributionCanvas scene={getFutureDistribution(scene.kind, activeStepIndex)} />
      {:else if scene.kind === "placeholder"}
        <PlaceholderCanvas
          label={scene.placeholderLabel ?? "Figure placeholder"}
          note={scene.placeholderNote ?? "Mock pending"}
        />
      {:else if scene.kind === "map-paris" || scene.kind === "map-prd" || scene.kind === "map-ghsl" || scene.kind === "map-allocation"}
        <LayeredMapCanvas map={getLayeredMap(scene.kind, activeStepIndex, stepProgress)} />
      {:else}
        <XYGraphCanvas graph={getXYGraph(scene.kind, activeStepIndex, stepProgress)} />
      {/if}

      <svelte:fragment slot="legend" let:activeStepIndex>
        {#if scene.kind === "map-prd"}
          <div class="graph-legend timeline-legend">
            <div class="timeline-track"></div>
            {#each getPrdTimelineItems(activeStepIndex) as item (item.id)}
              <div class={`timeline-item ${item.state}`}>
                <span class="timeline-dot" style={`--legend-color: ${item.color}`}></span>
                <span class="timeline-label">{item.label}</span>
              </div>
            {/each}
          </div>
        {:else}
          <div class="graph-legend">
            {#each getLegendItems(scene.kind, activeStepIndex) as item (item.label)}
            <div class="legend-item">
              <span
                class={`legend-swatch ${item.shape ?? "line"} ${item.linePattern ?? "solid"}`}
                style={`--legend-color: ${item.color}`}
              ></span>
              <span>{item.label}</span>
            </div>
            {/each}
          </div>
        {/if}
      </svelte:fragment>
    </StickyScene>

    <ProseSection
      heading={proseSections[index].heading}
      paragraphs={proseSections[index].paragraphs}
    />
  {/each}

  <article class="article references-section">
    <h3 class="references-heading">References</h3>
    <ol class="reference-list">
      {#each references as reference}
        <li id={`reference-${reference.id}`}>
          <span class="reference-label">{reference.label}</span>
          <span>{reference.citation}</span>
          <a href={reference.href} target="_blank" rel="noopener noreferrer">{reference.href}</a>
        </li>
      {/each}
    </ol>
  </article>
</main>

<style>
  .article-progress {
    position: fixed;
    inset: 0 0 auto;
    z-index: 80;
    height: 4px;
    pointer-events: none;
  }

  .article-progress-fill {
    width: 100%;
    height: 100%;
    transform-origin: left center;
    background: currentColor;
    will-change: transform;
  }

  .page {
    width: 100%;
    overflow-x: clip;
  }

  .article {
    max-width: 550px;
    margin: 0 auto;
    padding: 26px 18px 56px;
  }

  .article.intro {
    padding-bottom: 6px;
  }

  h1 {
    margin: 0 0 18px;
    font-size: clamp(34px, 7vw, 64px);
    line-height: 0.95;
    letter-spacing: -0.03em;
  }

  .references-section {
    padding-top: 8px;
  }

  .references-heading {
    margin: 0 0 14px;
    font-size: clamp(20px, 4.6vw, 28px);
    line-height: 1.05;
    letter-spacing: -0.02em;
  }

  .reference-list {
    counter-reset: references;
    display: grid;
    gap: 16px;
    margin: 0;
    padding: 0;
    list-style: none;
    font-size: clamp(14px, 3.2vw, 16px);
    line-height: 1.45;
  }

  .reference-list li {
    counter-increment: references;
    display: grid;
    grid-template-columns: 28px minmax(0, 1fr);
    column-gap: 10px;
    color: #ddd4c8;
    scroll-margin-top: 24px;
  }

  .reference-list li::before {
    content: counter(references);
    color: #67e0cc;
    font-family: Arial, sans-serif;
    font-size: 13px;
    font-weight: 700;
    line-height: 1.2;
  }

  .reference-label {
    display: block;
    margin-bottom: 4px;
    color: #efe7db;
    font-family: Arial, sans-serif;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0;
    text-transform: uppercase;
  }

  .reference-label,
  .reference-list li > span:not(.reference-label),
  .reference-list a {
    grid-column: 2;
  }

  .reference-list a {
    display: block;
    width: fit-content;
    max-width: 100%;
    margin-top: 4px;
    color: #67e0cc;
    overflow-wrap: anywhere;
    text-decoration-thickness: 1px;
    text-underline-offset: 3px;
  }

  .prose {
    font-size: clamp(19px, 4.6vw, 24px);
    line-height: 1.52;
  }

  .graph-legend {
    height: 100%;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    gap: 10px 16px;
    padding: 8px 12px;
  }

  .scene-intro-overlay {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: flex-start;
    justify-content: center;
    padding: 16svh 18px 12svh;
    background: rgba(74, 80, 88, 0.34);
    backdrop-filter: blur(6px);
  }

  .scene-intro-overlay-copy {
    max-width: 420px;
    text-align: center;
  }

  .scene-intro-overlay-title {
    color: var(--ink);
    font-size: clamp(28px, 8vw, 46px);
    font-weight: 700;
    line-height: 0.98;
    letter-spacing: -0.03em;
  }

  .scene-intro-overlay-body {
    margin-top: 12px;
    color: #ece3d7;
    font-size: clamp(15px, 3.9vw, 20px);
    line-height: 1.35;
  }

  .scene-intro-overlay-arrow {
    position: absolute;
    left: 50%;
    top: 66%;
    transform: translateX(-50%);
    width: clamp(54px, 12vw, 88px);
    opacity: 0.95;
    animation: intro-arrow-bounce 1.5s ease-in-out infinite;
  }

  .scene-intro-overlay-arrow-svg {
    display: block;
    width: 100%;
    height: auto;
    overflow: visible;
    filter: drop-shadow(0 6px 18px rgba(0, 0, 0, 0.18));
  }

  .scene-intro-overlay-arrow-svg path {
    fill: none;
    stroke: var(--ink);
    stroke-width: 7;
    stroke-linecap: round;
    stroke-linejoin: round;
  }

  @keyframes intro-arrow-bounce {
    0%,
    100% {
      transform: translateX(-50%) translateY(0);
      opacity: 0.7;
    }

    50% {
      transform: translateX(-50%) translateY(10px);
      opacity: 1;
    }
  }

  .timeline-legend {
    position: relative;
    display: grid;
    grid-template-columns: repeat(6, minmax(0, 1fr));
    align-items: center;
    gap: 12px;
    padding: 10px 18px 8px;
  }

  .timeline-track {
    position: absolute;
    left: 9%;
    right: 9%;
    top: 34px;
    height: 2px;
    border-radius: 999px;
    background: rgba(205, 215, 225, 0.18);
  }

  .timeline-item {
    position: relative;
    z-index: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
    color: var(--muted);
    opacity: 0.38;
    transition: opacity 220ms ease;
  }

  .timeline-item.past,
  .timeline-item.current {
    opacity: 1;
  }

  .timeline-dot {
    width: 14px;
    height: 14px;
    border-radius: 999px;
    border: 2px solid color-mix(in srgb, var(--legend-color) 82%, white);
    background: var(--legend-color);
    box-shadow: 0 0 0 6px color-mix(in srgb, var(--card) 88%, transparent);
  }

  .timeline-item.current .timeline-dot {
    width: 18px;
    height: 18px;
    box-shadow:
      0 0 0 6px color-mix(in srgb, var(--card) 88%, transparent),
      0 0 18px color-mix(in srgb, var(--legend-color) 42%, transparent);
  }

  .timeline-label {
    font-family: Arial, sans-serif;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  .legend-item {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    color: var(--muted);
    font-family: Arial, sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  .legend-swatch {
    flex: none;
  }

  .legend-swatch.line {
    width: 20px;
    height: 4px;
    border-radius: 999px;
    background: var(--legend-color);
  }

  .legend-swatch.line.dashed {
    background: repeating-linear-gradient(
      to right,
      var(--legend-color) 0 10px,
      transparent 10px 16px
    );
  }

  .legend-swatch.line.dotted {
    background:
      radial-gradient(circle, var(--legend-color) 58%, transparent 62%)
      center / 8px 4px repeat-x;
  }

  .legend-swatch.fill,
  .legend-swatch.outline {
    width: 14px;
    height: 14px;
    border-radius: 4px;
  }

  .legend-swatch.fill {
    background: color-mix(in srgb, var(--legend-color) 28%, transparent);
    border: 1px solid color-mix(in srgb, var(--legend-color) 44%, transparent);
  }

  .legend-swatch.outline {
    background: transparent;
    border: 2px solid var(--legend-color);
  }

  @media (max-width: 720px) {
    .scene-intro-overlay {
      padding: 14svh 14px 10svh;
    }

    .scene-intro-overlay-body {
      margin-top: 10px;
    }

    .scene-intro-overlay-arrow {
      top: 68%;
      width: clamp(48px, 14vw, 76px);
    }

    .article {
      padding: 20px 16px 54px;
    }

    .graph-legend {
      gap: 8px 12px;
      padding-left: 10px;
      padding-right: 10px;
    }

    .timeline-legend {
      gap: 8px;
      padding: 10px 10px 8px;
    }

    .timeline-track {
      left: 10%;
      right: 10%;
      top: 30px;
    }

    .timeline-dot {
      width: 12px;
      height: 12px;
    }

    .timeline-item.current .timeline-dot {
      width: 16px;
      height: 16px;
    }

    .timeline-label {
      font-size: 9px;
      letter-spacing: 0.06em;
    }
  }
</style>
