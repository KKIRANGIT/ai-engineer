export function createJob({ jobId, workspaceId, requestedByUserId }) {
  return {
    jobId,
    workspaceId,
    requestedByUserId,
    status: "queued",
    resultSummary: null,
  };
}

export function markRunning(job) {
  return {
    ...job,
    status: "running",
  };
}

export function markCompleted(job, resultSummary) {
  return {
    ...job,
    status: "completed",
    resultSummary,
  };
}
