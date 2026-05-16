export const planLimits = {
  free: { maxUnits: 1000 },
  team: { maxUnits: 20000 },
};

export function canConsumeUnits(planKey, currentUnits, requestedUnits) {
  const limit = planLimits[planKey];

  if (!limit) {
    throw new Error(`Unknown plan: ${planKey}`);
  }

  return currentUnits + requestedUnits <= limit.maxUnits;
}
