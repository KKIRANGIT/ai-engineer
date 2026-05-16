import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { buildPortfolioSummary } from "../src/portfolio-summary.js";
import { buildProposalDraft } from "../src/proposal-builder.js";
import { buildResumeBullets } from "../src/resume-builder.js";

const currentDir = path.dirname(fileURLToPath(import.meta.url));
const projects = JSON.parse(
  readFileSync(path.join(currentDir, "..", "data", "project-evidence.json"), "utf8")
);
const target = JSON.parse(
  readFileSync(path.join(currentDir, "..", "data", "opportunity-target.json"), "utf8")
);

test("resume bullets keep user, system, and result visible", () => {
  const bullets = buildResumeBullets(projects[0]);

  assert.equal(bullets.length, 2);
  assert.match(bullets[0], /compliance teams/);
  assert.match(bullets[0], /improved trust/);
});

test("portfolio summary reuses project proof for the right buyer context", () => {
  const summary = buildPortfolioSummary(projects[1], target);

  assert.equal(summary.audience, "operations-focused SaaS teams");
  assert.match(summary.summary, /workflow automation/);
});

test("proposal draft includes scope boundaries and risks", () => {
  const proposal = buildProposalDraft(projects[0], target);

  assert.equal(proposal.excludedScope.length, 2);
  assert.match(proposal.risks[0], /grounded answers with citations/);
});
