export function buildCompletionEmail(job) {
  return {
    subject: `Support analysis ready for job ${job.jobId}`,
    body: `The analysis for workspace ${job.workspaceId} completed successfully. Review the saved summary and confirm whether escalation is needed.`,
  };
}
