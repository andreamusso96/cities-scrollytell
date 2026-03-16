export type LayeredMapTextAnchor = "start" | "middle" | "end";

export type LayeredMapViewport = {
  viewBox: [number, number, number, number];
  background?: string;
  preserveAspectRatio?: string;
};

type LayeredMapBaseLayer = {
  id: string;
  opacity?: number;
  translateX?: number;
  translateY?: number;
  scale?: number;
  originX?: number;
  originY?: number;
};

export type LayeredMapImageLayer = LayeredMapBaseLayer & {
  kind: "image";
  href: string;
  x: number;
  y: number;
  width: number;
  height: number;
  preserveAspectRatio?: string;
};

export type LayeredMapPathItem = {
  id?: string;
  d: string;
  fill?: string;
  fillOpacity?: number;
  stroke?: string;
  strokeOpacity?: number;
  strokeWidth?: number;
  opacity?: number;
  drawTo?: number;
  lineCap?: "butt" | "round" | "square";
  lineJoin?: "miter" | "round" | "bevel";
};

export type LayeredMapPathsLayer = LayeredMapBaseLayer & {
  kind: "paths";
  items: LayeredMapPathItem[];
};

export type LayeredMapRectItem = {
  id?: string;
  x: number;
  y: number;
  width: number;
  height: number;
  rx?: number;
  ry?: number;
  fill?: string;
  fillOpacity?: number;
  stroke?: string;
  strokeOpacity?: number;
  strokeWidth?: number;
  opacity?: number;
};

export type LayeredMapRectsLayer = LayeredMapBaseLayer & {
  kind: "rects";
  items: LayeredMapRectItem[];
};

export type LayeredMapLabelItem = {
  id?: string;
  x: number;
  y: number;
  text: string;
  fill?: string;
  opacity?: number;
  fontSize?: number;
  fontWeight?: number | string;
  anchor?: LayeredMapTextAnchor;
  letterSpacing?: string;
};

export type LayeredMapLabelsLayer = LayeredMapBaseLayer & {
  kind: "labels";
  items: LayeredMapLabelItem[];
};

export type LayeredMapLayer =
  | LayeredMapImageLayer
  | LayeredMapPathsLayer
  | LayeredMapRectsLayer
  | LayeredMapLabelsLayer;

export type LayeredMapScene = {
  viewport: LayeredMapViewport;
  layers: LayeredMapLayer[];
};
