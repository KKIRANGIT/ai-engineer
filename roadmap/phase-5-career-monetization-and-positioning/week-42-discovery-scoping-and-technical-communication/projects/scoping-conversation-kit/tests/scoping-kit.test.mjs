import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { buildDiscoveryQuestions } from "../src/discovery.js";
import { buildRiskRegister } from "../src/risk-register.js";
import { buildScopeDraft, buildStatementOfWork } from "../src/scope-draft.js";

const currentDir = path.dirname(fileURLToPath(import.meta.url));
const brief = JSON.parse(
  readFileSync(path.join(currentDir, "..", "data", "client-brief.json"), "utf8")
);

test("discovery questions focus on workflow, success, and constraints", () => {
  const questions = buildDiscoveryQuestions(brief);

  assert.equal(questions.length, 3);
  assert.match(questions[0], /triaging policy and billing tickets/);
});

test("risk register keeps unknowns visible", () => {
  const risks = buildRiskRegister(brief);

  assert.equal(risks.length, 2);
  assert.match(risks[0].mitigation, /validate during discovery/);
});

test("scope draft includes boundary decisions", () => {
  const scope = buildScopeDraft(brief);
  const statement = buildStatementOfWork(brief);

  assert.equal(scope.excludedScope.length, 2);
  assert.match(statement, /Excluded:/);
});
