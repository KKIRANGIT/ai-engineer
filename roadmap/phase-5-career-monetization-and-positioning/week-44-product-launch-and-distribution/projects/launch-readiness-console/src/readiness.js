export function readinessScore(plan) {
  return Object.values(plan.readinessChecks).filter(Boolean).length;
}

export function missingReadinessAreas(plan) {
  return Object.entries(plan.readinessChecks)
    .filter(([, ready]) => !ready)
    .map(([area]) => area);
}
