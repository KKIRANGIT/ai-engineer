import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { choosePrimaryPath, pathDecisionMemo } from "../src/path-selection.js";
import { buildQuarterPlan } from "../src/quarter-plan.js";
import { buildReviewSummary } from "../src/review-summary.js";

const currentDir = path.dirname(fileURLToPath(import.meta.url));
const review = JSON.parse(
  readFileSync(path.join(currentDir, "..", "data", "year-review.json"), "utf8")
);

test("review summary keeps strongest yearly signal visible", () => {
  const summary = buildReviewSummary(review);

  assert.match(summary, /policy-evidence-assistant/);
  assert.match(summary, /consistent distribution after building/);
});

test("path selection reflects the strongest path signal", () => {
  assert.equal(choosePrimaryPath(review), "hybrid");
  assert.match(pathDecisionMemo(review), /founder conversations/);
});

test("quarter plan translates strategy into action", () => {
  const plan = buildQuarterPlan(review);

  assert.equal(plan.actions.length, 3);
  assert.match(plan.goal, /win one strong opportunity/);
});
