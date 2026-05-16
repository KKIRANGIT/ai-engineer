export function estimateRequestCost(units, ratePerThousandUnits = 0.004) {
  return Number(((units / 1000) * ratePerThousandUnits).toFixed(4));
}
