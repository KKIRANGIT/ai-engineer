function TicketCard({ ticket, isSelected, onSelect }) {
  const className = isSelected ? "ticket-card ticket-card--active" : "ticket-card";

  return (
    <button type="button" className={className} onClick={() => onSelect(ticket.id)}>
      <div className="ticket-card__topline">
        <span className="ticket-id">{ticket.id}</span>
        <span className={`badge badge--${ticket.priority}`}>{ticket.priority}</span>
      </div>
      <h3>{ticket.title}</h3>
      <p>{ticket.summary}</p>
      <div className="ticket-card__meta">
        <span>{ticket.customer}</span>
        <span>{ticket.owner}</span>
        <span>{ticket.status.replace("_", " ")}</span>
      </div>
    </button>
  );
}

export default TicketCard;
