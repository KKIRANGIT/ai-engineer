import IntakePreviewForm from "../../components/IntakePreviewForm";

export default function ComposePage() {
  return (
    <main className="compose-grid">
      <section className="panel panel--accent">
        <p className="eyebrow">Client interaction</p>
        <h2 className="page-title">Intake preview</h2>
        <p className="page-lead">
          This route stays server-rendered overall, but the form itself is a client island
          because it needs browser state, submit behavior, and progressive feedback.
        </p>
        <p className="field-hint">
          The form posts JSON to a route handler that validates the request and returns a
          deterministic triage preview.
        </p>
      </section>

      <IntakePreviewForm />
    </main>
  );
}
