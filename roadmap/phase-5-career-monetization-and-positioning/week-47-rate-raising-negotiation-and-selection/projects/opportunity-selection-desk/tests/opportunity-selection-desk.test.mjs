import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { fitFlags } from "../src/fit-flags.js";
import { scoreOpportunity } from "../src/opportunity-score.js";
import { suggestedRate } from "../src/pricing.js";

const currentDir = path.dirname(fileURLToPath(import.meta.url));
const opportunities = JSON.parse(
  readFileSync(path.join(currentDir, "..", "data", "opportunities.json"), "utf8")
);
const rateCard = JSON.parse(
  readFileSync(path.join(currentDir, "..", "data", "rate-card.json"), "utf8")
);

test("fit scoring differentiates stronger opportunities from weak ones", () => {
  assert.ok(scoreOpportunity(opportunities[0]) > scoreOpportunity(opportunities[1]));
});

test("pricing logic increases rate for complexity and urgency", () => {
  assert.equal(suggestedRate(rateCard, { complex: true, urgent: true }), 168);
});

test("bad-fit flags surface weak scopes quickly", () => {
  assert.deepEqual(fitFlags(opportunities[1]), [
    "scope-unclear",
    "timeline-risk",
    "budget-risk"
  ]);
});
