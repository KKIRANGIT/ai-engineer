import Link from "next/link";
import { Suspense } from "react";
import QueueStatsPanel from "../components/QueueStatsPanel";
import RouteCardGrid from "../components/RouteCardGrid";
import StreamedInsightsPanel from "../components/StreamedInsightsPanel";
import { buildQueueStats, getAllTickets } from "../lib/data";

export default function HomePage() {
  const tickets = getAllTickets();
  const stats = buildQueueStats(tickets);

  return (
    <main className="dashboard-grid">
      <section className="page-grid">
        <section className="panel panel--accent">
          <p className="eyebrow">Dashboard</p>
          <h2 className="page-title">App Router support dashboard</h2>
          <p className="page-lead">
            This page is server-rendered by default. It can assemble data-rich sections
            without turning the whole screen into browser code.
          </p>
          <div className="button-row">
            <Link className="primary-button" href="/tickets">
              Open ticket queue
            </Link>
            <Link className="secondary-button" href="/compose">
              Open intake preview
            </Link>
          </div>
        </section>

        <QueueStatsPanel stats={stats} />
        <RouteCardGrid />
      </section>

      <section className="page-grid">
        <Suspense
          fallback={
            <section className="panel">
              <div className="panel-heading">
                <h2>Generating queue insight</h2>
                <p>
                  This fallback exists so the rest of the dashboard remains visible while
                  the slower insight section resolves.
                </p>
              </div>
              <div className="loading-skeleton" />
            </section>
          }
        >
          <StreamedInsightsPanel />
        </Suspense>
      </section>
    </main>
  );
}
