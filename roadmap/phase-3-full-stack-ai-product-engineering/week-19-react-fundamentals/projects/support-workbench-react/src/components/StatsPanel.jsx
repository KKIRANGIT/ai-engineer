const statCards = [
  { key: "total", label: "Total tickets" },
  { key: "open", label: "Open tickets" },
  { key: "active", label: "Active queue" },
  { key: "highPriority", label: "High priority" },
];

function StatsPanel({ stats }) {
  return (
    <section className="panel">
      <div className="panel-heading">
        <h2>Queue snapshot</h2>
        <p>Derived from the same ticket collection used everywhere else.</p>
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

export default StatsPanel;
