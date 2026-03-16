<script lang="ts">
  import type {
    LayeredMapLayer,
    LayeredMapPathItem,
    LayeredMapScene,
    LayeredMapTextAnchor
  } from "./types";

  export let map: LayeredMapScene;

  function clamp(value: number, min = 0, max = 1) {
    return Math.min(Math.max(value, min), max);
  }

  function layerOpacity(layer: LayeredMapLayer) {
    return clamp(layer.opacity ?? 1);
  }

  function textAnchor(anchor?: LayeredMapTextAnchor) {
    return anchor ?? "middle";
  }

  function layerTransform(layer: LayeredMapLayer, scene: LayeredMapScene) {
    const translateX = layer.translateX ?? 0;
    const translateY = layer.translateY ?? 0;
    const scale = layer.scale ?? 1;

    if (scale === 1) {
      return translateX || translateY ? `translate(${translateX} ${translateY})` : undefined;
    }

    const [minX, minY, width, height] = scene.viewport.viewBox;
    const originX = layer.originX ?? minX + width / 2;
    const originY = layer.originY ?? minY + height / 2;

    return [
      `translate(${translateX} ${translateY})`,
      `translate(${originX} ${originY})`,
      `scale(${scale})`,
      `translate(${-originX} ${-originY})`
    ].join(" ");
  }

  function pathOpacity(item: LayeredMapPathItem) {
    return clamp(item.opacity ?? 1);
  }

  function normalizedDrawTo(item: LayeredMapPathItem) {
    return item.drawTo == null ? undefined : clamp(item.drawTo);
  }
</script>

<svg
  viewBox={map.viewport.viewBox.join(" ")}
  role="img"
  aria-label="Layered map scene"
  preserveAspectRatio={map.viewport.preserveAspectRatio ?? "xMidYMid meet"}
>
  {#if map.viewport.background}
    <rect
      x={map.viewport.viewBox[0]}
      y={map.viewport.viewBox[1]}
      width={map.viewport.viewBox[2]}
      height={map.viewport.viewBox[3]}
      fill={map.viewport.background}
    ></rect>
  {/if}

  {#each map.layers as layer (layer.id)}
    <g transform={layerTransform(layer, map)} style:opacity={layerOpacity(layer)}>
      {#if layer.kind === "image"}
        <image
          href={layer.href}
          x={layer.x}
          y={layer.y}
          width={layer.width}
          height={layer.height}
          preserveAspectRatio={layer.preserveAspectRatio ?? "xMidYMid slice"}
        ></image>
      {:else if layer.kind === "paths"}
        {#each layer.items as item, index (item.id ?? `${layer.id}-${index}`)}
          {@const drawTo = normalizedDrawTo(item)}
          <path
            d={item.d}
            fill={item.fill ?? "none"}
            fill-opacity={item.fillOpacity ?? (item.fill ? 1 : 0)}
            stroke={item.stroke ?? "none"}
            stroke-opacity={item.strokeOpacity ?? (item.stroke ? 1 : 0)}
            stroke-width={item.strokeWidth ?? 1}
            stroke-linecap={item.lineCap ?? "round"}
            stroke-linejoin={item.lineJoin ?? "round"}
            pathLength={drawTo != null ? 1 : undefined}
            stroke-dasharray={drawTo != null ? 1 : undefined}
            stroke-dashoffset={drawTo != null ? 1 - drawTo : undefined}
            style:opacity={pathOpacity(item)}
          ></path>
        {/each}
      {:else if layer.kind === "rects"}
        {#each layer.items as item, index (item.id ?? `${layer.id}-${index}`)}
          <rect
            x={item.x}
            y={item.y}
            width={item.width}
            height={item.height}
            rx={item.rx}
            ry={item.ry}
            fill={item.fill ?? "none"}
            fill-opacity={item.fillOpacity ?? (item.fill ? 1 : 0)}
            stroke={item.stroke ?? "none"}
            stroke-opacity={item.strokeOpacity ?? (item.stroke ? 1 : 0)}
            stroke-width={item.strokeWidth ?? 1}
            style:opacity={clamp(item.opacity ?? 1)}
          ></rect>
        {/each}
      {:else if layer.kind === "labels"}
        {#each layer.items as item, index (item.id ?? `${layer.id}-${index}`)}
          <text
            x={item.x}
            y={item.y}
            fill={item.fill ?? "#f5efe5"}
            font-size={item.fontSize ?? 18}
            font-weight={item.fontWeight ?? 700}
            letter-spacing={item.letterSpacing}
            text-anchor={textAnchor(item.anchor)}
            style:opacity={clamp(item.opacity ?? 1)}
          >
            {item.text}
          </text>
        {/each}
      {/if}
    </g>
  {/each}
</svg>

<style>
  svg {
    width: 100%;
    height: 100%;
    display: block;
  }

  image,
  path,
  rect,
  text,
  g {
    transition:
      opacity 220ms linear,
      stroke-dashoffset 160ms linear,
      transform 260ms cubic-bezier(0.16, 1, 0.3, 1);
  }

  text {
    font-family: Arial, sans-serif;
  }
</style>
