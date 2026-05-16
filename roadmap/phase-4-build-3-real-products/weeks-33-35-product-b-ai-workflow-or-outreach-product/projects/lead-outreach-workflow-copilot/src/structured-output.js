export function buildLeadBrief(task, enrichment) {
  return {
    taskId: task.taskId,
    company: task.company,
    contactName: task.contactName,
    contactRole: task.contactRole,
    painSummary: task.painSignal,
    urgency: enrichment.urgency,
    recommendedValue: enrichment.outreachAngle,
  };
}

export function validateLeadBrief(brief) {
  const requiredFields = [
    "taskId",
    "company",
    "contactName",
    "contactRole",
    "painSummary",
    "urgency",
    "recommendedValue",
  ];

  const missing = requiredFields.filter((field) => !brief[field]);

  return {
    valid: missing.length === 0,
    missing,
  };
}
