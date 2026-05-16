import test from "node:test";
import assert from "node:assert/strict";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { estimateContributionMargin, estimateSessionCost } from "../src/cost-model.js";
import { buildFeedback } from "../src/feedback.js";
import { loadSubmissions } from "../src/load-submissions.js";
import { estimateOverallBand, scoreEssay } from "../src/rubric.js";
import { buildNextStepPlan } from "../src/study-plan.js";

const currentDir = path.dirname(fileURLToPath(import.meta.url));
const submissionsDir = path.join(currentDir, "..", "data", "submissions");
const submissions = loadSubmissions(submissionsDir);

test("submission loader returns representative essays", () => {
  assert.equal(submissions.length, 2);
  assert.equal(submissions[0].submissionId, "essay-001");
});

test("rubric scoring produces the four IELTS-style dimensions", () => {
  const scores = scoreEssay(submissions[0].essay);

  assert.deepEqual(Object.keys(scores), [
    "taskResponse",
    "coherenceAndCohesion",
    "lexicalResource",
    "grammaticalRangeAndAccuracy",
  ]);
});

test("feedback builder returns priorities and an overall band", () => {
  const feedback = buildFeedback(submissions[1]);

  assert.ok(feedback.overallBand >= 5);
  assert.ok(feedback.priorities.length >= 1);
});

test("study plan turns feedback into a next-step practice path", () => {
  const feedback = buildFeedback(submissions[1]);
  const plan = buildNextStepPlan(feedback);

  assert.equal(typeof plan.primaryFocus, "string");
  assert.equal(plan.nextPractice.length, 3);
});

test("cost model estimates session cost and margin", () => {
  const sessionCost = estimateSessionCost({ tokensPerEssay: 2400 });
  const margin = estimateContributionMargin({
    pricePerMonth: 12,
    essaysPerMonth: 12,
    sessionCost,
  });

  assert.equal(sessionCost, 0.0072);
  assert.ok(margin > 11);
});

test("overall band is derived from rubric scores", () => {
  const overallBand = estimateOverallBand({
    taskResponse: 6,
    coherenceAndCohesion: 6.5,
    lexicalResource: 6,
    grammaticalRangeAndAccuracy: 5.5,
  });

  assert.equal(overallBand, 6);
});
