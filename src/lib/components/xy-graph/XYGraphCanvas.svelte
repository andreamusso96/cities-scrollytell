<script lang="ts">
  import type {
    XYAxis,
    XYCurveAnnotation,
    XYGraph,
    XYLine,
    XYMargins,
    XYPoint,
    XYScaleType,
    XYTextAnchor
  } from "./types";

  const VIEW_WIDTH = 800;
  const VIEW_HEIGHT = 600;
  const DEFAULT_MARGINS: XYMargins = {
    top: 102,
    right: 42,
    bottom: 132,
    left: 128
  };

  export let graph: XYGraph;

  const clamp = (value: number, min = 0, max = 1) => Math.min(Math.max(value, min), max);

  function mergeMargins(margins?: Partial<XYMargins>): XYMargins {
    return { ...DEFAULT_MARGINS, ...margins };
  }

  function normalizeValue(value: number, domain: [number, number], scale: XYScaleType) {
    if (scale === "log") {
      const safeMin = Math.max(domain[0], 1e-6);
      const safeMax = Math.max(domain[1], safeMin * 10);
      const safeValue = Math.min(Math.max(value, safeMin), safeMax);
      const minLog = Math.log10(safeMin);
      const maxLog = Math.log10(safeMax);
      return (Math.log10(safeValue) - minLog) / (maxLog - minLog);
    }

    return (value - domain[0]) / (domain[1] - domain[0]);
  }

  function scaleX(value: number, axis: XYAxis, margins: XYMargins) {
    const left = margins.left;
    const right = VIEW_WIDTH - margins.right;
    return left + normalizeValue(value, axis.domain, axis.scale ?? "linear") * (right - left);
  }

  function scaleY(value: number, axis: XYAxis, margins: XYMargins) {
    const top = margins.top;
    const bottom = VIEW_HEIGHT - margins.bottom;
    return bottom - normalizeValue(value, axis.domain, axis.scale ?? "linear") * (bottom - top);
  }

  function pointDistance(a: { x: number; y: number }, b: { x: number; y: number }) {
    const dx = b.x - a.x;
    const dy = b.y - a.y;
    return Math.sqrt(dx * dx + dy * dy);
  }

  function linePath(points: XYPoint[], xAxis: XYAxis, yAxis: XYAxis, margins: XYMargins) {
    if (points.length === 0) {
      return "";
    }

    return points
      .map((point, index) => {
        const x = scaleX(point.x, xAxis, margins).toFixed(1);
        const y = scaleY(point.y, yAxis, margins).toFixed(1);
        return `${index === 0 ? "M" : "L"} ${x} ${y}`;
      })
      .join(" ");
  }

  function lineLength(points: XYPoint[], xAxis: XYAxis, yAxis: XYAxis, margins: XYMargins) {
    if (points.length < 2) {
      return 0;
    }

    let total = 0;

    for (let index = 1; index < points.length; index += 1) {
      total += pointDistance(
        {
          x: scaleX(points[index - 1].x, xAxis, margins),
          y: scaleY(points[index - 1].y, yAxis, margins)
        },
        {
          x: scaleX(points[index].x, xAxis, margins),
          y: scaleY(points[index].y, yAxis, margins)
        }
      );
    }

    return total;
  }

  function lineOpacity(line: XYLine) {
    const drawTo = clamp(line.drawTo ?? 1);
    if (drawTo <= 0) {
      return 0;
    }

    return line.opacity ?? 1;
  }

  function anchorValue(anchor?: XYTextAnchor) {
    return anchor ?? "middle";
  }

  function estimateTextWidth(text: string, fontSize: number) {
    return text.length * fontSize * 0.62;
  }

  function fitHorizontalText(x: number, anchor: XYTextAnchor, text: string, fontSize: number) {
    const estimate = estimateTextWidth(text, fontSize);
    const minX = 10;
    const maxX = VIEW_WIDTH - 10;

    if (anchor === "start" && x + estimate > maxX) {
      return {
        x: Math.min(x, maxX),
        anchor: "end" as XYTextAnchor
      };
    }

    if (anchor === "end" && x - estimate < minX) {
      return {
        x: Math.max(x, minX),
        anchor: "start" as XYTextAnchor
      };
    }

    if (anchor === "middle") {
      const half = estimate / 2;
      return {
        x: Math.min(Math.max(x, minX + half), maxX - half),
        anchor
      };
    }

    return { x, anchor };
  }

  function findClosestPointIndex(points: XYPoint[], target: XYPoint) {
    let nearestIndex = 0;
    let nearestDistance = Number.POSITIVE_INFINITY;

    points.forEach((point, index) => {
      const dx = point.x - target.x;
      const dy = point.y - target.y;
      const distance = dx * dx + dy * dy;

      if (distance < nearestDistance) {
        nearestDistance = distance;
        nearestIndex = index;
      }
    });

    return nearestIndex;
  }

  function annotationOpacity(drawTo: number, revealAt: number) {
    return clamp((drawTo - revealAt) / 0.08, 0, 1);
  }

  $: margins = mergeMargins(graph.margins);
  $: plotLeft = margins.left;
  $: plotRight = VIEW_WIDTH - margins.right;
  $: plotTop = margins.top;
  $: plotBottom = VIEW_HEIGHT - margins.bottom;
  $: xAxisOpacity = clamp(graph.xAxis.opacity ?? 1);
  $: yAxisOpacity = clamp(graph.yAxis.opacity ?? 1);
  $: renderedLines = graph.lines.map((line) => {
    const scaledPoints = line.points.map((point) => ({
      rawX: point.x,
      rawY: point.y,
      x: scaleX(point.x, graph.xAxis, margins),
      y: scaleY(point.y, graph.yAxis, margins)
    }));
    const cumulativeRatios: number[] = [];
    const length = lineLength(line.points, graph.xAxis, graph.yAxis, margins);
    let runningLength = 0;

    scaledPoints.forEach((point, index) => {
      if (index > 0) {
        runningLength += pointDistance(scaledPoints[index - 1], point);
      }

      cumulativeRatios.push(length > 0 ? runningLength / length : 0);
    });

    return {
      ...line,
      drawTo: clamp(line.drawTo ?? 1),
      d: linePath(line.points, graph.xAxis, graph.yAxis, margins),
      length,
      scaledPoints,
      cumulativeRatios
    };
  });
  $: renderedLineMap = new Map(renderedLines.map((line) => [line.id, line]));
  $: renderedAnnotations = (graph.annotations ?? []).flatMap((annotation) => {
    const line = renderedLineMap.get(annotation.lineId);

    if (!line || line.scaledPoints.length === 0) {
      return [];
    }

    const pointIndex = findClosestPointIndex(line.points, annotation.point);
    const point = line.scaledPoints[pointIndex];
    const baseRevealAt = annotation.revealAt ?? line.cumulativeRatios[pointIndex] ?? 0;
    const revealAt =
      pointIndex === line.points.length - 1 ? Math.min(baseRevealAt, 0.94) : baseRevealAt;
    const opacity = annotationOpacity(line.drawTo, revealAt) * lineOpacity(line);

    if (opacity <= 0) {
      return [];
    }

    const direction = annotation.orientation === "below" ? 1 : -1;
    const dx = annotation.dx ?? 0;
    const blockOffset = annotation.dy ?? (annotation.orientation === "below" ? 62 : 56);
    const stemOffset = Math.max(blockOffset - 18, 18);
    const textX = point.x + dx;
    const stemY = point.y + direction * stemOffset;
    const titleY = point.y + direction * blockOffset;
    const subtitleY = annotation.subtitle
      ? titleY + (annotation.orientation === "below" ? 24 : 24)
      : undefined;

    return [
      {
        ...annotation,
        color: line.color,
        x: point.x,
        y: point.y,
        textX,
        stemX: textX,
        stemY,
        titleY,
        subtitleY,
        opacity,
        anchor: anchorValue(annotation.align)
      }
    ];
  });
  $: renderedEndpointLabels = renderedLines.flatMap((line) => {
    if (!line.endLabel || line.scaledPoints.length === 0) {
      return [];
    }

    const lastPoint = line.scaledPoints[line.scaledPoints.length - 1];
    const revealAt = line.endLabel.revealAt ?? 0.96;
    const opacity = annotationOpacity(line.drawTo, revealAt) * lineOpacity(line);

    if (opacity <= 0) {
      return [];
    }

    const placement = line.endLabel.placement ?? "point";
    const desiredAnchor = anchorValue(line.endLabel.anchor ?? "start");
    const fitted =
      placement === "right-column"
        ? fitHorizontalText(
            plotRight + (line.endLabel.dx ?? 12),
            anchorValue(line.endLabel.anchor ?? "start"),
            line.endLabel.text,
            26
          )
        : fitHorizontalText(
            lastPoint.x + (line.endLabel.dx ?? 16),
            desiredAnchor,
            line.endLabel.text,
            26
          );

    return [
      {
        id: `${line.id}-end-label`,
        text: line.endLabel.text,
        color: line.color,
        x: fitted.x,
        y: lastPoint.y + (line.endLabel.dy ?? 6),
        anchor: fitted.anchor,
        opacity
      }
    ];
  });
