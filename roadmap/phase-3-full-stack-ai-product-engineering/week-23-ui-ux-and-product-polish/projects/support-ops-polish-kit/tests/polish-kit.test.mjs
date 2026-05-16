import test from "node:test";
import assert from "node:assert/strict";

import { describeSurfaceState } from "../src/state-models.js";
import { getEmptyStateMessage, getLatencyMessage, getTrustCue } from "../src/ui-copy.js";

test("empty state message explains both absence and next step", () => {
  const message = getEmptyStateMessage("reports");

  assert.match(message, /No reports yet/);
  assert.match(message, /first useful signal/);
});

test("latency message explains visible progress", () => {
  const message = getLatencyMessage("ticket clustering");

  assert.match(message, /Working on ticket clustering/);
  assert.match(message, /visible instead of silent/);
});

test("surface state chooses onboarding when there is no data", () => {
  const result = describeSurfaceState({ isLoading: false, hasData: false, errorCode: null });

  assert.equal(result.tone, "onboarding");
  assert.equal(result.nextAction, "show-first-step");
});

test("trust cue references data volume", () => {
  const cue = getTrustCue(314);

  assert.match(cue, /314/);
});
