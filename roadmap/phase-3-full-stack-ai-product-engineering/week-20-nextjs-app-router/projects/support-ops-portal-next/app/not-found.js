import Link from "next/link";

export default function NotFound() {
  return (
    <main className="page-grid">
      <section className="panel">
        <div className="panel-heading">
          <h2>Ticket not found</h2>
          <p>The requested route parameter did not match an available resource.</p>
        </div>
        <p className="page-lead">
          This is a clearer App Router behavior than silently rendering an empty page.
        </p>
        <Link className="primary-button" href="/tickets">
          Return to tickets
        </Link>
      </section>
    </main>
  );
}
