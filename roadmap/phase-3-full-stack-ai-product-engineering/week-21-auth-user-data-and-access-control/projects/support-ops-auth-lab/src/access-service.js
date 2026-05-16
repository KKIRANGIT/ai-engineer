import { getSessionFromToken } from "./auth-model.js";
import { tickets } from "./data-store.js";
import { canAccessRoute, canMutateTicket, scopeTicketsForSession } from "./policies.js";

export function listVisibleTickets(token) {
  const session = getSessionFromToken(token);
  return scopeTicketsForSession(session, tickets);
}

export function requireRoute(token, routeKey) {
  const session = getSessionFromToken(token);

  if (!canAccessRoute(session, routeKey)) {
    throw new Error("Access denied");
  }

  return session;
}

export function updateTicketStatus(token, ticketId, nextStatus) {
  const session = getSessionFromToken(token);
  const ticket = tickets.find((entry) => entry.id === ticketId);

  if (!canMutateTicket(session, ticket)) {
    throw new Error("Mutation denied");
  }

  return {
    ...ticket,
    status: nextStatus,
  };
}
