export function enrichLead(task) {
  const urgency = task.painSignal.includes("delays") ? "high" : "medium";
  const outreachAngle =
    task.industry === "health-tech"
      ? "reduce backlog without weakening response quality"
      : "improve follow-up consistency across the funnel";

  return {
    company: task.company,
    contactName: task.contactName,
    contactRole: task.contactRole,
    urgency,
    outreachAngle,
  };
}

export function buildDraftEmail(brief) {
  return `Hi ${brief.contactName},\n\nI noticed ${brief.company} may be dealing with ${brief.painSummary}. We help teams ${brief.recommendedValue}. Would a short intro next week be useful?\n\nBest,\nYour Name`;
}
