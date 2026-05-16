function QueueFilters({ filters, onChange }) {
  function handleFieldChange(event) {
    const { name, value } = event.target;

    onChange({
      ...filters,
      [name]: value,
    });
  }

  return (
    <section className="panel">
      <div className="panel-heading">
        <h2>Queue filters</h2>
        <p>These inputs are controlled by the parent because multiple sections depend on them.</p>
      </div>

      <div className="filters-grid">
        <label className="field">
          <span>Search</span>
          <input
            type="search"
            name="search"
            value={filters.search}
            onChange={handleFieldChange}
            placeholder="Search title, owner, customer, or tags"
          />
        </label>

        <label className="field">
          <span>Status</span>
          <select name="status" value={filters.status} onChange={handleFieldChange}>
            <option value="all">All statuses</option>
            <option value="open">Open</option>
            <option value="in_progress">In progress</option>
            <option value="closed">Closed</option>
          </select>
        </label>

        <label className="field">
          <span>Priority</span>
          <select name="priority" value={filters.priority} onChange={handleFieldChange}>
            <option value="all">All priorities</option>
            <option value="high">High</option>
            <option value="medium">Medium</option>
            <option value="low">Low</option>
          </select>
        </label>
      </div>
    </section>
  );
}

export default QueueFilters;
