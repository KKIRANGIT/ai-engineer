export const activationEvents = [
  "signup_completed",
  "dataset_uploaded",
  "analysis_completed",
  "return_visit",
];

export function isKnownEvent(name) {
  return activationEvents.includes(name);
}
