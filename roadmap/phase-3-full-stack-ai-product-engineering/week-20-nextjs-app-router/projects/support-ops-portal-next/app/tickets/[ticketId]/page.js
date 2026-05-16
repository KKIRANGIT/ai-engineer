import { notFound } from "next/navigation";
import { getTicketById } from "../../../lib/data";

export default async function TicketDetailPage({ params }) {
  const { ticketId } = await params;
  const ticket = getTicketById(ticketId);

  if (!ticket) {
    notFound();
  }

  return (
    <main className="page-grid">
      <section className="panel">
        <p className="eyebrow">Dynamic route</p>
        <h2 className="page-title">{ticket.title}</h2>
        <p className="page-lead">
          This page is resolved from the route parameter on the server side.
        </p>

        <div className="detail-stack">
          <div className="meta-row">
            <span className="ticket-id">{ticket.id}</span>
            <span className={`badge badge--${ticket.priority}`}>{ticket.priority}</span>
            <span className={`badge badge--${ticket.status}`}>{ticket.status}</span>
          </div>

          <p className="detail-copy">{ticket.description}</p>

          <div className="detail-grid">
            <div>
              <strong>Customer</strong>
              <p>{ticket.customer}</p>
            </div>
            <div>
              <strong>Owner</strong>
              <p>{ticket.owner}</p>
            </div>
            <div>
              <strong>Channel</strong>
              <p>{ticket.channel}</p>
            </div>
          </div>

          <div className="detail-tags">
            {ticket.tags.map((tag) => (
              <span className="tag" key={tag}>
                {tag}
              </span>
            ))}
          </div>
        </div>
      </section>
    </main>
  );
}
