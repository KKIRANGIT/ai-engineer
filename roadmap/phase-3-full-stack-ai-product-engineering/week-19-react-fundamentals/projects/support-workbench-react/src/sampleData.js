export const seedTickets = [
  {
    id: "T-2001",
    title: "Refund request blocked by duplicate charge flag",
    customer: "Acme Logistics",
    priority: "high",
    status: "open",
    channel: "email",
    summary: "Customer was charged twice and the refund workflow did not complete.",
    description:
      "Finance confirmed the duplicate payment, but the refund action remained stuck in pending status after the agent attempted the reversal.",
    owner: "Priya",
    createdAt: "2026-05-07",
    tags: ["billing", "refund", "finance"],
  },
  {
    id: "T-2002",
    title: "Workspace invite email never arrived",
    customer: "Northstar Health",
    priority: "medium",
    status: "open",
    channel: "chat",
    summary: "Admin cannot complete workspace onboarding for a new manager.",
    description:
      "The admin sent multiple invites, but the new manager still has not received any onboarding email. Spam and security filters were checked.",
    owner: "Mina",
    createdAt: "2026-05-08",
    tags: ["auth", "email", "onboarding"],
  },
  {
    id: "T-2003",
    title: "Need export of last quarter support metrics",
    customer: "Bluebird Retail",
    priority: "low",
    status: "closed",
    channel: "email",
    summary: "Customer success team requested historical reporting export.",
    description:
      "The customer success lead asked for a CSV containing resolution times and ticket categories for the previous quarter.",
    owner: "Derek",
    createdAt: "2026-05-04",
    tags: ["reporting", "analytics"],
  },
  {
    id: "T-2004",
    title: "SLA escalation warning triggered too early",
    customer: "Orbit Finance",
    priority: "high",
    status: "in_progress",
    channel: "voice",
    summary: "Team received an escalation warning even though the response clock had not expired.",
    description:
      "The support lead reported that the escalation alert fired during the first response window instead of after the documented SLA threshold.",
    owner: "Anita",
    createdAt: "2026-05-09",
    tags: ["sla", "alerts", "workflow"],
  },
];

export const defaultFilters = {
  search: "",
  status: "all",
  priority: "all",
};

export const emptyDraft = {
  title: "",
  customer: "",
  priority: "medium",
  channel: "email",
  summary: "",
  description: "",
  owner: "",
};
