import QueueSearchForm from "../../components/QueueSearchForm";
import TicketListTable from "../../components/TicketListTable";
import { filterTickets, getAllTickets, normalizeTicketFilters } from "../../lib/data";

export default async function TicketsPage({ searchParams }) {
  const rawSearchParams = await searchParams;
  const filters = normalizeTicketFilters(rawSearchParams);
  const tickets = filterTickets(getAllTickets(), filters);

  return (
    <main className="page-grid">
      <section className="panel">
        <p className="eyebrow">Tickets route</p>
        <h2 className="page-title">Queue view</h2>
        <p className="page-lead">
          This page reads filter state from the URL so the view is reload-safe, shareable,
          and server-readable.
        </p>
      </section>

      <QueueSearchForm filters={filters} />
      <TicketListTable tickets={tickets} />
    </main>
  );
}
