export function getEmptyStateMessage(resourceName) {
  return `No ${resourceName} yet. Add one to generate the first useful signal instead of starting from a blank dashboard.`;
}

export function getLatencyMessage(progressLabel) {
  return `Working on ${progressLabel}. Early signals appear first so the wait is visible instead of silent.`;
}

export function getTrustCue(sampleCount) {
  return `Based on ${sampleCount} recent records with the review logic shown next to the answer.`;
}
