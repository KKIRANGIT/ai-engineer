export default function TicketsLoading() {
  return (
    <main className="page-grid">
      <section className="panel">
        <div className="panel-heading">
          <h2>Loading ticket queue</h2>
          <p>The route shell can appear immediately while the ticket list resolves.</p>
        </div>
        <div className="loading-skeleton" />
      </section>
    </main>
  );
}
