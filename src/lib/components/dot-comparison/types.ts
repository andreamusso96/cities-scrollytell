export type DotComparisonMetric = {
  title: string;
  verb: string;
  delta: string;
  tail: string;
  color: string;
  smallActive?: number[];
  largeActive?: number[];
  largeFilter?: {
    mode: "outer-ring";
    minDist: number;
  };
  smallFade: number;
  largeFade: number;
  glow: number;
  warning: number;
  co2: number;
};

export type DotComparisonScene = {
  smallLabel: string;
  largeLabel: string;
  metric: DotComparisonMetric | null;
  baseGlow?: number;
  baseWarning?: number;
  baseCo2?: number;
};
