export function canAccessExperimentalFeature({ role, planKey }) {
  return role === "admin" && planKey === "team";
}
