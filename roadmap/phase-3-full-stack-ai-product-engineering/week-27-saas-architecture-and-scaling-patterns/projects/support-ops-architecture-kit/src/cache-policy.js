export function chooseCachePolicy(resourceType) {
  if (resourceType === "dashboard-summary") {
    return "short-lived-cache";
  }

  if (resourceType === "billing-state" || resourceType === "ticket-ownership") {
    return "always-fresh";
  }

  return "case-by-case";
}
