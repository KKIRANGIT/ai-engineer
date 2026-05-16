export function fitFlags(opportunity) {
  const flags = [];

  if (opportunity.scopeClarity <= 1) {
    flags.push("scope-unclear");
  }

  if (opportunity.timelineRealism <= 1) {
    flags.push("timeline-risk");
  }

  if (opportunity.budget <= 1) {
    flags.push("budget-risk");
  }

  return flags;
}