</script>

<svg
  viewBox={`0 0 ${VIEW_WIDTH} ${VIEW_HEIGHT}`}
  role="img"
  aria-label="XY graph"
  preserveAspectRatio="xMidYMid meet"
>
  <g class="axis-group" style:opacity={xAxisOpacity}>
    <line class="axis-line" x1={plotLeft} y1={plotBottom} x2={plotRight} y2={plotBottom}></line>

    {#each graph.xAxis.ticks as tick}
      {@const x = scaleX(tick.value, graph.xAxis, margins)}
      <line class="tick-line" x1={x} y1={plotBottom} x2={x} y2={plotBottom + 12}></line>
      <text class="tick-text" x={x} y={plotBottom + 50} text-anchor="middle">{tick.label}</text>
    {/each}

    {#if graph.xAxis.label}
      <text class="axis-label x-label" x={(plotLeft + plotRight) / 2} y={VIEW_HEIGHT - 28} text-anchor="middle">
        {graph.xAxis.label}
      </text>
    {/if}
  </g>

  <g class="axis-group" style:opacity={yAxisOpacity}>
    <line class="axis-line" x1={plotLeft} y1={plotTop} x2={plotLeft} y2={plotBottom}></line>

    {#each graph.yAxis.ticks as tick}
      {@const y = scaleY(tick.value, graph.yAxis, margins)}
      <line class="tick-line" x1={plotLeft - 12} y1={y} x2={plotLeft} y2={y}></line>
      <text class="tick-text" x={plotLeft - 24} y={y + 9} text-anchor="end">{tick.label}</text>
    {/each}

    {#if graph.yAxis.label}
      <text class="axis-label y-label" x={plotLeft} y={plotTop - 32} text-anchor="start">
        {graph.yAxis.label}
      </text>
    {/if}
  </g>

  <g class="line-group">
    {#each renderedLines as line (line.id)}
      <path
        class="line-path"
        d={line.d}
        fill="none"
        stroke={line.color}
        stroke-width={line.width ?? 5}
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-dasharray={line.length}
        stroke-dashoffset={line.length * (1 - line.drawTo)}
        style:opacity={lineOpacity(line)}
      ></path>
    {/each}
  </g>

  <g class="annotation-layer">
    {#each renderedAnnotations as annotation (annotation.id)}
      <line
        class="annotation-stem"
        x1={annotation.x}
        y1={annotation.y}
        x2={annotation.stemX}
        y2={annotation.stemY}
        stroke={annotation.color}
        style:opacity={annotation.opacity * 0.55}
      ></line>
      <circle
        class="annotation-dot"
        cx={annotation.x}
        cy={annotation.y}
        r="7"
        fill={annotation.color}
        style:opacity={annotation.opacity}
      ></circle>
      <text
        class="annotation-text"
        x={annotation.textX}
        y={annotation.titleY}
        text-anchor={annotation.anchor}
        style:opacity={annotation.opacity}
      >
        {annotation.title}
      </text>
      {#if annotation.subtitle}
        <text
          class="annotation-sub"
          x={annotation.textX}
          y={annotation.subtitleY}
          text-anchor={annotation.anchor}
          style:opacity={annotation.opacity}
        >
          {annotation.subtitle}
        </text>
      {/if}
    {/each}
  </g>

  <g class="endpoint-layer">
    {#each renderedEndpointLabels as label (label.id)}
      <text
        class="endpoint-label"
        x={label.x}
        y={label.y}
        text-anchor={label.anchor}
        fill={label.color}
        style:opacity={label.opacity}
      >
        {label.text}
      </text>
    {/each}
  </g>
</svg>

<style>
  svg {
    width: 100%;
    height: 100%;
    display: block;
  }

  .axis-group,
  .line-path,
  .annotation-stem,
  .annotation-dot,
  .annotation-text,
  .annotation-sub,
  .endpoint-label {
    transition: opacity 180ms linear, stroke-dashoffset 120ms linear;
  }

  .axis-line {
    stroke: #2c3946;
    stroke-width: 2;
  }

  .tick-line {
    stroke: #2c3946;
    stroke-width: 1.5;
  }

  .axis-label,
  .tick-text {
    fill: #f5efe5;
    font-family: Arial, sans-serif;
    font-weight: 700;
  }

  .axis-label {
    font-size: 30px;
  }

  .tick-text {
    font-size: 28px;
  }

  .annotation-text,
  .annotation-sub,
  .endpoint-label {
    font-family: Arial, sans-serif;
    font-weight: 800;
  }

  .annotation-text {
    fill: #f5efe5;
    font-size: 24px;
  }

  .annotation-sub {
    fill: #b8ada0;
    font-size: 20px;
    font-weight: 700;
  }

  .endpoint-label {
    font-size: 26px;
  }
</style>
