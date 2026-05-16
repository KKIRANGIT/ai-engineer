export function describeSurfaceState({ isLoading, hasData, errorCode }) {
  if (errorCode) {
    return {
      tone: "recovery",
      nextAction: "retry-or-contact-support",
    };
  }

  if (isLoading) {
    return {
      tone: "progress",
      nextAction: "wait-with-feedback",
    };
  }

  if (!hasData) {
    return {
      tone: "onboarding",
      nextAction: "show-first-step",
    };
  }

  return {
    tone: "active",
    nextAction: "continue-workflow",
  };
}
