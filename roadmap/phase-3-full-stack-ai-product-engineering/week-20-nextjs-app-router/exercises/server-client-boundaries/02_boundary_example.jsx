// Server component
import TicketFiltersClient from "./TicketFiltersClient";

async function TicketPage({ searchParams }) {
  const params = await searchParams;
  const tickets = await loadTickets(params);

  return (
    <section>
      <h1>Tickets</h1>
      <TicketFiltersClient />
      <TicketTable tickets={tickets} />
    </section>
  );
}

/*
Why this boundary is healthy:

- the page owns server-side reading of URL params and data lookup
- the client component only handles interactive filter changes
- the ticket table stays render-focused
*/

export default TicketPage;
