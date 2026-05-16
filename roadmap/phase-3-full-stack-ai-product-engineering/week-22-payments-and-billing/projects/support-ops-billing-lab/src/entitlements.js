import { plans } from "./plans.js";

export function getEntitlements(billingState) {
  const plan = plans[billingState.planKey] ?? plans.free;
  const isEnabled = billingState.status === "active" || plan.key === "free";

  return {
    canUseAi: isEnabled,
    monthlyAiRuns: isEnabled ? plan.monthlyAiRuns : 0,
    seats: isEnabled ? plan.seats : 1,
    prioritySupport: billingState.status === "active" && plan.prioritySupport,
  };
}
