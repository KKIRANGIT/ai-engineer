import { useState } from "react";

const initialDraft = {
  title: "",
  priority: "medium",
};

function SmallTicketForm() {
  const [draft, setDraft] = useState(initialDraft);
  const [error, setError] = useState("");

  function handleChange(event) {
    const { name, value } = event.target;
    setDraft((currentDraft) => ({
      ...currentDraft,
      [name]: value,
    }));
  }

  function handleSubmit(event) {
    event.preventDefault();

    if (draft.title.trim().length < 5) {
      setError("Title must be at least 5 characters long.");
      return;
    }

    setError("");
    console.log("Submit ticket draft:", draft);
    setDraft(initialDraft);
  }

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="title">Title</label>
      <input id="title" name="title" value={draft.title} onChange={handleChange} />

      <label htmlFor="priority">Priority</label>
      <select
        id="priority"
        name="priority"
        value={draft.priority}
        onChange={handleChange}
      >
        <option value="low">Low</option>
        <option value="medium">Medium</option>
        <option value="high">High</option>
      </select>

      {error ? <p>{error}</p> : null}
      <button type="submit">Create ticket</button>
    </form>
  );
}

export default SmallTicketForm;
