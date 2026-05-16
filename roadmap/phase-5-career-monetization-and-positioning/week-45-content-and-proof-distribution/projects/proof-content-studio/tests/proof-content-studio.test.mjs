import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { isProofBacked, proofStrength } from "../src/proof-check.js";
import { repurposeAsset } from "../src/repurpose.js";
import { chooseLeadTheme, summarizeTheme } from "../src/theme-planner.js";

const currentDir = path.dirname(fileURLToPath(import.meta.url));
const assets = JSON.parse(
  readFileSync(path.join(currentDir, "..", "data", "content-assets.json"), "utf8")
);

test("lead theme comes from real project-backed proof", () => {
  const lead = chooseLeadTheme(assets);

  assert.equal(lead.project, "policy-evidence-assistant");
  assert.match(summarizeTheme(lead), /AI product teams/);
});

test("proof checks reject vague content inputs", () => {
  assert.equal(proofStrength(assets[0]), 3);
  assert.equal(isProofBacked(assets[1]), true);
});

test("repurposing keeps the core lesson consistent", () => {
  const repurposed = repurposeAsset(assets[0]);

  assert.match(repurposed.articleHook, /trust depends on visible grounding/);
  assert.match(repurposed.portfolioSnippet, /retrieval and citation design/);
});
