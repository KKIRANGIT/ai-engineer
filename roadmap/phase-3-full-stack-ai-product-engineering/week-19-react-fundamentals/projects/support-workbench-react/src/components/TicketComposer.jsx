import { useState } from "react";
import { emptyDraft } from "../sampleData.js";
import { validateTicketDraft } from "../utils.js";

function TicketComposer({ onCreateTicket }) {
  const [draft, setDraft] = useState(emptyDraft);
  const [errors, setErrors] = useState({});

  function handleChange(event) {
    const { name, value } = event.target;

    setDraft((currentDraft) => ({
      ...currentDraft,
      [name]: value,
    }));
  }

  function handleSubmit(event) {
    event.preventDefault();

    const nextErrors = validateTicketDraft(draft);
    setErrors(nextErrors);

    if (Object.keys(nextErrors).length > 0) {
      return;
    }

    onCreateTicket(draft);
    setDraft(emptyDraft);
    setErrors({});
  }

  return (
    <section className="panel panel--accent">
      <div className="panel-heading">
        <h2>Create ticket</h2>
        <p>This form owns its own draft state because the rest of the app does not need every keystroke.</p>
      </div>

      <form className="composer-form" onSubmit={handleSubmit}>
        <label className="field">
          <span>Ticket title</span>
          <input name="title" value={draft.title} onChange={handleChange} />
          {errors.title ? <small className="field-error">{errors.title}</small> : null}
        </label>

        <label className="field">
          <span>Customer</span>
          <input name="customer" value={draft.customer} onChange={handleChange} />
          {errors.customer ? <small className="field-error">{errors.customer}</small> : null}
        </label>

        <div className="two-column-fields">
          <label className="field">
            <span>Priority</span>
            <select name="priority" value={draft.priority} onChange={handleChange}>
              <option value="low">Low</option>
              <option value="medium">Medium</option>
              <option value="high">High</option>
            </select>
          </label>

          <label className="field">
            <span>Channel</span>
            <select name="channel" value={draft.channel} onChange={handleChange}>
              <option value="email">Email</option>
              <option value="chat">Chat</option>
              <option value="voice">Voice</option>
            </select>
          </label>
        </div>

        <label className="field">
          <span>Summary</span>
          <textarea name="summary" rows="2" value={draft.summary} onChange={handleChange} />
          {errors.summary ? <small className="field-error">{errors.summary}</small> : null}
        </label>

        <label className="field">
          <span>Description</span>
          <textarea
            name="description"
            rows="4"
            value={draft.description}
            onChange={handleChange}
          />
          {errors.description ? (
            <small className="field-error">{errors.description}</small>
          ) : null}
        </label>

        <label className="field">
          <span>Owner</span>
          <input name="owner" value={draft.owner} onChange={handleChange} />
          {errors.owner ? <small className="field-error">{errors.owner}</small> : null}
        </label>

        <button className="primary-button" type="submit">
          Add ticket to queue
        </button>
      </form>
    </section>
  );
}

export default TicketComposer;
