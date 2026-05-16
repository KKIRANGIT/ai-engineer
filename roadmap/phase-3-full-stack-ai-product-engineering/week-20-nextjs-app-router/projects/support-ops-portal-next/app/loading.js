export default function Loading() {
  return (
    <main className="page-grid">
      <section className="panel">
        <div className="panel-heading">
          <h2>Loading route</h2>
          <p>The page shell can appear while slower server work is still resolving.</p>
        </div>
        <div className="loading-skeleton" />
      </section>
    </main>
  );
}
