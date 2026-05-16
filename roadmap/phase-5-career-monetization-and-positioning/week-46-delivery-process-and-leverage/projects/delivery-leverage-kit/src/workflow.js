export function summarizeWorkflow(process) {
  return process.stages.join(" -> ");
}

export function hasReviewStage(process) {
  return process.stages.includes("qa") && process.stages.includes("handoff");
}
