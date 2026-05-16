export function canAccessRoute(session, routeKey) {
  if (!session) {
    return false;
  }

  const adminOnlyRoutes = new Set(["settings", "billing", "team"]);

  if (!adminOnlyRoutes.has(routeKey)) {
    return true;
  }

  return session.role === "admin";
}

export function scopeTicketsForSession(session, tickets) {
  if (!session) {
    return [];
  }

  return tickets.filter((ticket) => ticket.workspaceId === session.workspaceId);
}

export function canMutateTicket(session, ticket) {
  if (!session || !ticket) {
    return false;
  }

  if (ticket.workspaceId !== session.workspaceId) {
    return false;
  }

  return session.role === "admin" || ticket.assigneeUserId === session.userId;
}
