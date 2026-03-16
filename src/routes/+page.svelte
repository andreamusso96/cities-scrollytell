<script lang="ts">
  import DotComparisonCanvas from "$lib/components/dot-comparison/DotComparisonCanvas.svelte";
  import type { DotComparisonScene } from "$lib/components/dot-comparison/types";
  import FutureDistributionCanvas from "$lib/components/future-distribution/FutureDistributionCanvas.svelte";
  import type { FutureDistributionScene } from "$lib/components/future-distribution/types";
  import LayeredMapCanvas from "$lib/components/layered-map/LayeredMapCanvas.svelte";
  import type { LayeredMapScene } from "$lib/components/layered-map/types";
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

  export let data: PageData;

  $: generatedFigures = data.generatedFigures as GeneratedFigures;

  const introParagraphs = [
    "Take two cities. One has 100,000 people. The other has 10 million. The bigger one does not just contain more people. Those people are qualitatively different. They are more productive, as measured by their wage, which is 74% higher.",
    "They are more innovative: they are 3.5 times more likely to produce a patent. As a result, wealth and innovation concentrate. In the United States, the ten most innovative metros account for 23% of the population, but 48% of patents and 33% of GDP.",
    "And when we get to fronteer knowledge this is even more pronounced. People in large cities are more 3.5 time more likely to produce any type of patent, but are X times more likely to produce a patent in a fronteer industry like farma or advanaced tech.",
        "The general idea is that there are non-linear scaling laws. As city get bigger --- their scale increases --- the people within them become qualitatively different, e.g.,they are more innovative, more productive.",
        "The scaling pattern, however, cuts both ways. The downsides scale too. For example, people in big cities have X% higher CO2 emissions. They are X% more likely to contract sexually transmitted diseases. They spend X% more time in traffic and X% more of their salary on their homes.",
        "Put simply, big cities amplify invention and income, but they also amplify congestion, land pressure, infrastructure stress."
  ];

  const proseSections: Array<{ heading?: string; paragraphs: string[] }> = [
    {
      paragraphs: [
        "So whether we are all going to live in megacities is a curiosity. It is a crucial determinant of how much wealth we can produce, where our technological frontier sits, and how we are going to impact and consume the resources of our planet.",
        "Cities overall are growing fast. Every 2 months the urban population adds 20 million people. That is one New York City worth of people. It was not always like this. In the 1800s, urbanization was a thing of few countries. Mostly industrializing countries in the west. England was first, followed by Benelux area. Then the US. Latin America. Southern Europe. North Africa. Evereyone else. [Check the sequence is correct]. Today, every country is either urban or rapidly urbanizing. More than 50% of humanity lives in cities. And in the next 75 years, cities are projected to add about X billion residents.",
        "Where will these people go? Small towns or sprawling mega-cities? Three scenarios are possible.",
        "In one, new urban residents spread across large and small cities alike, and the overall shape of the urban system stays roughly intact. That means that a good share of the whole population, say around X%, will continue to live in cities with fewer than 1M people.",
        "Another scenarios, the biggest cities absorb a disproportionate share of growth. People move to these urban behemoths. They grow faster than the rest and gobble up an every increasing share of the population. If today X% of the world population lives in 1M+ cities, in 2100 it could be X% or even much higher. Eventually, there will be just a couple of massive cities dominating the world population.",
        "In third scenario growth leans toward smaller cities, producing a more distributed urban future. The small cities get more of the pie. They grow faster than the big ones. Their X% share today becomes larger over time. And altough they grow larger, the population remains distributed across many places instead of piling up in a handfull of winners."
      ]
    },
    {
      paragraphs: [
        "So, which of these futures is more likely? That is the real question. The world is urbanizing fast, but which cities are absorbing that growth?",
        "Answering this question is hard. And the reason why its hard might be different from what you expect. Or at least it was different from what I expected. We use this word \"city\" to describe this thing where people live near each other.",
        "But the more I ponder the question \"what is a city\" the more it becomes hard to answer. Its one of those abstractions that make sweep all the complexity under the rug. But once you lift the rug, its a total mess.",
        "Take for example Paris. If you ask the French government what is Paris they might point you to the Legal borders of the city. This is an area of just 105.4 square kilometers and had about 2.11 million residents in 2022. This border is a fossil of historical accident. If you take a satellite picture of paris, you see that the built-up area has spilled way beyond the border in a much broader area. Various parts of the banlieu are effectively one physical unit with paris. And you can push it even further. Let's say now you consider not only the physical city, but the attraction area. The area from where people move into paris for work or other reasons. The people who are connected to paris but by invisble ties. Then that area is most of northern france. It stretched across 18,940.7 square kilometers and holds 13.24 million people. I guess you start seeing the problem: What is Paris? This question is hard to answer for Paris. But to understand where the world population is headed we have to answer them for every single damn city on this planet."
      ]
    },
    {
      paragraphs: [
        "For most of history, answering this questions was impossible. Not hard, impossible. You would have to put everyone in aggreement, every statistical agency on the planet, abotu the definition of city, and then maintain that agreement across time.",
        "Then satellites started quietly building a memory of the planet. Landsat has been observing the Earth since the 1970s. Sentinel-2 added much sharper optical imagery in the 2010s. Today, the planet get's photographed every second by a different satellites. This imagery made it possible to skip all the agreement. It created a picture of the earth that is comparable across all places, and adjusting the resolution also across all times. With some wizardry one could use those pictures to reconstruct cities and their populations.",
        "The basic idea is simple. First, you start from the pictures. You break this pictures into small cells. For each cell, you esitmate how much of each cell is physically built up: roofs, roads, blocks, industrial surfaces, the material footprint of settlement. With this data you can trace the boundaries of physical cities. That is, you get a grid 1kmx1km cells covering the whole planet, and its kinda easy to say whether a cell is urban or not. This is the work of the GHSL a european initiative.",
        "In my work, I take these grid to construct cities. The algorithm is simpl. First, I identify which cells count as urban. Then, I connect neighboring urban cells into clusters. Each cluster is a city."
      ]
    },
    {
      paragraphs: [
        "Next, I need to assign it a population. After all, we are interested in the population growth.",
        "Doing that require quite a bit of extra effort. You start by estimating the physical volume of houses in the cells. You look at shadows, re-project harmonize, to infer how a 3D volume of the built up material in a cell. You collect census totals reported for administrative areas. These areas tile up the whole worrld into small pieces. They might be of different size in different countries.Usually they are farily small, but not always so. Given the population in these areas, you redistributes those residents into grid cells using their volume from before. Where there is more volume, more people are assigned.Tada, you know have an guess, a pretty educated one, of how many people live in eavch 1kmx1km cell of the world. I then take this and my city boundaries, sum up all the people within the boundaries and get the population of the city in some givne year."
      ]
    },
    {
      paragraphs: [
        "Using that procedure, I build a dataset of global cities that covers 99 countries, about 94% of the world’s population, from 1975 to 2025, with 1,604,593 city-year observations."
      ]
    },
    {
      paragraphs: [
        "At first glance, the giants really do seem to be winning. The share of the world population living in million-plus cities rose from 11% in 1975 to 24% in 2025. And that in 10M+ cities rose from X% to X%. This trend is clear in developing coutnreis. Take for instance, Shenzen. It was a fisherman village in 1980 and its a 150 million metropolis today."
      ]
    },
    {
      paragraphs: [
        "Acoss the global data, larger cities often appear to outpace smaller ones. If we plot the size of city on the x-axis and its growth on the y-axis we observe that over time large cities outpaced their peers."
      ]
    },
    {
      paragraphs: [
        "Now this is self-reinforcing: If larger cities grow faster, they become larger, and this leads them to grow even faster, and so becom even larger. A small lead turns into a large lead. Follow that logic far enough and the future starts to look like a world increasingly dominated by giant cities.",
        "Yet, when you split the data, a different pattern appears. The average 1M+ city in Asia and Africa outgrew its national urban average by about 7% between 1975 and 2025. But in Europe, these cities barely outgrew the national average and in the Americas, 1M+ cities actually grew about 1.6% more slowly than the national average."
      ]
    },
    {
      paragraphs: [
        "At first, that looks like a geographic divide: perhaps Asia and Africa are giant-city regions, while Europe and the Americas are not. But another hypothesis is that timing matters: What looks like a map of regional difference is, to a large extent, a map of countries sitting at different stages of the same process.",
        "One way to check this is oreder countries on the x-axis by how much they are urbanized, and on the y-axis use a metric of how steep is teh curve between growth and size. How much large cities grow faster. When we do this, we observe a neat downward sloping correlation. More urbanized countries tend to see their large cities outgrowing the rest less.",
        "But to really determine this a cross-sectional snapshot is not enough. WE need a longitudinal series.",
        "The United States provides likely the one of the few longitudinal snapshot that are long enough to capture this phenoomenon. Long before satellites, long before digital maps, long before modern geographic information systems, the United States was already collecting census material rich enough that it can be turned back into a map of urban development. Census bureau officers went around the country, they asked registered individual people in individual places, every 10 years [More about how the census was collected]. These handwritten documents were passed down in library through generation, until recentrly a massive project transformed those old project in machine readable format, linked across years, matched to old places. The result of this massice effort is the: IPUMS Full Count now makes available over 800 million individual-level census records for 1850–1950.",
        "I took those records and reconstructed cities from 1850 to today. I constructed first grids of population and then aggregated them to cities. Surpsingly, these incredbile long run data. shows exactly the pattern the global data hint at. Early on, large U.S. cities had a strong growth advantage. Over time, that advantage weakened dramatically, until today its roughly flat."
      ]
    },
    {
      paragraphs: [
        "Another historical accident allows us to dig deeper. South Korea's economic miracle. Korea’s postwar transformation was not merely fast. It was historically extreme. The IMF describes three decades through the 1965-1995, in which annual real income growth averaged over 8% per year. The World Bank describes urbanization rising from 28% in 1960 to 79% in 1996, and GDP per person climbing from about $158 in 1960 to above $31,000 by 2020. That is development in fast-forward. This massive development pace implies that our global cities dataset 1975-2025 sees much of Korea's development. Of no other countries can be said the same.",
        "And guess what. Korea shows much the same plot in a few decades. Early on, Seoul and the largest Korean cities pull away hard. Later, the advantage fades. Put differntly, we continue to see evidence of this urban lyfecylce where big cities take the lead and but then petter out."
      ]
    },
    {
      paragraphs: [
        "Why would that be? The causes are likely many. Here is my take. Early in development, distance is expensive, markets are thin, and much of the economy is still tied tightly to land. Then transport improves. Manufacturing scales. Rail, ports, power, finance, universities, and state capacity reward concentration. Once one place gets ahead, the feedback loops start. Firms want access to customers. Workers go where the jobs are. Suppliers follow firms. Infrastructure follows everyone. A city that got a little ahead can suddenly get far ahead. Essentially, its like the arrival of modern technology opens new vast opportunities and large cities are the first to seize them.",
        "Then the systme. start hitting its limit. The logic changes. The rural reservoir shrinks. Transport and infrastructure spread outward. Secondary cities become capable of supporting their own thick labor markets. Land and housing costs bite harder in the biggest cores. Some growth spills into suburbs and satellites. S. All these conspire to slow the giants down.",
        "So where does this leaves us going forward? Where are we headed in 2100? If current 1975–2025 size-growth patterns were simply extended forward, that figure would be about 42%. But the self-reinforcing nature suggested above could push this even higher. The lifecycle model suggests instead somewhere around 38%. Relative to the straight extrapolation, that means about 450 million fewer people in million-plus cities by the end of the century."
      ]
    },
    {
      paragraphs: [
        "That is not a bookkeeping difference. The same scaling logic applies: these 450 million inhabitants will have see less wealth, invention, but also less inequality and climate risk as compared to a world where they had lived in large cities, and this will be visible in the aggregate, from global economic growth to climate change.",
        "So are we all going to live in giant cities?",
        "Probably not. At least not in the runaway way that a first glance at global city growth estimates suggests. But the giants forged by the large growth advantage in the early phases of urbanization will remain, amplifying wealth, invention, ambition, pressure, inequality, climate risk, and much more."
      ]
    }
  ];

  const displayedProseSections = proseSections.reduce<Array<{ heading?: string; paragraphs: string[] }>>(
    (sections, section, index) => {
      if (index === 5 && sections[4]) {
        sections[4] = {
          heading: sections[4].heading,
          paragraphs: [...sections[4].paragraphs, ...section.paragraphs]
        };
        return sections;
      }

      sections.push(section);
      return sections;
    },
    []
  );

  const stickyScenes: Array<{
    id: string;
    kind: SceneKind;
    ariaLabel: string;
    pinDurationVh: number;
    tailHoldVh?: number;
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
      steps: [
        { id: "dot-a", kicker: "City comparison", title: "Start with the two piles", body: "Use the same dot grammar on both sides. One city is sparse and legible; the other is dense enough to feel like a machine.", accentColor: "#67e0cc" },
        { id: "dot-b", kicker: "GDP", title: "Add output per person", body: "With respect to a person in a 100K metro, a person in a 10M city earns 24% more.", accentColor: "#8ac6ff" },
        { id: "dot-c", kicker: "Patents", title: "Now add invention", body: "With respect to a person in a 100K metro, a person in a 10M city produces 109% more patents.", accentColor: "#67e0cc" },
        { id: "dot-d", kicker: "Housing", title: "Now add housing pressure", body: "With respect to a person in a 100K metro, a person in a 10M city pays 41% more for housing.", accentColor: "#ff8d6b" },
        { id: "dot-e", kicker: "CO2", title: "Finish with emissions", body: "With respect to a person in a 100K metro, a person in a 10M city consumes 32% more CO2.", accentColor: "#f2c56f" }
      ]
    },
    {
      id: "figure-02",
      kind: "future-distribution",
      ariaLabel: "Figure 2",
      pinDurationVh: 340,
      tailHoldVh: 96,
      steps: [
        { id: "future-a", kicker: "Urbanization futures", title: "Today", body: "Start with the current distribution. The baseline already leans toward large metros, but it does not settle the future.", accentColor: "#2d3844" },
        { id: "future-b", kicker: "Urbanization futures", title: "Balanced growth", body: "Now add the next wave proportionally. Every bin grows, but the overall shape stays almost unchanged.", accentColor: "#67e0cc" },
        { id: "future-c", kicker: "Urbanization futures", title: "Giants win", body: "In this scenario, most new residents funnel into the large-metro bins. The right side swells fast.", accentColor: "#ff8b67" },
        { id: "future-d", kicker: "Urbanization futures", title: "Smaller cities catch up", body: "Here the added population spreads leftward. Growth still happens everywhere, but much more of it lands in smaller places.", accentColor: "#f0c66f" }
      ]
    },
    {
      id: "figure-03",
      kind: "map-paris",
      ariaLabel: "Figure 3",
      pinDurationVh: 360,
      steps: [
        { id: "paris-a", kicker: "Boundary problem", title: "Basemap only", body: "Start with a fixed spatial frame. Nothing moves yet; the point is to lock the reader into one region." },
        { id: "paris-b", kicker: "Administrative boundary", title: "Draw the legal core", body: "First reveal a compact legal city around the historic core. This is the smallest definition." },
        { id: "paris-c", kicker: "Morphological footprint", title: "Reveal the built city", body: "Then add the contiguous built-up footprint. It is clearly larger than the administrative core." },
        { id: "paris-d", kicker: "Attraction area", title: "Reveal the wider region", body: "Finally add the broader commuting and attraction area. The same place now covers far more territory." },
        { id: "paris-e", kicker: "Measurement problem", title: "The border changes the city", body: "Nothing moved on the map. Only the border changed, and yet the city became radically larger." }
      ]
    },
    {
      id: "figure-04",
      kind: "map-ghsl",
      ariaLabel: "Figure 4",
      pinDurationVh: 420,
      tailHoldVh: 132,
      steps: [
        { id: "ghsl-a", kicker: "Input surface", title: "Satellites see surfaces, not city names", body: "Start with one fixed frame. At this point the algorithm has not classified anything." },
        { id: "ghsl-b", kicker: "Built-up fraction", title: "Estimate built-up share cell by cell", body: "A regular grid samples the landscape. Some cells are barely built up; others are mostly settlement surface." },
        { id: "ghsl-c", kicker: "Urban classification", title: "Apply a cutoff: urban or non-urban", body: "The continuous surface becomes a clean binary classification. Cells above the threshold turn solid." },
        { id: "ghsl-d", kicker: "Cluster construction", title: "Merge neighboring urban cells", body: "Adjacency does the rest. Contiguous urban cells collapse into a small number of candidate city clusters." }
      ]
    },
    {
      id: "figure-05",
      kind: "map-allocation",
      ariaLabel: "Figure 5",
      pinDurationVh: 360,
      tailHoldVh: 112,
      steps: [
        { id: "alloc-a", kicker: "Residential signal", title: "Estimate residential building heights", body: "Start from imagery again. Roof texture and shadow hint at how much residential volume each cell contains." },
        { id: "alloc-b", kicker: "Residential volume", title: "Turn the grid into a 3D residential volume map", body: "Bars rise where residential built volume is larger. This becomes the weight used for redistribution." },
        { id: "alloc-c", kicker: "Census redistribution", title: "Administrative totals are pushed back into the grid", body: "Each district total is split across its cells. More residential volume receives a larger population share." }
      ]
    },
    {
      id: "figure-07",
      kind: "map-prd",
      ariaLabel: "Figure 7",
      pinDurationVh: 380,
      steps: [
        { id: "prd-a", kicker: "Pearl River Delta", title: "1975", body: "Start from the fragmented delta city field in 1975. The region is still a loose constellation of separate clusters.", accentColor: "#7a8794" },
        { id: "prd-b", kicker: "Pearl River Delta", title: "1985", body: "By 1985 the field thickens, but most clusters are still clearly distinct.", accentColor: "#93a2b2" },
        { id: "prd-c", kicker: "Pearl River Delta", title: "1995", body: "In 1995 the urban mass expands sharply across the delta.", accentColor: "#b2c0cf" },
        { id: "prd-d", kicker: "Pearl River Delta", title: "2005", body: "By 2005 the major centers are visibly pushing into one another.", accentColor: "#7ed7cb" },
        { id: "prd-e", kicker: "Pearl River Delta", title: "2015", body: "In 2015 the urbanized field becomes much more continuous across the estuary.", accentColor: "#8cf0de" },
        { id: "prd-f", kicker: "Pearl River Delta", title: "2025", body: "By 2025 the Pearl River Delta reads as a vast composite urban region rather than a handful of isolated cities.", accentColor: "#67e0cc" }
      ]
    },
    {
      id: "figure-08",
      kind: "xy-world",
      ariaLabel: "Figure 8",
      pinDurationVh: 300,
      steps: [
        { id: "step-1", kicker: "XY graph", title: "Load the x-axis", body: "Start by fading in the horizontal axis so the reader can anchor the population scale first." },
        { id: "step-2", kicker: "XY graph", title: "Now add the y-axis", body: "Then fade in the vertical axis and its scale. The chart only starts talking once both directions are legible." },
        { id: "step-3", kicker: "XY graph", title: "Draw the first line", body: "Finally draw the first curve with scroll. This is the most basic reusable analytic canvas." }
      ]
    },
    {
      id: "figure-09",
      kind: "xy-regions",
      ariaLabel: "Figure 9",
      pinDurationVh: 320,
      steps: [
        { id: "p9-a", kicker: "Regional split", title: "Add Asia", body: "Keep the world curve as the backdrop and draw Asia first, where large cities clearly pull ahead.", accentColor: "#ff8b67" },
        { id: "p9-b", kicker: "Regional split", title: "Add Africa", body: "Africa follows a similar pattern. Large cities there also outgrow the national urban average.", accentColor: "#f1c56d" },
        { id: "p9-c", kicker: "Regional split", title: "Add Europe", body: "Europe bends the pattern down. The large-city advantage is much weaker.", accentColor: "#8ac6ff" },
        { id: "p9-d", kicker: "Regional split", title: "Add the Americas", body: "In the Americas the curve flattens further and even tilts negative at the top end.", accentColor: "#b6dc7c" }
      ]
    },
    {
      id: "figure-11",
      kind: "xy-usa-periods",
      ariaLabel: "Figure 11",
      pinDurationVh: 260,
      steps: [
        { id: "p11-a", kicker: "U.S. lifecycle", title: "Draw the early United States", body: "In the early phase, larger U.S. cities enjoyed a strong growth premium over the national urban average.", accentColor: "#ff8b67" },
        { id: "p11-b", kicker: "U.S. lifecycle", title: "Add the later United States", body: "Later on, the same relationship flattens substantially. The large-city advantage weakens.", accentColor: "#8ac6ff" }
      ]
    },
    {
      id: "figure-12",
      kind: "xy-usa-korea-periods",
      ariaLabel: "Figure 12",
      pinDurationVh: 260,
      steps: [
        { id: "p12-a", kicker: "Korea in fast-forward", title: "Add early South Korea", body: "Use the U.S. pair as the reference, then draw Korea’s early period with its steep large-city premium.", accentColor: "#ff8b67" },
        { id: "p12-b", kicker: "Korea in fast-forward", title: "Add later South Korea", body: "Korea then moves toward the flatter later-stage pattern in just a few decades.", accentColor: "#8ac6ff" }
      ]
    },
    {
      id: "figure-13",
      kind: "xy-scenarios",
      ariaLabel: "Figure 13",
      pinDurationVh: 320,
      steps: [
        { id: "step-a", kicker: "XY graph", title: "Load the x-axis again", body: "The second chart should teach the frame the same way: start with the horizontal axis only.", accentColor: "#cfd6dd" },
        { id: "step-b", kicker: "XY graph", title: "Now add the y-axis", body: "Then fade in the vertical scale, keeping the same graph shell while the values change.", accentColor: "#cfd6dd" },
        { id: "step-c", kicker: "XY graph", title: "Draw the first scenario", body: "One curve can draw first while the others stay hidden.", accentColor: "#ff8b67" },
        { id: "step-d", kicker: "XY graph", title: "Add the remaining lines", body: "Additional curves then draw into the same coordinate system without changing the canvas type.", accentColor: "#f1c56d" }
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

  function buildWorldCurveGraph(activeStepIndex: number, stepProgress: number): XYGraph {
    const graph = cloneGraph(generatedFigures.figure08.graph);
    graph.yAxis.label = "Growth rate (log)";

    graph.xAxis.opacity = activeStepIndex === 0 ? stepProgress : 1;
    graph.yAxis.opacity = activeStepIndex < 1 ? 0 : activeStepIndex === 1 ? stepProgress : 1;
    setLineReveal(graph, "world", activeStepIndex < 2 ? 0 : activeStepIndex === 2 ? stepProgress : 1);

    return graph;
  }

  function buildRegionGraph(activeStepIndex: number, stepProgress: number): XYGraph {
    const graph = cloneGraph(generatedFigures.figure09.graph);
    graph.yAxis.label = "Growth rate (log)";
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
    graph.yAxis.label = "Growth rate (log)";

    setLineReveal(graph, "usa-early", activeStepIndex === 0 ? stepProgress : 1);
    setLineReveal(graph, "usa-late", activeStepIndex < 1 ? 0 : activeStepIndex === 1 ? stepProgress : 1);

    return graph;
  }

  function buildUsaKoreaPeriodsGraph(activeStepIndex: number, stepProgress: number): XYGraph {
    const graph = cloneGraph(generatedFigures.figure12.graph);
    graph.yAxis.label = "Growth rate (log)";

    setLineReveal(graph, "usa-early", 1);
    setLineReveal(graph, "usa-late", 1);
    setLineReveal(graph, "korea-early", activeStepIndex === 0 ? stepProgress : 1);
    setLineReveal(graph, "korea-late", activeStepIndex < 1 ? 0 : activeStepIndex === 1 ? stepProgress : 1);

    return graph;
  }

  function buildScenarioGraph(activeStepIndex: number, stepProgress: number): XYGraph {
    const graph = cloneGraph(generatedFigures.figure13.graph);

    graph.xAxis.opacity = activeStepIndex === 0 ? stepProgress : 1;
    graph.yAxis.opacity = activeStepIndex < 1 ? 0 : activeStepIndex === 1 ? stepProgress : 1;

    setLineReveal(graph, "runaway", activeStepIndex < 2 ? 0 : activeStepIndex === 2 ? stepProgress : 1);
    setLineReveal(graph, "extrapolation", activeStepIndex < 3 ? 0 : rangeProgress(stepProgress, 0, 0.4));
    setLineReveal(graph, "lifecycle", activeStepIndex < 3 ? 0 : rangeProgress(stepProgress, 0.2, 0.7));
    setLineReveal(graph, "proportional", activeStepIndex < 3 ? 0 : rangeProgress(stepProgress, 0.45, 1));

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
        activeStepIndex < 2
          ? []
          : activeStepIndex === 2
            ? ["runaway"]
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

<main class="page">
  <article class="article intro">
    <h1>Are we all going to live in megacities?</h1>
    <div class="prose">
      {#each introParagraphs as paragraph}
        <p>{paragraph}</p>
      {/each}
    </div>
  </article>

  {#each stickyScenes as scene, index (scene.id)}
    <StickyScene
      sceneId={scene.id}
      ariaLabel={scene.ariaLabel}
      pinDurationVh={scene.pinDurationVh}
      tailHoldVh={scene.tailHoldVh}
      steps={scene.steps}
      let:activeStepIndex
      let:stepProgress
    >
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
      heading={displayedProseSections[index].heading}
      paragraphs={displayedProseSections[index].paragraphs}
    />
  {/each}
</main>

<style>
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

  .prose {
    font-size: clamp(19px, 4.6vw, 24px);
    line-height: 1.52;
  }

  .prose p {
    margin: 0 0 1.1em;
    color: #ddd4c8;
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
