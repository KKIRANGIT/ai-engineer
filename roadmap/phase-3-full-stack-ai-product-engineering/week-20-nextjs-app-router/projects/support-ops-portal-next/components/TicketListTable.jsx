import Link from "next/link";

export default function TicketListTable({ tickets }) {
  return (
    <section className="panel">
      <div className="panel-heading">
        <h2>Visible tickets</h2>
        <p>This list is built on the server from the current route state.</p>
      </div>

      {tickets.length === 0 ? (
        <div className="empty-state">
          <h3>No tickets match the current filters.</h3>
          <p>Change the query, status, or priority values to widen the results.</p>
        </div>
      ) : (
        <table className="ticket-table">
          <thead>
            <tr>
              <th>Ticket</th>
              <th>Customer</th>
              <th>Owner</th>
              <th>Status</th>
              <th>Priority</th>
            </tr>
          </thead>
          <tbody>
            {tickets.map((ticket) => (
              <tr key={ticket.id}>
                <td>
                  <Link className="ticket-link" href={`/tickets/${ticket.id}`}>
                    <strong>{ticket.title}</strong>
                    <span>{ticket.id}</span>
                  </Link>
                </td>
                <td>{ticket.customer}</td>
                <td>{ticket.owner}</td>
                <td>
                  <span className={`badge badge--${ticket.status}`}>{ticket.status}</span>
                </td>
                <td>
                  <span className={`badge badge--${ticket.priority}`}>{ticket.priority}</span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </section>
  );
}
