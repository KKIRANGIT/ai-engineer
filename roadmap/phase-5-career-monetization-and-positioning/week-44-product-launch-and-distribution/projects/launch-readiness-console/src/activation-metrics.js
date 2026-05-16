export function activationRate(feedback) {
  const signups = feedback.find((item) => item.type === "signup")?.count || 0;
  const activations = feedback.find((item) => item.type === "activation")?.count || 0;

  if (signups === 0) {
    return 0;
  }

  return activations / signups;
}

export function signalSummary(feedback) {
  const confusion = feedback.find((item) => item.type === "confusion")?.count || 0;
  return confusion > 0 ? "review onboarding and message clarity" : "signal looks clean";
}
