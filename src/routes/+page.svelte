<script lang="ts">
  import type { XYGraph } from "$lib/components/xy-graph/types";
  import XYGraphCanvas from "$lib/components/xy-graph/XYGraphCanvas.svelte";
  import ProseSection from "../lib/components/ProseSection.svelte";
  import StickyScene from "../lib/components/StickyScene.svelte";

  const proseSections = [
    {
      heading: "Prose scene 1",
      paragraphs: [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris congue, justo eu feugiat pretium, tellus magna volutpat arcu, vitae feugiat lectus turpis sed risus.",
        "Suspendisse potenti. Cras euismod, nibh nec blandit suscipit, augue mauris aliquet augue, vitae faucibus risus orci id velit.",
        "Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Integer dictum, purus a pulvinar tempor, nisl mauris facilisis sem, sed cursus elit lorem a nunc."
      ]
    },
    {
      heading: "Prose scene 2",
      paragraphs: [
        "Curabitur aliquam feugiat quam, ac tincidunt neque fringilla sit amet. Praesent vehicula, purus sed tincidunt suscipit, metus libero commodo augue, sed sodales nibh ligula vitae sem.",
        "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec pharetra varius lorem, non hendrerit mauris volutpat eget.",
        "Aliquam erat volutpat. Sed et lorem sit amet ipsum iaculis malesuada. Donec rhoncus velit vitae risus imperdiet, ut elementum erat luctus."
      ]
    },
    {
      heading: "Prose scene 3",
      paragraphs: [
        "Nam euismod, lorem vel auctor tincidunt, felis turpis ultrices lorem, at pretium turpis turpis non massa. Ut ultrices mauris et mi finibus, ac ullamcorper nulla sagittis.",
        "Quisque tempor massa non purus facilisis, vitae tempor lectus ultrices. Integer luctus lectus eget vulputate blandit.",
        "Aenean non orci non erat fermentum finibus. Integer pellentesque felis in varius feugiat, arcu nisl viverra purus, id dictum est libero vitae nibh."
      ]
    }
  ];

  const stickyScenes = [
    {
      id: "sticky-1",
      ariaLabel: "Sticky test scene one",
      pinDurationVh: 300,
      steps: [
        { id: "step-1", kicker: "XY graph", title: "Load the x-axis", body: "Start by fading in the horizontal axis so the reader can anchor the population scale first." },
        { id: "step-2", kicker: "XY graph", title: "Now add the y-axis", body: "Then fade in the vertical axis and its scale. The chart only starts talking once both directions are legible." },
        { id: "step-3", kicker: "XY graph", title: "Draw the first line", body: "Finally draw the first curve with scroll. This is the most basic reusable analytic canvas." }
      ]
    },
    {
      id: "sticky-2",
      ariaLabel: "Sticky test scene two",
      pinDurationVh: 320,
      steps: [
        { id: "step-a", kicker: "XY graph", title: "Load the x-axis again", body: "The second chart should teach the frame the same way: start with the horizontal axis only." },
        { id: "step-b", kicker: "XY graph", title: "Now add the y-axis", body: "Then fade in the vertical scale, keeping the same graph shell while the values change." },
        { id: "step-c", kicker: "XY graph", title: "Draw the first scenario", body: "One curve can draw first while the others stay hidden." },
        { id: "step-d", kicker: "XY graph", title: "Add the remaining lines", body: "Additional curves then draw into the same coordinate system without changing the canvas type." }
      ]
    }
  ];

  const worldCurvePoints = [
    { x: 10_000, y: -10 },
    { x: 30_000, y: -9 },
    { x: 100_000, y: -7 },
    { x: 300_000, y: -3 },
    { x: 1_000_000, y: 2 },
    { x: 3_000_000, y: 8 },
    { x: 10_000_000, y: 17 }
  ];

  const runawayPoints = [
    { x: 1975, y: 16 },
    { x: 2000, y: 19 },
    { x: 2025, y: 25 },
    { x: 2050, y: 34 },
    { x: 2075, y: 45 },
    { x: 2100, y: 56 }
  ];

  const lifecyclePoints = [
    { x: 1975, y: 16 },
    { x: 2000, y: 19 },
    { x: 2025, y: 25 },
    { x: 2050, y: 31 },
    { x: 2075, y: 36 },
    { x: 2100, y: 41 }
  ];

  const proportionalPoints = [
    { x: 1975, y: 16 },
    { x: 2000, y: 19 },
    { x: 2025, y: 25 },
    { x: 2050, y: 29 },
    { x: 2075, y: 33 },
    { x: 2100, y: 36 }
  ];

  function rangeProgress(progress: number, start: number, end: number) {
    if (progress <= start) {
      return 0;
    }

    if (progress >= end) {
      return 1;
    }

    return (progress - start) / (end - start);
  }

  function buildWorldCurveGraph(activeStepIndex: number, stepProgress: number): XYGraph {
    return {
      xAxis: {
        domain: [10_000, 10_000_000],
        ticks: [
          { value: 10_000, label: "10K" },
          { value: 100_000, label: "100K" },
          { value: 1_000_000, label: "1M" },
          { value: 10_000_000, label: "10M" }
        ],
        label: "City population",
        scale: "log",
        opacity: activeStepIndex === 0 ? stepProgress : 1
      },
      yAxis: {
        domain: [-12, 22],
        ticks: [
          { value: -10, label: "-10%" },
          { value: 0, label: "0%" },
          { value: 10, label: "+10%" },
          { value: 20, label: "+20%" }
        ],
        label: "Growth relative to national urban average",
        opacity: activeStepIndex >= 1 ? (activeStepIndex === 1 ? stepProgress : 1) : 0
      },
      lines: [
        {
          id: "world",
          color: "#67e0cc",
          width: 5,
          points: worldCurvePoints,
          drawTo: activeStepIndex >= 2 ? stepProgress : 0
        }
      ],
      annotations: [
        {
          id: "world-100k",
          lineId: "world",
          point: { x: 100_000, y: -7 },
          title: "100K",
          subtitle: "-7%",
          orientation: "above"
        },
        {
          id: "world-1m",
          lineId: "world",
          point: { x: 1_000_000, y: 2 },
          title: "1M",
          subtitle: "+2%",
          orientation: "above"
        },
        {
          id: "world-10m",
          lineId: "world",
          point: { x: 10_000_000, y: 17 },
          title: "10M",
          subtitle: "+17%",
          orientation: "above",
          align: "end",
          dx: -12
        }
      ]
    };
  }

  function buildScenarioGraph(activeStepIndex: number, stepProgress: number): XYGraph {
    return {
      margins: {
        right: 80
      },
      xAxis: {
        domain: [1975, 2100],
        ticks: [
          { value: 1975, label: "1975" },
          { value: 2000, label: "2000" },
          { value: 2025, label: "2025" },
          { value: 2050, label: "2050" },
          { value: 2075, label: "2075" },
          { value: 2100, label: "2100" }
        ],
        label: "Year",
        scale: "linear",
        opacity: activeStepIndex === 0 ? stepProgress : 1
      },
      yAxis: {
        domain: [12, 58],
        ticks: [
          { value: 20, label: "20%" },
          { value: 30, label: "30%" },
          { value: 40, label: "40%" },
          { value: 50, label: "50%" }
        ],
        label: "World population in 1M+ cities",
        opacity: activeStepIndex >= 1 ? (activeStepIndex === 1 ? stepProgress : 1) : 0
      },
      lines: [
        {
          id: "runaway",
          color: "#ff8b67",
          width: 5,
          points: runawayPoints,
          drawTo: activeStepIndex >= 2 ? (activeStepIndex === 2 ? stepProgress : 1) : 0,
          endLabel: {
            text: "RW",
            dx: 10,
            dy: 6,
            anchor: "start",
            placement: "right-column"
          }
        },
        {
          id: "lifecycle",
          color: "#67e0cc",
          width: 5,
          points: lifecyclePoints,
          drawTo: activeStepIndex >= 3 ? rangeProgress(stepProgress, 0, 0.72) : 0,
          endLabel: {
            text: "LC",
            dx: 10,
            dy: 6,
            anchor: "start",
            placement: "right-column"
          }
        },
        {
          id: "proportional",
          color: "#8ac6ff",
          width: 5,
          points: proportionalPoints,
          drawTo: activeStepIndex >= 3 ? rangeProgress(stepProgress, 0.28, 1) : 0,
          endLabel: {
            text: "PO",
            dx: 10,
            dy: 8,
            anchor: "start",
            placement: "right-column"
          }
        }
      ]
    };
  }

  function getSceneGraph(sceneIndex: number, activeStepIndex: number, stepProgress: number) {
    return sceneIndex === 0
      ? buildWorldCurveGraph(activeStepIndex, stepProgress)
      : buildScenarioGraph(activeStepIndex, stepProgress);
  }

  function getLegendItems(sceneIndex: number) {
    return sceneIndex === 0
      ? [{ label: "World", color: "#67e0cc" }]
      : [
          { label: "Runaway", color: "#ff8b67" },
          { label: "Lifecycle", color: "#67e0cc" },
          { label: "Proportional", color: "#8ac6ff" }
        ];
  }
