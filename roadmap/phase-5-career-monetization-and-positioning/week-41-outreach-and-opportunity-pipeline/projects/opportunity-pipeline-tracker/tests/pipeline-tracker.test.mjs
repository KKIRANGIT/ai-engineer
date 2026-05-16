import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { summarizePipeline, chooseFocusChannel } from "../src/pipeline-metrics.js";
import { buildMessage } from "../src/personalization.js";
import { totalWeeklyTouches, rhythmSummary } from "../src/weekly-rhythm.js";

const currentDir = path.dirname(fileURLToPath(import.meta.url));
const opportunities = JSON.parse(
  readFileSync(path.join(currentDir, "..", "data", "opportunities.json"), "utf8")
);
const target = JSON.parse(
  readFileSync(path.join(currentDir, "..", "data", "weekly-target.json"), "utf8")
);

test("pipeline summary counts stages and channels", () => {
  const summary = summarizePipeline(opportunities);

  assert.equal(summary.byStage.reply, 1);
  assert.equal(summary.byChannel["job-application"], 1);
});

test("focus channel prefers the highest relevance opportunity", () => {
  const focusChannel = chooseFocusChannel(opportunities);

  assert.equal(focusChannel, "job-application");
});

test("personalized message keeps relevance and proof visible", () => {
  const message = buildMessage({
    context: "your support automation workflow",
    projectProof: "lead-outreach-workflow-copilot",
    proofTheme: "approval-gated automation",
    targetType: "operations stack"
  });

  assert.match(message, /lead-outreach-workflow-copilot/);
  assert.match(message, /operations stack/);
});

test("weekly rhythm summarizes expected touch count", () => {
  assert.equal(totalWeeklyTouches(target), 13);
  assert.match(rhythmSummary(target), /4 follow-ups/);
});
