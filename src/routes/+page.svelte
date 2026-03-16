<script lang="ts">
  import LayeredMapCanvas from "$lib/components/layered-map/LayeredMapCanvas.svelte";
  import type { LayeredMapScene } from "$lib/components/layered-map/types";
  import ProseSection from "$lib/components/ProseSection.svelte";
  import StickyScene from "$lib/components/StickyScene.svelte";
  import XYGraphCanvas from "$lib/components/xy-graph/XYGraphCanvas.svelte";
  import type { XYGraph } from "$lib/components/xy-graph/types";

  type SceneKind = "xy-world" | "xy-scenarios" | "map-paris" | "map-ghsl" | "map-allocation";

  type LegendItem = {
    label: string;
    color: string;
    shape?: "line" | "fill" | "outline";
  };

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
    },
    {
      heading: "Prose scene 4",
      paragraphs: [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam pulvinar leo sed lectus egestas, in interdum mi feugiat. Proin aliquet faucibus nibh, et facilisis tellus ultricies vitae.",
        "Nullam et semper ligula. Sed placerat tempus nibh, non consequat tellus gravida eu. Integer egestas, nibh ac vestibulum interdum, lectus lectus efficitur sem, vel vulputate nisl justo ac ex.",
        "Vestibulum mattis turpis vitae sem accumsan, sit amet euismod elit rhoncus. Donec consequat velit in eros tincidunt, vitae posuere augue porttitor."
      ]
    },
    {
      heading: "Prose scene 5",
      paragraphs: [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer iaculis mi at mauris congue, in vulputate enim feugiat. Mauris pretium massa ac mauris efficitur, et feugiat velit interdum.",
        "Donec varius pretium lorem, in tincidunt purus faucibus vel. Phasellus sed mi vehicula, lacinia tortor vitae, tristique erat. Curabitur sed dui at erat tempus viverra.",
        "Morbi dictum, tortor sed varius tincidunt, justo justo tincidunt lectus, ac viverra nisi sapien et ipsum. Vivamus eget urna ac lectus porttitor posuere."
      ]
    },
    {
      heading: "Prose scene 6",
      paragraphs: [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, dui sed accumsan convallis, purus ipsum interdum orci, sit amet cursus justo mauris vitae lacus.",
        "Praesent mollis, nunc nec accumsan maximus, neque dolor congue odio, vel luctus mauris augue vitae massa. Integer aliquet dignissim augue, sed tincidunt justo pulvinar at.",
        "Mauris blandit augue sed varius vulputate. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Pellentesque sit amet libero a purus faucibus tincidunt."
      ]
    }
  ];

  const stickyScenes: Array<{
    id: string;
    kind: SceneKind;
    ariaLabel: string;
    pinDurationVh: number;
    tailHoldVh?: number;
    steps: Array<{
      id: string;
      kicker: string;
      title: string;
      body: string;
    }>;
  }> = [
    {
      id: "sticky-1",
      kind: "xy-world",
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
      kind: "xy-scenarios",
      ariaLabel: "Sticky test scene two",
      pinDurationVh: 320,
      steps: [
        { id: "step-a", kicker: "XY graph", title: "Load the x-axis again", body: "The second chart should teach the frame the same way: start with the horizontal axis only." },
        { id: "step-b", kicker: "XY graph", title: "Now add the y-axis", body: "Then fade in the vertical scale, keeping the same graph shell while the values change." },
        { id: "step-c", kicker: "XY graph", title: "Draw the first scenario", body: "One curve can draw first while the others stay hidden." },
        { id: "step-d", kicker: "XY graph", title: "Add the remaining lines", body: "Additional curves then draw into the same coordinate system without changing the canvas type." }
      ]
    },
    {
      id: "sticky-3",
      kind: "map-paris",
      ariaLabel: "Layered Paris boundary scene",
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
      id: "sticky-4",
      kind: "map-ghsl",
      ariaLabel: "Layered GHSL pipeline scene",
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
      id: "sticky-5",
      kind: "map-allocation",
      ariaLabel: "Layered population allocation scene",
      pinDurationVh: 360,
      tailHoldVh: 112,
      steps: [
        { id: "alloc-a", kicker: "Residential signal", title: "Estimate residential building heights", body: "Start from imagery again. Roof texture and shadow hint at how much residential volume each cell contains." },
        { id: "alloc-b", kicker: "Residential volume", title: "Turn the grid into a 3D residential volume map", body: "Bars rise where residential built volume is larger. This becomes the weight used for redistribution." },
        { id: "alloc-c", kicker: "Census redistribution", title: "Administrative totals are pushed back into the grid", body: "Each district total is split across its cells. More residential volume receives a larger population share." }
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

  const properBoundaryPath =
    "M 372 286 L 414 270 L 450 290 L 464 334 L 446 378 L 404 396 L 364 382 L 344 334 Z";
  const builtUpPath =
    "M 278 210 C 340 182, 446 186, 516 226 C 576 268, 600 352, 566 430 C 528 496, 426 534, 322 518 C 234 504, 184 438, 188 356 C 190 290, 222 236, 278 210 Z";
  const attractionPath =
    "M 178 134 C 258 94, 386 86, 520 120 C 618 154, 694 236, 716 340 C 740 452, 694 540, 608 592 C 520 646, 370 650, 252 612 C 160 582, 96 510, 82 402 C 68 286, 100 194, 178 134 Z";

  function svgDataUri(svg: string) {
    return `data:image/svg+xml;charset=UTF-8,${encodeURIComponent(svg)}`;
  }

  const parisSatelliteImage = svgDataUri(`
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
      <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#0b1117"/>
          <stop offset="100%" stop-color="#0d141b"/>
        </linearGradient>
        <filter id="blur" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="18"/>
        </filter>
      </defs>
      <rect width="800" height="600" fill="url(#bg)"/>
      <g opacity="0.92">
        <path d="M30 120 C200 70, 330 150, 470 120 S690 78, 770 132" fill="none" stroke="#18242e" stroke-width="12"/>
        <path d="M22 208 C172 168, 314 244, 468 224 S650 190, 778 240" fill="none" stroke="#14202a" stroke-width="14"/>
        <path d="M26 316 C172 274, 320 350, 468 326 S664 290, 780 346" fill="none" stroke="#18242e" stroke-width="10"/>
        <path d="M18 432 C164 390, 324 466, 476 440 S664 406, 782 458" fill="none" stroke="#131d26" stroke-width="13"/>
        <path d="M84 24 L168 576" stroke="#16222c" stroke-width="10"/>
        <path d="M248 10 L322 586" stroke="#111920" stroke-width="8"/>
        <path d="M432 14 L470 590" stroke="#16222c" stroke-width="10"/>
        <path d="M640 12 L592 586" stroke="#111920" stroke-width="8"/>
      </g>
      <g opacity="0.95">
        <path d="M340 78 C366 110, 366 164, 336 206 C312 240, 308 282, 336 322 C372 374, 428 390, 448 438 C460 468, 458 518, 438 570" fill="none" stroke="#6fa3e7" stroke-width="10" stroke-linecap="round"/>
        <path d="M354 96 C376 122, 376 162, 350 202 C328 236, 326 278, 352 316 C386 364, 434 384, 448 426 C456 454, 452 500, 434 548" fill="none" stroke="#8ac0ff" stroke-width="4" stroke-linecap="round" opacity="0.92"/>
      </g>
      <g opacity="0.62">
        <path d="M104 116 C154 78, 230 88, 274 130 C244 180, 174 194, 120 168 Z" fill="#15241f"/>
        <path d="M520 82 C590 62, 670 102, 694 166 C656 194, 584 204, 532 176 C510 150, 506 110, 520 82 Z" fill="#13231e"/>
        <path d="M566 420 C638 392, 706 434, 708 492 C676 528, 602 534, 558 506 C542 474, 542 438, 566 420 Z" fill="#14251f"/>
        <path d="M88 420 C148 394, 228 420, 248 480 C220 524, 150 540, 104 510 C82 478, 76 444, 88 420 Z" fill="#14241f"/>
      </g>
      <g opacity="0.2" filter="url(#blur)">
        <ellipse cx="402" cy="314" rx="108" ry="84" fill="#ffffff"/>
      </g>
      <g opacity="0.3">
        <path d="M120 236 L692 236" stroke="#1a2630" stroke-width="3" stroke-dasharray="8 12"/>
        <path d="M138 390 L680 390" stroke="#1a2630" stroke-width="3" stroke-dasharray="8 12"/>
        <path d="M232 140 L232 544" stroke="#1a2630" stroke-width="3" stroke-dasharray="8 12"/>
        <path d="M538 112 L538 560" stroke="#1a2630" stroke-width="3" stroke-dasharray="8 12"/>
      </g>
    </svg>
  `);

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

  const ghslGrid = {
    x: 175,
    y: 95,
    size: 450,
    cells: 15
  };

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

  function buildGhslCells() {
    const { x, y, size, cells } = ghslGrid;
    const cellSize = size / cells;
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
          x: x + col * cellSize,
          y: y + row * cellSize,
          cx: x + col * cellSize + cellSize / 2,
          cy: y + row * cellSize + cellSize / 2
        });
      }
    }

    return { cells: result, cellSize, threshold };
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

  const ghslPrepared = buildGhslCells();
  const ghslCells = ghslPrepared.cells;
  const ghslCellSize = ghslPrepared.cellSize;
  const ghslClusters = clusterGhslCells(ghslCells, ghslGrid.cells);

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

  const allocationGrid = {
    x: 180,
    y: 110,
    size: 440,
    cells: 12
  };

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

  const districtConfigs = [
    {
      key: "A",
      color: "#7ab6a7",
      points: [
        [180, 110],
        [400, 110],
        [400, 350],
        [180, 574]
      ] as Array<[number, number]>,
      anchorX: 284,
      anchorY: 208,
      linkDirection: "down" as const
    },
    {
      key: "B",
      color: "#c8a264",
      points: [
        [400, 110],
        [620, 110],
        [620, 574],
        [400, 350]
      ] as Array<[number, number]>,
      anchorX: 516,
      anchorY: 208,
      linkDirection: "down" as const
    },
    {
      key: "C",
      color: "#c68678",
      points: [
        [180, 574],
        [400, 350],
        [620, 574]
      ] as Array<[number, number]>,
      anchorX: 400,
      anchorY: 510,
      linkDirection: "up" as const
    }
  ];

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

  function districtIndexForPoint(x: number, y: number) {
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

  function buildAllocationCells() {
    const { x, y, size, cells } = allocationGrid;
    const cellSize = size / cells;
    const result: AllocationCell[] = [];

    for (let row = 0; row < cells; row += 1) {
      for (let col = 0; col < cells; col += 1) {
        const cx = x + col * cellSize + cellSize / 2;
        const cy = y + row * cellSize + cellSize / 2;
        result.push({
          row,
          col,
          x: x + col * cellSize,
          y: y + row * cellSize,
          cx,
          cy,
          surface: allocationSurface(col, row),
          volume: allocationVolume(col, row),
          district: districtIndexForPoint(cx, cy),
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

    return { cells: result, cellSize, totals };
  }

  const allocationPrepared = buildAllocationCells();
  const allocationCells = allocationPrepared.cells;
  const allocationCellSize = allocationPrepared.cellSize;
  const allocationDistrictTotals = allocationPrepared.totals;

  function isoBarPaths(x: number, y: number, size: number, height: number) {
    const inset = 4;
    const left = x + inset;
    const right = x + size - inset;
    const top = y + inset;
    const bottom = y + size - inset;
    const dx = size * 0.12;
    const lift = Math.max(8, height);

    const front = `M ${left} ${bottom} L ${right} ${bottom} L ${right} ${bottom - lift} L ${left} ${bottom - lift} Z`;
    const side = `M ${right} ${bottom} L ${right + dx} ${bottom - dx} L ${right + dx} ${bottom - lift - dx} L ${right} ${bottom - lift} Z`;
    const roof = `M ${left} ${bottom - lift} L ${right} ${bottom - lift} L ${right + dx} ${bottom - lift - dx} L ${left + dx} ${bottom - lift - dx} Z`;

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

  function buildParisMap(activeStepIndex: number, stepProgress: number): LayeredMapScene {
    const properReveal = stepReveal(activeStepIndex, 1, stepProgress);
    const builtReveal = stepReveal(activeStepIndex, 2, stepProgress);
    const attractionReveal = stepReveal(activeStepIndex, 3, stepProgress);

    return {
      viewport: {
        viewBox: [0, 0, 800, 600],
        background: "#0b1016"
      },
      layers: [
        {
          id: "satellite",
          kind: "image",
          href: parisSatelliteImage,
          x: 0,
          y: 0,
          width: 800,
          height: 600,
          opacity: 1
        },
        {
          id: "attraction-fill",
          kind: "paths",
          opacity: attractionReveal,
          items: [
            {
              d: attractionPath,
              fill: "#67e0cc",
              fillOpacity: 0.1,
              opacity: 1
            }
          ]
        },
        {
          id: "built-fill",
          kind: "paths",
          opacity: builtReveal,
          items: [
            {
              d: builtUpPath,
              fill: "#cfd6dd",
              fillOpacity: 0.22,
              opacity: 1
            }
          ]
        },
        {
          id: "proper-boundary",
          kind: "paths",
          opacity: properReveal,
          items: [
            {
              d: properBoundaryPath,
              stroke: "#ff8b67",
              strokeWidth: 6,
              drawTo: properReveal
            }
          ]
        },
        {
          id: "attraction-boundary",
          kind: "paths",
          opacity: attractionReveal,
          items: [
            {
              d: attractionPath,
              stroke: "#67e0cc",
              strokeWidth: 4,
              drawTo: attractionReveal
            }
          ]
        }
      ]
    };
  }

  function buildGhslMap(activeStepIndex: number, stepProgress: number): LayeredMapScene {
    const builtReveal = stepReveal(activeStepIndex, 1, stepProgress);
    const urbanReveal = stepReveal(activeStepIndex, 2, stepProgress);
    const clusterReveal =
      activeStepIndex < 3 ? 0 : activeStepIndex > 3 ? 1 : rangeProgress(stepProgress, 0, 0.22);

    return {
      viewport: {
        viewBox: [0, 0, 800, 600],
        background: "#091016"
      },
      layers: [
        {
          id: "base-image",
          kind: "image",
          href: ghslBaseImage,
          x: 0,
          y: 0,
          width: 800,
          height: 600,
          opacity: 1
        },
        {
          id: "frame-backdrop",
          kind: "rects",
          items: [
            {
              x: ghslGrid.x,
              y: ghslGrid.y,
              width: ghslGrid.size,
              height: ghslGrid.size,
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
            width: ghslCellSize - 2.4,
            height: ghslCellSize - 2.4,
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
            width: ghslCellSize - 2.4,
            height: ghslCellSize - 2.4,
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
              width: ghslCellSize - 2.4,
              height: ghslCellSize - 2.4,
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
          items: ghslClusters.slice(0, 4).map((cluster) => ({
            x: cluster.cx,
            y: cluster.cy + 6,
            text: cluster.label,
            fill: "#f5efe5",
            fontSize: 18,
            fontWeight: 800,
            anchor: "middle",
            letterSpacing: "0.04em"
          }))
        },
        {
          id: "frame-labels",
          kind: "labels",
          items: [
            {
              x: ghslGrid.x,
              y: 66,
              text: "Same spatial frame",
              fill: "rgba(245,239,229,0.76)",
              fontSize: 20,
              fontWeight: 700,
              anchor: "start",
              letterSpacing: "0.12em"
            },
            {
              x: ghslGrid.x,
              y: 572,
              text: "15 x 15 cells. Each square = 1 km.",
              fill: "rgba(184,173,160,0.84)",
              fontSize: 16,
              fontWeight: 700,
              anchor: "start",
              letterSpacing: "0.03em"
            }
          ]
        }
      ]
    };
  }

  function buildAllocationMap(activeStepIndex: number, stepProgress: number): LayeredMapScene {
    const volumeReveal = activeStepIndex < 1 ? 0 : activeStepIndex > 1 ? 1 : rangeProgress(stepProgress, 0, 0.7);
    const censusReveal = activeStepIndex < 2 ? 0 : activeStepIndex > 2 ? 1 : rangeProgress(stepProgress, 0, 0.24);

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

    const districtLabelWidth = 124;
    const districtLabelHeight = 62;

    const groundRects = allocationCells.map((cell) => ({
      x: cell.x + 0.8,
      y: cell.y + 0.8,
      width: allocationCellSize - 1.6,
      height: allocationCellSize - 1.6,
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

      const populationNorm = Math.min(1, cell.population / 2200);
      const paths = isoBarPaths(cell.x, cell.y, allocationCellSize, cell.volume * 54);
      const front = censusReveal > 0 ? rgb(mixTriplet(popFrontA, popFrontB, populationNorm)) : rgb(mixTriplet(volumeFrontA, volumeFrontB, cell.volume));
      const side = censusReveal > 0 ? rgb(mixTriplet(popSideA, popSideB, populationNorm)) : rgb(mixTriplet(volumeSideA, volumeSideB, cell.volume));
      const roof = censusReveal > 0 ? rgb(mixTriplet(popTopA, popTopB, populationNorm)) : rgb(mixTriplet(volumeTopA, volumeTopB, cell.volume));

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
        y: district.anchorY - 8,
        text: `ADMIN ${district.key}`,
        fill: "#f5efe5",
        fontSize: 13,
        fontWeight: 700,
        anchor: "middle" as const,
        letterSpacing: "0.08em",
        opacity: censusReveal
      },
      {
        id: `district-total-${district.key}`,
        x: district.anchorX,
        y: district.anchorY + 20,
        text: `${Math.round(allocationDistrictTotals[index].population / 1000)}K`,
        fill: "#f5efe5",
        fontSize: 24,
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
        viewBox: [0, 0, 800, 600],
        background: "#091016"
      },
      layers: [
        {
          id: "allocation-base",
          kind: "image",
          href: allocationBaseImage,
          x: 0,
          y: 0,
          width: 800,
          height: 600,
          opacity: 1
        },
        {
          id: "allocation-frame",
          kind: "rects",
          items: [
            {
              x: allocationGrid.x,
              y: allocationGrid.y,
              width: allocationGrid.size,
              height: allocationGrid.size,
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
        },
        {
          id: "allocation-frame-labels",
          kind: "labels",
          items: [
            {
              x: allocationGrid.x,
              y: 66,
              text: "Same spatial frame",
              fill: "rgba(245,239,229,0.76)",
              fontSize: 20,
              fontWeight: 700,
              anchor: "start",
              letterSpacing: "0.12em"
            },
            {
              x: allocationGrid.x,
              y: 572,
              text: "12 x 12 cells. Bar height = residential volume.",
              fill: "rgba(184,173,160,0.84)",
              fontSize: 16,
              fontWeight: 700,
              anchor: "start",
              letterSpacing: "0.03em"
            }
          ]
        }
      ]
    };
  }

  function getXYGraph(kind: SceneKind, activeStepIndex: number, stepProgress: number): XYGraph {
    return kind === "xy-world"
      ? buildWorldCurveGraph(activeStepIndex, stepProgress)
      : buildScenarioGraph(activeStepIndex, stepProgress);
  }

  function getLayeredMap(kind: SceneKind, activeStepIndex: number, stepProgress: number): LayeredMapScene {
    if (kind === "map-ghsl") {
      return buildGhslMap(activeStepIndex, stepProgress);
    }

    if (kind === "map-allocation") {
      return buildAllocationMap(activeStepIndex, stepProgress);
    }

    return buildParisMap(activeStepIndex, stepProgress);
  }

  function getLegendItems(kind: SceneKind): LegendItem[] {
    if (kind === "xy-world") {
      return [{ label: "World", color: "#67e0cc", shape: "line" }];
    }

    if (kind === "xy-scenarios") {
      return [
        { label: "Runaway", color: "#ff8b67", shape: "line" },
        { label: "Lifecycle", color: "#67e0cc", shape: "line" },
        { label: "Proportional", color: "#8ac6ff", shape: "line" }
      ];
    }

    if (kind === "map-ghsl") {
      return [
        { label: "Imagery", color: "#4e5d6d", shape: "fill" },
        { label: "Built-up share", color: "#d7aa72", shape: "fill" },
        { label: "Urban cells", color: "#efe7db", shape: "fill" },
        { label: "Clusters", color: "#7ab6a7", shape: "fill" }
      ];
    }

    if (kind === "map-allocation") {
      return [
        { label: "Imagery", color: "#4e5d6d", shape: "fill" },
        { label: "Volume bar", color: "#8db8ca", shape: "fill" },
        { label: "Admin total", color: "#efc684", shape: "fill" },
        { label: "Allocation flow", color: "#efc684", shape: "line" }
      ];
    }

    return [
      { label: "Paris proper", color: "#ff8b67", shape: "outline" },
      { label: "Built-up footprint", color: "#cfd6dd", shape: "fill" },
      { label: "Attraction area", color: "#67e0cc", shape: "outline" }
    ];
  }
</script>

<svelte:head>
  <title>Minimal scrollytell scaffold</title>
  <meta
    name="description"
    content="Minimal SvelteKit and Scrollama scaffold with prose scenes, sticky scenes, XY graphs, and layered map reveals."
  />
</svelte:head>

<main class="page">
  <article class="article intro">
    <h1>Minimal scrollytell scaffold</h1>
    <div class="prose">
      <p>
        This version is intentionally stripped down. It proves the app shell first:
        prose sections, sticky scenes, one reusable XY graph family, and one reusable
        layered map family.
      </p>
      <p>
        The third sticky scene ports the mock Paris boundary reveal into the same
        centered template, using dummy geometry and a fake satellite-like base layer.
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
      tailHoldVh={scene.tailHoldVh}
      steps={scene.steps}
      let:activeStepIndex
      let:stepProgress
    >
      {#if scene.kind === "map-paris" || scene.kind === "map-ghsl" || scene.kind === "map-allocation"}
        <LayeredMapCanvas map={getLayeredMap(scene.kind, activeStepIndex, stepProgress)} />
      {:else}
        <XYGraphCanvas graph={getXYGraph(scene.kind, activeStepIndex, stepProgress)} />
      {/if}

      <div slot="legend" class="graph-legend">
        {#each getLegendItems(scene.kind) as item (item.label)}
          <div class="legend-item">
            <span
              class={`legend-swatch ${item.shape ?? "line"}`}
              style={`--legend-color: ${item.color}`}
            ></span>
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
    flex: none;
  }

  .legend-swatch.line {
    width: 20px;
    height: 4px;
    border-radius: 999px;
    background: var(--legend-color);
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
  }
</style>
