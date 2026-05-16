export function scoreOpportunity(opportunity) {
  return (
    opportunity.budget +
    opportunity.scopeClarity +
    opportunity.dataReadiness +
    opportunity.timelineRealism +
    opportunity.strategicValue
  );
}
