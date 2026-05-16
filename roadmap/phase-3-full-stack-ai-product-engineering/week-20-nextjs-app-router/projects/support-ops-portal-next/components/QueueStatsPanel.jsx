const statCards = [
  { key: "total", label: "Total tickets" },
  { key: "open", label: "Open tickets" },
  { key: "active", label: "Active queue" },
  { key: "highPriority", label: "High priority" },
];

export default function QueueStatsPanel({ stats }) {
  return (
    <section className="panel">
      <div className="panel-heading">
        <h2>Queue snapshot</h2>
        <p>This server-rendered panel is derived from shared ticket data.</p>
      </div>

      <div className="stats-grid">
        {statCards.map((card) => (
          <article className="stat-card" key={card.key}>
            <span className="stat-card__label">{card.label}</span>
            <strong className="stat-card__value">{stats[card.key]}</strong>
          </article>
        ))}
      </div>
    </section>
  );
}
