"use client";

import { useState, useTransition } from "react";

const initialDraft = {
  title: "",
  customer: "",
  severity: "medium",
  problem: "",
};

export default function IntakePreviewForm() {
  const [draft, setDraft] = useState(initialDraft);
  const [preview, setPreview] = useState(null);
  const [error, setError] = useState("");
  const [isPending, startTransition] = useTransition();

  function handleChange(event) {
    const { name, value } = event.target;

    setDraft((currentDraft) => ({
      ...currentDraft,
      [name]: value,
    }));
  }

  function handleSubmit(event) {
    event.preventDefault();
    setError("");

    startTransition(async () => {
      const response = await fetch("/api/intake-preview", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(draft),
      });

      const payload = await response.json();

      if (!response.ok) {
        setPreview(null);
        setError(
          payload.errors
            ? Object.values(payload.errors).join(" ")
            : "Preview request failed.",
        );
        return;
      }

      setPreview(payload.preview);
    });
  }

  return (
    <section className="panel">
      <div className="panel-heading">
        <h2>Draft intake preview</h2>
        <p>
          The browser owns the draft state. The server route handler owns validation and
          response generation.
        </p>
      </div>

      <form className="page-grid" onSubmit={handleSubmit}>
        <label className="field">
          <span>Title</span>
          <input name="title" value={draft.title} onChange={handleChange} />
        </label>

        <label className="field">
          <span>Customer</span>
          <input name="customer" value={draft.customer} onChange={handleChange} />
        </label>

        <label className="field">
          <span>Severity</span>
          <select name="severity" value={draft.severity} onChange={handleChange}>
            <option value="low">Low</option>
            <option value="medium">Medium</option>
            <option value="high">High</option>
          </select>
        </label>

        <label className="field">
          <span>Problem statement</span>
          <textarea
            name="problem"
            rows="5"
            value={draft.problem}
            onChange={handleChange}
          />
        </label>

        <button className="primary-button" disabled={isPending} type="submit">
          {isPending ? "Generating preview..." : "Generate preview"}
        </button>
      </form>

      {error ? <div className="error-box">{error}</div> : null}

      {preview ? (
        <div className="preview-box">
          <h3>{preview.headline}</h3>
          <p>{preview.summary}</p>
          <div className="meta-row">
            <span className="tag">{preview.recommendedOwner}</span>
            <span className="tag">{preview.priorityLabel}</span>
            <span className="tag">{preview.nextAction}</span>
          </div>
        </div>
      ) : null}
    </section>
  );
}
