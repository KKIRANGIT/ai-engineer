import test from "node:test";
import assert from "node:assert/strict";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { loadTasks } from "../src/load-tasks.js";
import { compareWorkflowMinutes } from "../src/roi.js";
import { buildLeadBrief, validateLeadBrief } from "../src/structured-output.js";
import { enrichLead } from "../src/tools.js";
import { runWorkflow } from "../src/workflow-engine.js";

const currentDir = path.dirname(fileURLToPath(import.meta.url));
const tasksPath = path.join(currentDir, "..", "data", "tasks", "lead-tasks.json");
const tasks = loadTasks(tasksPath);

test("task loader returns the representative workflow tasks", () => {
  assert.equal(tasks.length, 2);
  assert.equal(tasks[0].taskId, "lead-001");
});

test("structured lead brief validates when all required fields exist", () => {
  const task = tasks[0];
  const brief = buildLeadBrief(task, enrichLead(task));
  const validation = validateLeadBrief(brief);

  assert.equal(validation.valid, true);
});

test("workflow ends in review state instead of auto-send", () => {
  const result = runWorkflow(tasks[0]);

  assert.equal(result.status, "needs_review");
  assert.ok(result.draftEmail.includes("Would a short intro next week be useful?"));
});

test("workflow emits an audit trail across the key states", () => {
  const result = runWorkflow(tasks[1]);
  const states = result.events.map((event) => event.state);

  assert.deepEqual(states, ["received", "enriched", "brief_ready", "draft_ready"]);
});

test("roi helper compares manual and assisted workflow time", () => {
  const roi = compareWorkflowMinutes({
    manualMinutes: 18,
    assistedMinutes: 7,
    tasksPerWeek: 12,
  });

  assert.equal(roi.timeSavedPerTask, 11);
  assert.equal(roi.weeklyMinutesSaved, 132);
});
