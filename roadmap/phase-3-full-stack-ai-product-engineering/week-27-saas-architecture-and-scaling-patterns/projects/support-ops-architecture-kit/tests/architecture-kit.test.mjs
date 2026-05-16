import test from "node:test";
import assert from "node:assert/strict";

import { chooseCachePolicy } from "../src/cache-policy.js";
import { canAccessExperimentalFeature } from "../src/feature-flags.js";
import { topology } from "../src/topology.js";

test("cache policy keeps billing state fresh", () => {
  assert.equal(chooseCachePolicy("billing-state"), "always-fresh");
});

test("experimental feature access stays narrow", () => {
  assert.equal(canAccessExperimentalFeature({ role: "admin", planKey: "team" }), true);
  assert.equal(canAccessExperimentalFeature({ role: "member", planKey: "team" }), false);
});

test("topology includes the worker boundary", () => {
  assert.ok(topology.some((entry) => entry.component === "worker"));
});
