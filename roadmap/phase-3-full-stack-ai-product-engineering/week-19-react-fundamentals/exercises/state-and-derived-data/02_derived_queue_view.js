const tickets = [
  { id: "T-1", status: "open", priority: "high", title: "Billing error" },
  { id: "T-2", status: "closed", priority: "low", title: "Feature request" },
  { id: "T-3", status: "open", priority: "medium", title: "Login issue" },
];

const filters = {
  status: "open",
  search: "issue",
};

function getVisibleTickets(allTickets, currentFilters) {
  return allTickets.filter((ticket) => {
    const matchesStatus =
      currentFilters.status === "all" || ticket.status === currentFilters.status;

    const matchesSearch =
      currentFilters.search.trim() === "" ||
      ticket.title.toLowerCase().includes(currentFilters.search.toLowerCase());

    return matchesStatus && matchesSearch;
  });
}

const visibleTickets = getVisibleTickets(tickets, filters);

console.log("Visible ticket ids:", visibleTickets.map((ticket) => ticket.id));

/*
Why this matters:

- The filtered list is derived when needed.
- We do not store a second "visible tickets" copy in state.
- This reduces bugs and keeps one source of truth.
*/
