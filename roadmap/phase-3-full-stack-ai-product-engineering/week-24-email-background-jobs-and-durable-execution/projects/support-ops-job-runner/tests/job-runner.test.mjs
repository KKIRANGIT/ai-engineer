import test from "node:test";
import assert from "node:assert/strict";

import { createAttemptRegistry } from "../src/idempotency.js";
import { submitAnalysisJob, processAnalysisJob } from "../src/workflow.js";

test("submitted jobs begin in queued state", () => {
  const job = submitAnalysisJob({
    jobId: "job-1",
    workspaceId: "w-acme",
    requestedByUserId: "u-alice",
  });

  assert.equal(job.status, "queued");
});

test("processing completes the job and produces a completion email", () => {
  const job = submitAnalysisJob({
    jobId: "job-2",
    workspaceId: "w-acme",
    requestedByUserId: "u-alice",
  });

  const result = processAnalysisJob(job, "attempt-1");

  assert.equal(result.job.status, "completed");
  assert.match(result.email.subject, /job-2/);
});

test("duplicate attempts are skipped by idempotency protection", () => {
  const registry = createAttemptRegistry();
  const job = submitAnalysisJob({
    jobId: "job-3",
    workspaceId: "w-acme",
    requestedByUserId: "u-alice",
  });

  const first = processAnalysisJob(job, "attempt-3", registry);
  const second = processAnalysisJob(job, "attempt-3", registry);

  assert.equal(first.skipped, false);
  assert.equal(second.skipped, true);
});
