import TicketCard from "./TicketCard.jsx";

function TicketList({ tickets, selectedTicketId, onSelectTicket }) {
  return (
    <section className="panel">
      <div className="panel-heading">
        <h2>Visible queue</h2>
        <p>Filtered and searched from the shared ticket collection.</p>
      </div>

      {tickets.length === 0 ? (
        <div className="empty-state">
          <h3>No tickets match the current filters.</h3>
          <p>Change the search, status, or priority filters to widen the queue.</p>
        </div>
      ) : (
        <div className="ticket-list">
          {tickets.map((ticket) => (
            <TicketCard
              key={ticket.id}
              ticket={ticket}
              isSelected={ticket.id === selectedTicketId}
              onSelect={onSelectTicket}
            />
          ))}
        </div>
      )}
    </section>
  );
}

export default TicketList;
