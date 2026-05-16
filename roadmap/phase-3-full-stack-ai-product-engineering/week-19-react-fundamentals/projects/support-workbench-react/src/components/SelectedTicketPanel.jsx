import { formatCreatedDate } from "../utils.js";

function SelectedTicketPanel({ ticket, totalVisibleTickets }) {
  if (!ticket) {
    return (
      <section className="panel panel--tall">
        <div className="panel-heading">
          <h2>Ticket detail</h2>
          <p>Select a ticket from the queue to inspect its details.</p>
        </div>
        <div className="empty-state empty-state--tall">
          <h3>No active selection</h3>
          <p>The queue currently has {totalVisibleTickets} visible ticket(s), but none is selected.</p>
        </div>
      </section>
    );
  }

  return (
    <section className="panel panel--tall">
      <div className="panel-heading">
        <h2>Ticket detail</h2>
        <p>The selected ticket is resolved from the shared data set by id.</p>
      </div>

      <article className="ticket-detail">
        <div className="ticket-detail__topline">
          <span className="ticket-id">{ticket.id}</span>
          <span className={`badge badge--${ticket.priority}`}>{ticket.priority}</span>
          <span className={`badge badge--status-${ticket.status}`}>{ticket.status}</span>
        </div>

        <h3>{ticket.title}</h3>
        <p className="ticket-detail__description">{ticket.description}</p>

        <dl className="detail-grid">
          <div>
            <dt>Customer</dt>
            <dd>{ticket.customer}</dd>
          </div>
          <div>
            <dt>Owner</dt>
            <dd>{ticket.owner}</dd>
          </div>
          <div>
            <dt>Channel</dt>
            <dd>{ticket.channel}</dd>
          </div>
          <div>
            <dt>Created</dt>
            <dd>{formatCreatedDate(ticket.createdAt)}</dd>
          </div>
        </dl>

        <div className="tag-row">
          {ticket.tags.map((tag) => (
            <span className="tag-chip" key={tag}>
              {tag}
            </span>
          ))}
        </div>
      </article>
    </section>
  );
}

export default SelectedTicketPanel;
