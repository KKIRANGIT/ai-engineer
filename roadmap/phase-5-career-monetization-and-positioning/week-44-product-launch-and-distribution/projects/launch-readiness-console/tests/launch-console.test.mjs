import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { activationRate, signalSummary } from "../src/activation-metrics.js";
import { chooseBestChannel } from "../src/channel-prioritizer.js";
import { readinessScore, missingReadinessAreas } from "../src/readiness.js";

const currentDir = path.dirname(fileURLToPath(import.meta.url));
const plan = JSON.parse(
  readFileSync(path.join(currentDir, "..", "data", "launch-plan.json"), "utf8")
);
const feedback = JSON.parse(
  readFileSync(path.join(currentDir, "..", "data", "launch-feedback.json"), "utf8")
);

test("readiness score surfaces missing areas", () => {
  assert.equal(readinessScore(plan), 3);
  assert.deepEqual(missingReadinessAreas(plan), ["errorHandlingVisible"]);
});

test("channel prioritization favors user fit with usable feedback", () => {
  const best = chooseBestChannel(plan.channels);

  assert.equal(best.name, "compliance community");
});

test("activation metrics keep learning visible", () => {
  assert.equal(activationRate(feedback), 6 / 14);
  assert.equal(signalSummary(feedback), "review onboarding and message clarity");
});
