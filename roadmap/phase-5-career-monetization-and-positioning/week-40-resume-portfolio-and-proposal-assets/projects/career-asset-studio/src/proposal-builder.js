export function buildProposalDraft(project, target) {
  return {
    understanding: `${target.targetBuyer} often need faster ways to handle ${project.problem}.`,
    includedScope: [
      `design a ${project.system}`,
      "define success criteria and review checkpoints",
      "document the main technical tradeoffs"
    ],
    excludedScope: ["long-tail integrations", "unvalidated feature expansion"],
    risks: [project.tradeoff, "timeline depends on stakeholder response speed"],
    nextStep: "Run a discovery call to confirm workflow details and delivery boundaries."
  };
}
