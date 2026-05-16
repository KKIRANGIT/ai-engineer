import test from "node:test";
import assert from "node:assert/strict";

import { buildCheckoutSession } from "../src/checkout.js";
import { getEntitlements } from "../src/entitlements.js";
import { reduceBillingState } from "../src/webhooks.js";

test("checkout payload includes user and workspace metadata", () => {
  const payload = buildCheckoutSession(
    { id: "u-alice", email: "alice@example.test", workspaceId: "w-acme" },
    "team"
  );

  assert.equal(payload.mode, "subscription");
  assert.equal(payload.metadata.planKey, "team");
  assert.equal(payload.metadata.workspaceId, "w-acme");
});

test("billing reducer activates the subscription after checkout", () => {
  const nextState = reduceBillingState(
    { planKey: "free", status: "free" },
    {
      type: "checkout.session.completed",
      planKey: "team",
      subscriptionId: "sub_123",
    }
  );

  assert.equal(nextState.status, "active");
  assert.equal(nextState.planKey, "team");
});

test("payment failure moves the subscription to past due", () => {
  const nextState = reduceBillingState(
    { planKey: "team", status: "active" },
    { type: "invoice.payment_failed" }
  );

  assert.equal(nextState.status, "past_due");
});

test("entitlements come from both plan and status", () => {
  const entitlements = getEntitlements({ planKey: "team", status: "active" });

  assert.equal(entitlements.monthlyAiRuns, 500);
  assert.equal(entitlements.prioritySupport, true);
});

test("free plan still exposes the intended base allowance", () => {
  const entitlements = getEntitlements({ planKey: "free", status: "free" });

  assert.equal(entitlements.canUseAi, true);
  assert.equal(entitlements.monthlyAiRuns, 10);
});
