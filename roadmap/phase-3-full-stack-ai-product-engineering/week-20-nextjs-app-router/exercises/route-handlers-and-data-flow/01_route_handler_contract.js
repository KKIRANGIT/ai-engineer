function buildTicketListResponse(tickets) {
  return {
    items: tickets,
    total: tickets.length,
  };
}

function buildNotFoundResponse(ticketId) {
  return {
    error: `Ticket ${ticketId} was not found.`,
  };
}

console.log(buildTicketListResponse([{ id: "T-1" }, { id: "T-2" }]));
console.log(buildNotFoundResponse("T-404"));

/*
Why this exercise matters:

- route handlers should return predictable payloads
- callers should not guess the response structure
- request logic belongs on the server side of the app
*/
