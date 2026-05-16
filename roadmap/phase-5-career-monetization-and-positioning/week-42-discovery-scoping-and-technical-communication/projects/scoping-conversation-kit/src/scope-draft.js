export function buildScopeDraft(brief) {
  return {
    objective: brief.goal,
    includedScope: [
      "phase-one workflow mapping",
      "retrieval and citation design",
      "review checkpoints with stakeholders"
    ],
    excludedScope: ["full platform replacement", "every downstream integration in phase one"],
    assumptions: brief.constraints,
    risks: brief.unknowns
  };
}

export function buildStatementOfWork(brief) {
  const draft = buildScopeDraft(brief);
  return `Objective: ${draft.objective}. Included: ${draft.includedScope.join(", ")}. Excluded: ${draft.excludedScope.join(", ")}.`;
}
