import { buildQueueInsight, getAllTickets } from "../lib/data";
import { delay } from "../lib/delay";

export default async function StreamedInsightsPanel() {
  // The artificial delay exists only to make streaming behavior visible in the learning workspace.
  await delay(900);

  const insight = buildQueueInsight(getAllTickets());

  return (
    <section className="panel">
      <div className="panel-heading">
        <h2>Server-generated queue insight</h2>
        <p>This async server component resolves later without blocking the whole dashboard shell.</p>
      </div>

      <div className="preview-box">
        <h3>{insight.headline}</h3>
        <p>{insight.summary}</p>
        <div className="meta-row">
          <span className="tag">{insight.focusArea}</span>
          <span className="tag">{insight.nextAction}</span>
        </div>
      </div>
    </section>
  );
}
