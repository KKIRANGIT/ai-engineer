export function buildObservation({ funnelSummary, errorGroups }) {
  const firstIncomplete = funnelSummary.find((step) => !step.completed);
  const dominantError = errorGroups[0] ?? "none";

  return {
    bottleneck: firstIncomplete ? firstIncomplete.name : "repeat-use",
    dominantError,
    suggestedFocus: firstIncomplete
      ? `Improve the step before ${firstIncomplete.name}.`
      : "Investigate repeat-use and retention signals.",
  };
}