</script>

<svelte:head>
  <title>Minimal scrollytell scaffold</title>
  <meta
    name="description"
    content="Minimal SvelteKit and Scrollama scaffold with prose scenes and sticky scenes."
  />
</svelte:head>

<main class="page">
  <article class="article intro">
    <h1>Minimal scrollytell scaffold</h1>
    <div class="prose">
      <p>
        This version is intentionally stripped down. It only proves the two
        scene types we care about first: prose scenes and sticky scenes.
      </p>
      <p>
        The sticky scenes now mount the first reusable canvas family: a basic
        XY graph that can fade axes in and draw one or more lines with scroll.
      </p>
    </div>
  </article>

  <ProseSection
    heading={proseSections[0].heading}
    paragraphs={proseSections[0].paragraphs}
  />

  {#each stickyScenes as scene, index (scene.id)}
    <StickyScene
      sceneId={scene.id}
      ariaLabel={scene.ariaLabel}
      pinDurationVh={scene.pinDurationVh}
      steps={scene.steps}
      let:activeStepIndex
      let:stepProgress
    >
      <XYGraphCanvas graph={getSceneGraph(index, activeStepIndex, stepProgress)} />
      <div slot="legend" class="graph-legend">
        {#each getLegendItems(index) as item (item.label)}
          <div class="legend-item">
            <span class="legend-swatch" style={`--legend-color: ${item.color}`}></span>
            <span>{item.label}</span>
          </div>
        {/each}
      </div>
    </StickyScene>

    <ProseSection
      heading={proseSections[index + 1].heading}
      paragraphs={proseSections[index + 1].paragraphs}
    />
  {/each}
</main>

<style>
  .page {
    width: 100%;
    overflow-x: clip;
  }

  .article {
    max-width: 720px;
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
    width: 20px;
    height: 4px;
    border-radius: 999px;
    background: var(--legend-color);
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
  }
</style>
