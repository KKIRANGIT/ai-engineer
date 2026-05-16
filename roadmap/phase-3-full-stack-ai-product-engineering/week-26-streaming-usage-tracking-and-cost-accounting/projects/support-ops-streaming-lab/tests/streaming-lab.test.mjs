import test from "node:test";
import assert from "node:assert/strict";

import { estimateRequestCost } from "../src/cost-model.js";
import { canConsumeUnits } from "../src/quotas.js";
import { collectStream, streamSummary } from "../src/stream-session.js";
import { recordUsage, summarizeUsageByUser } from "../src/usage-ledger.js";

test("stream helper yields incremental chunks", async () => {
  const parts = await collectStream(streamSummary("high risk billing queue"));

  assert.deepEqual(parts, ["high", "risk", "billing", "queue"]);
});

test("usage summaries remain per user", () => {
  let entries = [];
  entries = recordUsage(entries, { userId: "u-alice", units: 120 });
  entries = recordUsage(entries, { userId: "u-alice", units: 80 });
  entries = recordUsage(entries, { userId: "u-bob", units: 999 });

  const summary = summarizeUsageByUser(entries, "u-alice");

  assert.equal(summary.requests, 2);
  assert.equal(summary.units, 200);
});

test("quota checks block requests beyond the plan limit", () => {
  assert.equal(canConsumeUnits("free", 950, 40), true);
  assert.equal(canConsumeUnits("free", 950, 60), false);
});

test("cost model estimates a rough request cost", () => {
  const cost = estimateRequestCost(2500);

  assert.equal(cost, 0.01);
});
