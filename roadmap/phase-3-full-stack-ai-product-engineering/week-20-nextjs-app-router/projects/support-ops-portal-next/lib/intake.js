function normalizeText(value) {
  return String(value ?? "").trim().replace(/\s+/g, " ");
}

export function validateIntakeDraft(draft) {
  const errors = {};

  if (normalizeText(draft.title).length < 8) {
    errors.title = "Use a title with at least 8 meaningful characters.";
  }

  if (normalizeText(draft.customer).length < 2) {
    errors.customer = "Enter the customer name.";
  }

  if (normalizeText(draft.problem).length < 25) {
    errors.problem = "Describe the problem with enough detail for triage.";
  }

  return errors;
}

export function buildIntakePreview(draft) {
  const normalizedTitle = normalizeText(draft.title);
  const normalizedCustomer = normalizeText(draft.customer);
  const normalizedProblem = normalizeText(draft.problem);

  const severityLabel =
    draft.severity === "high"
      ? "Urgent review"
      : draft.severity === "medium"
        ? "Normal triage"
        : "Backlog candidate";

  const recommendedOwner =
    normalizedProblem.toLowerCase().includes("billing") ||
    normalizedProblem.toLowerCase().includes("refund")
      ? "Route to finance operations"
      : normalizedProblem.toLowerCase().includes("login") ||
          normalizedProblem.toLowerCase().includes("invite")
        ? "Route to identity support"
        : "Route to core support";

  return {
    headline: `${severityLabel}: ${normalizedTitle}`,
    summary: `${normalizedCustomer} reported: ${normalizedProblem}`,
    recommendedOwner,
    priorityLabel: `Severity: ${draft.severity}`,
    nextAction: "Confirm scope, attach evidence, and assign the correct owner.",
  };
}
