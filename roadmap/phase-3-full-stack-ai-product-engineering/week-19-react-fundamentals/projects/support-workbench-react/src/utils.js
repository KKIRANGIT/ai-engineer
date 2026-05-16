function normalizeText(value) {
  return value.trim().replace(/\s+/g, " ");
}

export function validateTicketDraft(draft) {
  const errors = {};

  if (normalizeText(draft.title).length < 8) {
    errors.title = "Use a title with at least 8 meaningful characters.";
  }

  if (normalizeText(draft.customer).length < 2) {
    errors.customer = "Enter the customer or account name.";
  }

  if (normalizeText(draft.summary).length < 15) {
    errors.summary = "Write a short summary that another teammate can understand quickly.";
  }

  if (normalizeText(draft.description).length < 30) {
    errors.description = "Add enough detail so the next person knows what happened.";
  }

  if (normalizeText(draft.owner).length < 2) {
    errors.owner = "Assign an owner for the ticket.";
  }

  return errors;
}

export function isDraftValid(draft) {
  return Object.keys(validateTicketDraft(draft)).length === 0;
}

export function createTicketFromDraft(draft, currentDate = new Date()) {
  const sequence = String(currentDate.getTime()).slice(-5);

  return {
    id: `T-${sequence}`,
    title: normalizeText(draft.title),
    customer: normalizeText(draft.customer),
    priority: draft.priority,
    status: "open",
    channel: draft.channel,
    summary: normalizeText(draft.summary),
    description: normalizeText(draft.description),
    owner: normalizeText(draft.owner),
    createdAt: currentDate.toISOString().slice(0, 10),
    tags: [draft.priority, draft.channel],
  };
}

export function filterTickets(tickets, filters) {
  const normalizedSearch = filters.search.trim().toLowerCase();

  return tickets.filter((ticket) => {
    const matchesStatus =
      filters.status === "all" || ticket.status === filters.status;
    const matchesPriority =
      filters.priority === "all" || ticket.priority === filters.priority;

    const searchTarget = [
      ticket.title,
      ticket.customer,
      ticket.summary,
      ticket.owner,
      ...(ticket.tags ?? []),
    ]
      .join(" ")
      .toLowerCase();

    const matchesSearch =
      normalizedSearch === "" || searchTarget.includes(normalizedSearch);

    return matchesStatus && matchesPriority && matchesSearch;
  });
}

export function buildQueueStats(tickets) {
  const counts = {
    total: tickets.length,
    open: 0,
    active: 0,
    highPriority: 0,
  };

  for (const ticket of tickets) {
    if (ticket.status === "open") {
      counts.open += 1;
    }

    if (ticket.status === "open" || ticket.status === "in_progress") {
      counts.active += 1;
    }

    if (ticket.priority === "high") {
      counts.highPriority += 1;
    }
  }

  return counts;
}

export function buildActivityFeed(tickets) {
  return [...tickets]
    .sort((left, right) => right.createdAt.localeCompare(left.createdAt))
    .slice(0, 5)
    .map((ticket) => ({
      id: `activity-${ticket.id}`,
      title: ticket.title,
      message: `${ticket.owner} is responsible for ${ticket.customer}.`,
      meta: `${ticket.status} · ${ticket.priority} priority`,
      createdAt: ticket.createdAt,
    }));
}

export function formatCreatedDate(dateText) {
  const [year, month, day] = dateText.split("-");
  return `${day}/${month}/${year}`;
}

export function getSelectedTicket(tickets, selectedTicketId) {
  return tickets.find((ticket) => ticket.id === selectedTicketId) ?? null;
}
