import test from "node:test";
import assert from "node:assert/strict";

import { buildMilestoneBlueprint } from "../src/domain/product.js";

test("milestone blueprint includes required capability areas", () => {
  const blueprint = buildMilestoneBlueprint();

  assert.ok(blueprint.capabilities.includes("multi-user-access"));
  assert.ok(blueprint.capabilities.includes("plan-aware-entitlements"));
  assert.ok(blueprint.capabilities.includes("background-analysis-workflow"));
  assert.ok(blueprint.capabilities.includes("product-observability"));
});

test("milestone blueprint keeps durable job support explicit", () => {
  const blueprint = buildMilestoneBlueprint();

  assert.equal(blueprint.jobModel.supportsDurableExecution, true);
  assert.equal(blueprint.jobModel.completionSignal, "email-and-dashboard-status");
  assert.equal(blueprint.observabilityModel.launchRequiresVisibility, true);
});
