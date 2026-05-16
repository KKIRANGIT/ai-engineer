import { logWorkflowEvent } from "./audit-log.js";
import { buildLeadBrief, validateLeadBrief } from "./structured-output.js";
import { buildDraftEmail, enrichLead } from "./tools.js";

export function runWorkflow(task) {
  const events = [logWorkflowEvent("received", { taskId: task.taskId })];

  const enrichment = enrichLead(task);
  events.push(logWorkflowEvent("enriched", enrichment));

  const brief = buildLeadBrief(task, enrichment);
  const validation = validateLeadBrief(brief);

  if (!validation.valid) {
    events.push(logWorkflowEvent("failed_validation", validation));

    return {
      status: "failed_validation",
      brief,
      draftEmail: null,
      events,
    };
  }

  events.push(logWorkflowEvent("brief_ready", brief));

  const draftEmail = buildDraftEmail(brief);
  events.push(logWorkflowEvent("draft_ready", { preview: draftEmail.slice(0, 80) }));

  return {
    status: "needs_review",
    brief,
    draftEmail,
    events,
  };
}
