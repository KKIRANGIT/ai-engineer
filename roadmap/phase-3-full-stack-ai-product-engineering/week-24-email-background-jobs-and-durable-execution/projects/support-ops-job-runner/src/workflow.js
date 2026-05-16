import { createAttemptRegistry, shouldProcessAttempt } from "./idempotency.js";
import { buildCompletionEmail } from "./notifications.js";
import { createJob, markCompleted, markRunning } from "./job-store.js";

export function submitAnalysisJob(request) {
  return createJob({
    jobId: request.jobId,
    workspaceId: request.workspaceId,
    requestedByUserId: request.requestedByUserId,
  });
}

export function processAnalysisJob(job, attemptKey, registry = createAttemptRegistry()) {
  if (!shouldProcessAttempt(registry, attemptKey)) {
    return {
      job,
      skipped: true,
      email: null,
    };
  }

  const running = markRunning(job);
  const completed = markCompleted(running, "High-priority billing queue needs review");

  return {
    job: completed,
    skipped: false,
    email: buildCompletionEmail(completed),
  };
}
