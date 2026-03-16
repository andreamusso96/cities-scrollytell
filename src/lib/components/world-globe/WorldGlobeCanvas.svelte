<script lang="ts">
  import type { WorldGlobeScene } from "./types";

  export let scene: WorldGlobeScene;
  export let activeStepIndex = 0;
  export let stepProgress = 0;

  const globe = {
    cx: 400,
    cy: 302,
    r: 166,
    lat0: -12
  };

  function clamp(value: number, min = 0, max = 1) {
    return Math.min(Math.max(value, min), max);
  }

  function rangeProgress(progress: number, start: number, end: number) {
    return clamp((progress - start) / (end - start), 0, 1);
  }

  function mulberry32(seed: number) {
    return function () {
      let t = (seed += 0x6d2b79f5);
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  function degToRad(value: number) {
    return (value * Math.PI) / 180;
  }

  function projectPoint(lon: number, lat: number, rotation: number) {
    const lambda = degToRad(lon - rotation);
    const phi = degToRad(lat);
    const phi0 = degToRad(globe.lat0);
    const cosPhi = Math.cos(phi);
    const sinPhi = Math.sin(phi);
    const cosPhi0 = Math.cos(phi0);
    const sinPhi0 = Math.sin(phi0);
    const cosLambda = Math.cos(lambda);
    const sinLambda = Math.sin(lambda);

    const x = cosPhi * sinLambda;
    const y = cosPhi0 * sinPhi - sinPhi0 * cosPhi * cosLambda;
    const z = sinPhi0 * sinPhi + cosPhi0 * cosPhi * cosLambda;

    return {
      x: globe.cx + globe.r * x,
      y: globe.cy - globe.r * y,
      z,
      visible: z > 0
    };
  }

  function buildLinePath(
    points: Array<{ x: number; y: number; visible: boolean }>
  ) {
    const segments: Array<Array<{ x: number; y: number }>> = [];
    let current: Array<{ x: number; y: number }> = [];

    points.forEach((point) => {
      if (point.visible) {
        current.push(point);
      } else if (current.length) {
        segments.push(current);
        current = [];
      }
    });

    if (current.length) {
      segments.push(current);
    }

    return segments
      .filter((segment) => segment.length > 1)
      .map((segment) => {
        const first = segment[0];
        const rest = segment
          .slice(1)
          .map((point) => `L ${point.x.toFixed(1)} ${point.y.toFixed(1)}`)
          .join(" ");

        return `M ${first.x.toFixed(1)} ${first.y.toFixed(1)} ${rest}`;
      });
  }

  function createCityPolygons() {
    const centers = [
      [-122.4, 37.8], [-118.25, 34.05], [-99.13, 19.43], [-74.0, 40.7], [-87.62, 41.88],
      [-46.63, -23.55], [-58.38, -34.6], [-70.66, -33.45], [-77.04, -12.05], [-74.08, 4.61],
      [-0.12, 51.5], [2.35, 48.86], [13.4, 52.52], [12.49, 41.89], [37.62, 55.75],
      [31.24, 30.04], [3.38, 6.52], [28.04, -26.2], [36.82, -1.29], [-7.59, 33.57],
      [77.21, 28.61], [72.88, 19.08], [88.36, 22.57], [67.01, 24.86], [90.41, 23.81],
      [100.5, 13.75], [106.82, -6.2], [121.0, 14.6], [103.82, 1.35], [114.17, 22.32],
      [121.47, 31.23], [116.4, 39.9], [139.69, 35.69], [126.98, 37.56], [151.21, -33.87],
      [144.96, -37.81], [174.76, -36.85], [55.27, 25.2], [51.39, 35.69], [44.37, 33.31]
    ];

    const rand = mulberry32(12);
    const polygons: Array<{ id: string; points: Array<[number, number]> }> = [];

    centers.forEach(([lon, lat], centerIndex) => {
      const count = 4 + Math.floor(rand() * 4);

      for (let i = 0; i < count; i += 1) {
        const jitterLon = lon + (rand() - 0.5) * 7.5;
        const jitterLat = lat + (rand() - 0.5) * 5.5;
        const radiusLon = 1.2 + rand() * 1.7;
        const radiusLat = 0.7 + rand() * 1.2;
        const points: Array<[number, number]> = [];
        const sides = 5 + Math.floor(rand() * 3);

        for (let side = 0; side < sides; side += 1) {
          const angle = (Math.PI * 2 * side) / sides;
          const wobble = 0.82 + rand() * 0.45;
          points.push([
            jitterLon + Math.cos(angle) * radiusLon * wobble,
            jitterLat + Math.sin(angle) * radiusLat * wobble
          ]);
        }

        polygons.push({
          id: `${centerIndex}-${i}`,
          points
        });
      }
    });

    return polygons;
  }

  const polygons = createCityPolygons();

  $: sceneProgress = clamp((activeStepIndex + stepProgress) / scene.stepCount, 0, 1);
  $: rotation = -165 + sceneProgress * 330;

  $: countriesProgress = rangeProgress(sceneProgress, 0.08, 0.25);
  $: populationProgress = rangeProgress(sceneProgress, 0.25, 0.42);
  $: observationsProgress = rangeProgress(sceneProgress, 0.42, 0.62);
  $: yearsProgress = rangeProgress(sceneProgress, 0.62, 0.82);

  $: stats = {
    countries: Math.round(99 * countriesProgress),
    population: Math.round(94 * populationProgress),
    observations: Math.round(1604593 * observationsProgress).toLocaleString("en-US"),
    years: `1975-${1975 + Math.round((2025 - 1975) * yearsProgress)}`
  };

  $: cardVisible = {
    countries: sceneProgress >= 0.08,
    population: sceneProgress >= 0.25,
    observations: sceneProgress >= 0.42,
    years: sceneProgress >= 0.62
  };

  $: cardActive = {
    countries: countriesProgress > 0 && countriesProgress < 1,
    population: populationProgress > 0 && populationProgress < 1,
    observations: observationsProgress > 0 && observationsProgress < 1,
    years: yearsProgress > 0 && yearsProgress < 1
  };

  $: {
    const meridians: Array<string> = [];
    const parallels: Array<string> = [];
    const back: string[] = [];
    const front: string[] = [];

    for (let lon = -150; lon <= 180; lon += 30) {
      const samples = [];
      for (let lat = -80; lat <= 80; lat += 4) {
        samples.push(projectPoint(lon, lat, rotation));
      }
      meridians.push(...buildLinePath(samples.map((point) => ({ ...point, visible: point.z > 0 }))));
      back.push(
        ...buildLinePath(samples.map((point) => ({ ...point, visible: point.z > -0.35 && point.z <= 0 })))
      );
    }

    for (let lat = -60; lat <= 60; lat += 30) {
      const samples = [];
      for (let lon = -180; lon <= 180; lon += 4) {
        samples.push(projectPoint(lon, lat, rotation));
      }
      parallels.push(...buildLinePath(samples.map((point) => ({ ...point, visible: point.z > 0 }))));
      back.push(
        ...buildLinePath(samples.map((point) => ({ ...point, visible: point.z > -0.35 && point.z <= 0 })))
      );
    }

    graticuleBackPaths = back;
    graticuleFrontPaths = [...meridians, ...parallels];
  }

  let graticuleBackPaths: string[] = [];
  let graticuleFrontPaths: string[] = [];

  $: polygonRender = polygons
    .map((polygon) => {
      const projected = polygon.points.map(([lon, lat]) => projectPoint(lon, lat, rotation));
      const avgZ = projected.reduce((sum, point) => sum + point.z, 0) / projected.length;

      if (avgZ <= 0.05) {
        return null;
      }

      const path =
        projected
          .map((point, index) => `${index === 0 ? "M" : "L"} ${point.x.toFixed(1)} ${point.y.toFixed(1)}`)
          .join(" ") + " Z";

      const opacity = clamp((avgZ - 0.03) / 0.92, 0.18, 1);

      return {
        id: polygon.id,
        path,
        opacity,
        shadowOpacity: opacity * 0.6
      };
    })
    .filter(Boolean) as Array<{ id: string; path: string; opacity: number; shadowOpacity: number }>;
</script>

<div class="globe-scene">
  <div class="stats-layer" class:visible={cardVisible.countries}>
    <div class="stats-row top">
      <div class:visible={cardVisible.countries} class:active={cardActive.countries} class="stat-card">
        <span class="stat-value">{stats.countries}</span>
        <span class="stat-label">countries</span>
      </div>
      <div class:visible={cardVisible.population} class:active={cardActive.population} class="stat-card">
        <span class="stat-value">{stats.population}%</span>
        <span class="stat-label">of world population</span>
      </div>
    </div>

    <div class="stats-row bottom">
      <div class:visible={cardVisible.observations} class:active={cardActive.observations} class="stat-card">
        <span class="stat-value small">{stats.observations}</span>
        <span class="stat-label">city-year observations</span>
      </div>
      <div class:visible={cardVisible.years} class:active={cardActive.years} class="stat-card">
        <span class="stat-value">{stats.years}</span>
        <span class="stat-label">panel window</span>
      </div>
    </div>
  </div>

  <svg
    viewBox="0 0 800 600"
    role="img"
    aria-label="Rotating globe with many city polygons"
    preserveAspectRatio="xMidYMid meet"
  >
    <defs>
      <radialGradient id="sphereFill" cx="42%" cy="36%" r="70%">
        <stop offset="0%" stop-color="#12202b"></stop>
        <stop offset="55%" stop-color="#0a131a"></stop>
        <stop offset="100%" stop-color="#070c11"></stop>
      </radialGradient>
      <radialGradient id="atmosphere" cx="50%" cy="48%" r="52%">
        <stop offset="72%" stop-color="rgba(103, 224, 204, 0)"></stop>
        <stop offset="92%" stop-color="rgba(103, 224, 204, 0.08)"></stop>
        <stop offset="100%" stop-color="rgba(103, 224, 204, 0.18)"></stop>
      </radialGradient>
      <clipPath id="globe-clip">
        <circle cx={globe.cx} cy={globe.cy} r={globe.r}></circle>
      </clipPath>
    </defs>

    <rect x="0" y="0" width="800" height="600" fill="#0f141c"></rect>
    <circle cx={globe.cx} cy={globe.cy} r={globe.r + 12} fill="rgba(0, 0, 0, 0.2)"></circle>
    <circle
      cx={globe.cx}
      cy={globe.cy}
      r={globe.r}
      fill="url(#sphereFill)"
      stroke="#16222c"
      stroke-width="2"
    ></circle>
    <circle cx={globe.cx} cy={globe.cy} r={globe.r + 6} fill="url(#atmosphere)" opacity="0.9"></circle>

    <g clip-path="url(#globe-clip)">
      <g opacity="0.32">
        {#each graticuleBackPaths as path, index (path + index)}
          <path d={path} fill="none" stroke="#1e2a34" stroke-width="1.2"></path>
        {/each}
      </g>

      <g opacity="0.18">
        {#each polygonRender as polygon (polygon.id)}
          <path
            d={polygon.path}
            fill="rgba(0,0,0,0.35)"
            transform="translate(0 2.5)"
            opacity={polygon.shadowOpacity}
          ></path>
        {/each}
      </g>

      <g>
        {#each polygonRender as polygon (polygon.id)}
          <path
            d={polygon.path}
            fill="rgba(103, 224, 204, 0.24)"
            stroke="rgba(103, 224, 204, 0.8)"
            stroke-width="1.2"
            opacity={polygon.opacity}
          ></path>
        {/each}
      </g>

      <g opacity="0.72">
        {#each graticuleFrontPaths as path, index (path + index)}
          <path d={path} fill="none" stroke="#283844" stroke-width="1.3"></path>
        {/each}
      </g>
    </g>

    <circle
      cx={globe.cx}
      cy={globe.cy}
      r={globe.r}
      fill="none"
      stroke="rgba(255,255,255,0.05)"
      stroke-width="1.5"
    ></circle>
  </svg>
</div>

<style>
  .globe-scene {
    position: relative;
    width: 100%;
    height: 100%;
    overflow: hidden;
  }

  svg {
    width: 100%;
    height: 100%;
    display: block;
  }

  .stats-layer {
    position: absolute;
    inset: 0;
    z-index: 2;
    opacity: 0;
    pointer-events: none;
    transition: opacity 220ms ease;
  }

  .stats-layer.visible {
    opacity: 1;
  }

  .stats-row {
    position: absolute;
    left: 26px;
    right: 26px;
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 6px;
  }

  .stats-row.top {
    top: 8px;
  }

  .stats-row.bottom {
    bottom: 6px;
  }

  .stat-card {
    min-width: 0;
    padding: 7px 8px 8px;
    border-radius: 11px;
    background: transparent;
    border: 1px solid transparent;
    opacity: 0;
    visibility: hidden;
    transform: translateY(8px);
    transition:
      opacity 220ms ease,
      border-color 220ms ease,
      background-color 220ms ease,
      transform 220ms ease;
  }

  .stat-card.visible {
    visibility: visible;
    background: rgba(10, 13, 17, 0.78);
    border-color: rgba(255, 255, 255, 0.06);
    opacity: 1;
    transform: translateY(0);
  }

  .stat-card.active {
    border-color: rgba(103, 224, 204, 0.28);
    background: rgba(12, 18, 24, 0.96);
  }

  .stat-value {
    display: block;
    font-family: Arial, sans-serif;
    font-size: 22px;
    font-weight: 800;
    line-height: 1;
    letter-spacing: -0.03em;
  }

  .stat-value.small {
    font-size: 18px;
  }

  .stat-label {
    display: block;
    margin-top: 4px;
    color: var(--muted);
    font-family: Arial, sans-serif;
    font-size: 10px;
    font-weight: 700;
    line-height: 1.2;
    text-transform: uppercase;
  }

  @media (max-width: 720px) {
    .stats-row {
      left: 18px;
      right: 18px;
    }

    .stat-card {
      padding: 7px 7px 8px;
    }

    .stat-value {
      font-size: 23px;
    }

    .stat-value.small {
      font-size: 18px;
    }

    .stat-label {
      font-size: 10px;
    }
  }
</style>
