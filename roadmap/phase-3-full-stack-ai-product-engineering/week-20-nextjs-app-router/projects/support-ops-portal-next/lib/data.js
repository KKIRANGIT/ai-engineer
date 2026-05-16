const tickets = [
  {
    id: "T-3001",
    title: "Duplicate billing retry loop",
    customer: "Acme Logistics",
    status: "open",
    priority: "high",
    owner: "Priya",
    channel: "email",
    description:
      "The billing service retried a duplicate invoice reconciliation and trapped the refund workflow in a loop.",
    tags: ["billing", "refund", "workflow"],
  },
  {
    id: "T-3002",
    title: "Invite acceptance fails on mobile",
    customer: "Northstar Health",
    status: "in_progress",
    priority: "medium",
    owner: "Mina",
    channel: "chat",
    description:
      "A workspace admin can send the invite, but the recipient hits an expired-session message when accepting from mobile email clients.",
    tags: ["auth", "mobile", "onboarding"],
  },
  {
    id: "T-3003",
    title: "Quarterly metrics export request",
    customer: "Bluebird Retail",
    status: "closed",
    priority: "low",
    owner: "Derek",
    channel: "email",
    description:
      "Customer success requested a CSV of resolution times and category counts for the previous quarter.",
    tags: ["reporting", "analytics"],
  },
  {
    id: "T-3004",
    title: "SLA reminder triggered early",
    customer: "Orbit Finance",
    status: "open",
    priority: "high",
    owner: "Anita",
    channel: "voice",
    description:
      "The support lead received an SLA breach reminder before the first-response threshold should have expired.",
    tags: ["sla", "alerts", "ops"],
  },
];

export function getAllTickets() {
  return tickets;
}

export function getTicketById(ticketId) {
  return tickets.find((ticket) => ticket.id === ticketId) ?? null;
}

export function normalizeTicketFilters(rawFilters) {
  return {
    q: String(rawFilters.q ?? "").trim(),
    status: String(rawFilters.status ?? "all"),
    priority: String(rawFilters.priority ?? "all"),
  };
}

export function filterTickets(allTickets, filters) {
  const query = filters.q.toLowerCase();

  return allTickets.filter((ticket) => {
    const matchesStatus = filters.status === "all" || ticket.status === filters.status;
    const matchesPriority =
      filters.priority === "all" || ticket.priority === filters.priority;

    const searchTarget = [
      ticket.title,
      ticket.customer,
      ticket.owner,
      ticket.description,
      ...ticket.tags,
    ]
      .join(" ")
      .toLowerCase();

    const matchesQuery = query === "" || searchTarget.includes(query);

    return matchesStatus && matchesPriority && matchesQuery;
  });
}

export function buildQueueStats(allTickets) {
  const stats = {
    total: allTickets.length,
    open: 0,
    active: 0,
    highPriority: 0,
  };

  for (const ticket of allTickets) {
    if (ticket.status === "open") {
      stats.open += 1;
    }

    if (ticket.status === "open" || ticket.status === "in_progress") {
      stats.active += 1;
    }

    if (ticket.priority === "high") {
      stats.highPriority += 1;
    }
  }

  return stats;
}

export function buildQueueInsight(allTickets) {
  const stats = buildQueueStats(allTickets);
  const criticalTicket = allTickets.find((ticket) => ticket.priority === "high");

  return {
    headline: `${stats.highPriority} high-priority ticket(s) need attention`,
    summary:
      criticalTicket !== undefined
        ? `The queue has ${stats.active} active ticket(s). Start with ${criticalTicket.title} for ${criticalTicket.customer}.`
        : "The queue is stable. No high-priority issues are waiting right now.",
    focusArea: criticalTicket ? `Focus: ${criticalTicket.owner}` : "Focus: queue maintenance",
    nextAction: criticalTicket ? "Review high-priority ownership" : "Review medium-priority backlog",
  };
}
