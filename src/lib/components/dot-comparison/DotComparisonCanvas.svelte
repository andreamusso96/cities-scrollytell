<script lang="ts">
  import type { DotComparisonScene } from "./types";

  export let scene: DotComparisonScene;

  type DotPoint = {
    x: number;
    y: number;
    r: number;
    dist?: number;
  };

  function mulberry32(seed: number) {
    return function () {
      let t = (seed += 0x6d2b79f5);
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  function buildGridPile(
    count: number,
    cx: number,
    cy: number,
    cols: number,
    spacing: number,
    jitter: number,
    r: number,
    seed: number
  ) {
    const rand = mulberry32(seed);
    const points: DotPoint[] = [];
    const rows = Math.ceil(count / cols);

    for (let i = 0; i < count; i += 1) {
      const col = i % cols;
      const row = Math.floor(i / cols);
      const width = (cols - 1) * spacing;
      const height = (rows - 1) * spacing;
      const x = cx - width / 2 + col * spacing + (rand() - 0.5) * jitter;
      const y = cy + height / 2 - row * spacing + (rand() - 0.5) * jitter;
      points.push({ x, y, r });
    }

    return points;
  }

  function buildDensePile(
    count: number,
    cx: number,
    cy: number,
    maxRadius: number,
    r: number,
    seed: number
  ) {
    const rand = mulberry32(seed);
    const points: DotPoint[] = [];

    for (let i = 0; i < count; i += 1) {
      const angle = rand() * Math.PI * 2;
      const radius = Math.pow(rand(), 0.62) * maxRadius;
      const x = cx + Math.cos(angle) * radius;
      const y = cy + Math.sin(angle) * radius * 0.86;
      points.push({ x, y, r, dist: radius / maxRadius });
    }

    points.sort((a, b) => (a.dist ?? 0) - (b.dist ?? 0));
    return points;
  }

  const smallPoints = buildGridPile(72, 224, 238, 8, 24, 1.5, 6, 4);
  const largePoints = buildDensePile(560, 574, 234, 156, 4.25, 9);

  const baseSmallOpacity = 0.96;
  const baseLargeOpacity = 0.9;
  const dividerX = 400;

  $: smallActive = new Set(scene.metric?.smallActive ?? []);
  $: largeActive = new Set(scene.metric?.largeActive ?? []);
  $: glowOpacity = scene.metric?.glow ?? scene.baseGlow ?? 0.1;
  $: warningOpacity = scene.metric?.warning ?? scene.baseWarning ?? 0;
  $: co2Opacity = scene.metric?.co2 ?? scene.baseCo2 ?? 0;
  $: smallBaseOpacity = scene.metric ? scene.metric.smallFade : baseSmallOpacity;
  $: largeBaseOpacity = scene.metric ? scene.metric.largeFade : baseLargeOpacity;
  $: highlightedSmallPoints = smallPoints.filter((_, index) => smallActive.has(index));
  $: largeOuterThreshold =
    scene.metric?.largeFilter?.mode === "outer-ring" ? scene.metric.largeFilter.minDist : null;
  $: highlightedLargePoints =
    largeOuterThreshold != null
      ? largePoints.filter((point) => (point.dist ?? 0) > largeOuterThreshold)
      : largePoints.filter((_, index) => largeActive.has(index));
</script>

<div class="dot-scene">
  <svg
    viewBox="0 0 800 600"
    role="img"
    aria-label="Two dot piles comparing a 100K metro with a 10M metro"
    preserveAspectRatio="xMidYMid meet"
  >
    <defs>
      <radialGradient id="centerGlow" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stop-color="#59dec8" stop-opacity="0.22"></stop>
        <stop offset="100%" stop-color="#59dec8" stop-opacity="0"></stop>
      </radialGradient>
      <radialGradient id="warningGlow" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stop-color="#ff8d6b" stop-opacity="0.18"></stop>
        <stop offset="100%" stop-color="#ff8d6b" stop-opacity="0"></stop>
      </radialGradient>
      <radialGradient id="co2Glow" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stop-color="#f2c56f" stop-opacity="0.16"></stop>
        <stop offset="100%" stop-color="#f2c56f" stop-opacity="0"></stop>
      </radialGradient>
    </defs>

    <line
      x1={dividerX}
      y1="74"
      x2={dividerX}
      y2="412"
      stroke="#1f252d"
      stroke-width="1.5"
    ></line>

    <circle cx="574" cy="234" r="184" fill="url(#centerGlow)" opacity={glowOpacity}></circle>
    <circle cx="574" cy="234" r="196" fill="url(#warningGlow)" opacity={warningOpacity}></circle>
    <circle cx="574" cy="234" r="204" fill="url(#co2Glow)" opacity={co2Opacity}></circle>

    <g aria-hidden="true">
      {#each smallPoints as point, index (index)}
        <circle
          class="dot"
          cx={point.x}
          cy={point.y}
          r={point.r}
          fill="#4a5562"
          opacity={smallBaseOpacity}
        ></circle>
      {/each}
    </g>

    <g aria-hidden="true">
      {#each largePoints as point, index (index)}
        <circle
          class="dot"
          cx={point.x}
          cy={point.y}
          r={point.r}
          fill="#3b4653"
          opacity={largeBaseOpacity}
        ></circle>
      {/each}
    </g>

    {#if scene.metric}
      <g aria-hidden="true">
        {#each highlightedSmallPoints as point, index (index)}
          <circle
            class="dot"
            cx={point.x}
            cy={point.y}
            r={point.r + 0.45}
            fill={scene.metric.color}
            opacity="1"
          ></circle>
        {/each}
      </g>

      <g aria-hidden="true">
        {#each highlightedLargePoints as point, index (index)}
          <circle
            class="dot"
            cx={point.x}
            cy={point.y}
            r={point.r + 0.3}
            fill={scene.metric.color}
            opacity="1"
          ></circle>
        {/each}
      </g>
    {/if}

    <text x="224" y="482" text-anchor="middle" class="city-label">{scene.smallLabel}</text>
    <text x="574" y="482" text-anchor="middle" class="city-label">{scene.largeLabel}</text>
  </svg>
</div>

<style>
  .dot-scene {
    position: relative;
    width: 100%;
    height: 100%;
    overflow: visible;
  }

  svg {
    width: 100%;
    height: 100%;
    display: block;
    overflow: visible;
  }

  .dot {
    transition:
      fill 240ms ease,
      opacity 240ms ease;
  }

  .city-label {
    fill: var(--ink);
    font-family: Arial, sans-serif;
    font-size: 23px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  @media (max-width: 720px) {
    .city-label {
      font-size: 19px;
    }
  }
</style>
