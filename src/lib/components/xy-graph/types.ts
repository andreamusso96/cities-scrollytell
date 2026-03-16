export type XYScaleType = "linear" | "log";
export type XYLinePattern = "solid" | "dashed" | "dotted";

export type XYTick = {
  value: number;
  label: string;
};

export type XYAxis = {
  domain: [number, number];
  ticks: XYTick[];
  label?: string;
  scale?: XYScaleType;
  opacity?: number;
};

export type XYPoint = {
  x: number;
  y: number;
};

export type XYTextAnchor = "start" | "middle" | "end";

export type XYEndpointLabel = {
  text: string;
  dx?: number;
  dy?: number;
  anchor?: XYTextAnchor;
  revealAt?: number;
  placement?: "point" | "right-column";
};

export type XYLine = {
  id: string;
  color: string;
  points: XYPoint[];
  drawTo?: number;
  opacity?: number;
  width?: number;
  linePattern?: XYLinePattern;
  endLabel?: XYEndpointLabel;
};

export type XYCurveAnnotation = {
  id: string;
  lineId: string;
  point: XYPoint;
  title: string;
  subtitle?: string;
  orientation?: "above" | "below";
  align?: XYTextAnchor;
  dx?: number;
  dy?: number;
  revealAt?: number;
};

export type XYMargins = {
  top: number;
  right: number;
  bottom: number;
  left: number;
};

export type XYGraph = {
  xAxis: XYAxis;
  yAxis: XYAxis;
  lines: XYLine[];
  annotations?: XYCurveAnnotation[];
  margins?: Partial<XYMargins>;
};
