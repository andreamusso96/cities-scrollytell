<script lang="ts">
  import type { FutureDistributionScene } from "./types";

  export let scene: FutureDistributionScene;

  const chart = {
    baselineY: 510,
    blockHeight: 20,
    blockGap: 6,
    blockWidth: 118,
    xPositions: [80, 250, 420, 590]
  };

  function futureY(baseCount: number, futureIndex: number) {
    return (
      chart.baselineY -
      (baseCount + futureIndex + 1) * chart.blockHeight -
      (baseCount + futureIndex) * chart.blockGap
    );
  }
</script>

<div class="future-scene">
  <svg
    viewBox="0 0 800 600"
    role="img"
    aria-label="Four urban size bins with alternate future population distributions"
    preserveAspectRatio="xMidYMid meet"
  >
    <g>
      <line x1="62" y1="510" x2="726" y2="510" stroke="#1c232b" stroke-width="2"></line>
      <line x1="62" y1="96" x2="62" y2="510" stroke="#1c232b" stroke-width="2"></line>

      <text x="62" y="56" class="axis-label">Urban population by city-size bin</text>

      {#each scene.baseCounts as baseCount, binIndex (binIndex)}
        {#each Array.from({ length: baseCount }) as _, blockIndex (blockIndex)}
          <rect
            class="block"
            x={chart.xPositions[binIndex]}
            y={futureY(0, blockIndex)}
            width={chart.blockWidth}
            height={chart.blockHeight}
            rx="4"
            fill="#2d3844"
            opacity="1"
          ></rect>
        {/each}

        {#each Array.from({ length: scene.maxFutureByBin[binIndex] ?? 0 }) as _, futureIndex (futureIndex)}
          <rect
            class="block"
            x={chart.xPositions[binIndex]}
            y={futureY(scene.baseCounts[binIndex], futureIndex)}
            width={chart.blockWidth}
            height={chart.blockHeight}
            rx="4"
            fill={scene.futureColor}
            opacity={futureIndex < scene.futureCounts[binIndex] ? 1 : 0}
          ></rect>
        {/each}
      {/each}

      {#each scene.bins as bin, index (bin.label)}
        <text x={chart.xPositions[index] + chart.blockWidth / 2} y="560" text-anchor="middle" class="bin-label">
          {bin.label}
        </text>
        <text x={chart.xPositions[index] + chart.blockWidth / 2} y="584" text-anchor="middle" class="bin-sub">
          {bin.sublabel}
        </text>
      {/each}
    </g>
  </svg>
</div>

<style>
  .future-scene {
    position: relative;
    width: 100%;
    height: 100%;
  }

  svg {
    width: 100%;
    height: 100%;
    display: block;
  }

  .axis-label {
    fill: var(--ink);
    font-family: Arial, sans-serif;
    font-size: 24px;
    font-weight: 700;
    letter-spacing: 0.04em;
  }

  .bin-label {
    fill: var(--ink);
    font-family: Arial, sans-serif;
    font-size: 24px;
    font-weight: 700;
  }

  .bin-sub {
    fill: var(--muted);
    font-family: Arial, sans-serif;
    font-size: 17px;
    font-weight: 700;
  }

  .block {
    transition:
      y 380ms cubic-bezier(0.16, 1, 0.3, 1),
      fill 260ms ease,
      opacity 260ms ease;
  }

  @media (max-width: 720px) {
    .axis-label {
      font-size: 30px;
    }

    .bin-label {
      font-size: 30px;
    }

    .bin-sub {
      font-size: 18px;
    }
  }
</style>
