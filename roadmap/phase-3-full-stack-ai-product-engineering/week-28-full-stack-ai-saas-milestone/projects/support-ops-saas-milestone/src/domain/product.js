import { authModel } from "./auth.js";
import { billingModel } from "./billing.js";
import { jobModel } from "./jobs.js";
import { observabilityModel } from "./observability.js";
import { usageModel } from "./usage.js";

export function buildMilestoneBlueprint() {
  return {
    name: "support-ops-saas-milestone",
    authModel,
    billingModel,
    jobModel,
    observabilityModel,
    usageModel,
    capabilities: [
      "multi-user-access",
      "plan-aware-entitlements",
      "background-analysis-workflow",
      "product-observability",
      "usage-tracking",
      "launch-documentation",
    ],
  };
}
