import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { buildDesignOutline } from "../src/design-outline.js";
import { buildIntro, buildWalkthrough } from "../src/story-compression.js";
import { buildTradeoffAnswers } from "../src/tradeoff-bank.js";

const currentDir = path.dirname(fileURLToPath(import.meta.url));
const story = JSON.parse(
  readFileSync(path.join(currentDir, "..", "data", "project-story.json"), "utf8")
);

test("intro stays specific to user and outcome", () => {
  const intro = buildIntro(story);

  assert.match(intro, /compliance and operations teams/);
  assert.match(intro, /policy-evidence-assistant/);
});

test("walkthrough keeps the problem, architecture, and tradeoff visible", () => {
  const walkthrough = buildWalkthrough(story);

  assert.match(walkthrough, /ingestion, chunking, retrieval/);
  assert.match(walkthrough, /grounded answers with citations/);
});

test("design outline breaks the system into components", () => {
  const outline = buildDesignOutline(story);

  assert.equal(outline.components.length, 5);
  assert.equal(buildTradeoffAnswers(story).length, 3);
});
