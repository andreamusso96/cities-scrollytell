export type FutureDistributionBin = {
  label: string;
  sublabel: string;
};

export type FutureDistributionScene = {
  bins: FutureDistributionBin[];
  baseCounts: number[];
  futureCounts: number[];
  maxFutureByBin: number[];
  futureColor: string;
  futureLabel: string;
};
