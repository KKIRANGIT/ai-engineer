import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { auditProfileConsistency } from "../src/profile-audit.js";
import { buildPositioningStatement, buildVerbalIntro } from "../src/positioning.js";
import { rankProjects } from "../src/project-ranking.js";

const currentDir = path.dirname(fileURLToPath(import.meta.url));
const profile = JSON.parse(
  readFileSync(path.join(currentDir, "..", "data", "profile-data.json"), "utf8")
);
const projects = JSON.parse(
  readFileSync(path.join(currentDir, "..", "data", "projects.json"), "utf8")
);

test("project ranking puts the strongest proof-first projects at the top", () => {
  const ranked = rankProjects(projects);

  assert.equal(ranked[0].name, "policy-evidence-assistant");
  assert.equal(ranked[ranked.length - 1].name, "cli-calculator");
});

test("positioning statement is specific enough to mention user and outcome", () => {
  const statement = buildPositioningStatement(profile);

  assert.match(statement, /operations and support teams/);
  assert.match(statement, /save time and improve trust/);
});

test("verbal intro uses visible project proof", () => {
  const ranked = rankProjects(projects);
  const intro = buildVerbalIntro(profile, ranked.map((project) => project.name));

  assert.match(intro, /policy-evidence-assistant/);
  assert.match(intro, /lead-outreach-workflow-copilot/);
});

test("profile audit checks whether the main signals overlap", () => {
  const audit = auditProfileConsistency(profile);

  assert.equal(audit.consistent, true);
  assert.ok(audit.headlineSummaryOverlap >= 1);
  assert.ok(audit.summaryGithubOverlap >= 1);
});
