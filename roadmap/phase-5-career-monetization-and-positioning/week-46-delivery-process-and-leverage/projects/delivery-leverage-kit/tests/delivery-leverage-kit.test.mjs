import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { buildChecklist } from "../src/checklist-builder.js";
import { rankReusableTasks } from "../src/leverage-audit.js";
import { summarizeWorkflow, hasReviewStage } from "../src/workflow.js";

const currentDir = path.dirname(fileURLToPath(import.meta.url));
const process = JSON.parse(
  readFileSync(path.join(currentDir, "..", "data", "delivery-process.json"), "utf8")
);

test("workflow summary preserves delivery stages", () => {
  assert.equal(
    summarizeWorkflow(process),
    "discovery -> scope -> implementation -> qa -> deployment -> handoff"
  );
  assert.equal(hasReviewStage(process), true);
});

test("leverage audit prioritizes repeated higher-risk work", () => {
  const ranked = rankReusableTasks(process);

  assert.equal(ranked[0].name, "qa checklist");
});

test("checklist builder creates reusable review prompts", () => {
  const checklist = buildChecklist(process);

  assert.equal(checklist.length, 3);
  assert.match(checklist[0], /project kickoff/);
});
