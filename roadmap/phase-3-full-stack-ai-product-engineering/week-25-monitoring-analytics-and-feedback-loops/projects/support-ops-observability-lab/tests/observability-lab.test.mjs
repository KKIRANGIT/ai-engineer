import test from "node:test";
import assert from "node:assert/strict";

import { recordEvent, summarizeActivationFunnel } from "../src/analytics.js";
import { groupError } from "../src/error-monitor.js";
import { buildObservation } from "../src/feedback-loop.js";

test("activation funnel reflects missing milestones", () => {
  const events = [
    recordEvent("signup_completed"),
    recordEvent("dataset_uploaded"),
  ];

  const summary = summarizeActivationFunnel(events);
  const analysisStep = summary.find((step) => step.name === "analysis_completed");

  assert.equal(analysisStep.completed, false);
});

test("known failures are grouped for triage", () => {
  const group = groupError({ code: "AUTH_SCOPE_FAILURE" });

  assert.equal(group, "access-control");
});

test("observation helper points at the first incomplete step", () => {
  const observation = buildObservation({
    funnelSummary: [
      { name: "signup_completed", completed: true },
      { name: "dataset_uploaded", completed: false },
    ],
    errorGroups: ["provider-latency"],
  });

  assert.equal(observation.bottleneck, "dataset_uploaded");
  assert.match(observation.suggestedFocus, /dataset_uploaded/);
});
