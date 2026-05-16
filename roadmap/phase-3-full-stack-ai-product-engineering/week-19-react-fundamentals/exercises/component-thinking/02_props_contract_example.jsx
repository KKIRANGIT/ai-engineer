function TicketCard({ ticket, isSelected, onSelect }) {
  return (
    <button
      type="button"
      className={isSelected ? "ticket-card ticket-card--active" : "ticket-card"}
      onClick={() => onSelect(ticket.id)}
    >
      <h3>{ticket.title}</h3>
      <p>{ticket.summary}</p>
    </button>
  );
}

/*
Why this exercise matters:

- The card does not fetch data or own queue state.
- It receives everything it needs through props.
- The parent decides what "selected" means.
- The child only renders and reports user intent.

That is a healthy component contract.
*/

export default TicketCard;
