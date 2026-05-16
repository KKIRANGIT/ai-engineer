"use client";

import { useRouter, useSearchParams } from "next/navigation";
import { useState, useTransition } from "react";

export default function QueueSearchForm({ filters }) {
  const router = useRouter();
  const searchParams = useSearchParams();
  const [isPending, startTransition] = useTransition();
  const [draftSearch, setDraftSearch] = useState(filters.q);

  function pushFilters(nextValues) {
    const params = new URLSearchParams(searchParams.toString());

    const nextEntries = {
      q: nextValues.q,
      status: nextValues.status,
      priority: nextValues.priority,
    };

    for (const [key, value] of Object.entries(nextEntries)) {
      if (!value || value === "all") {
        params.delete(key);
      } else {
        params.set(key, value);
      }
    }

    startTransition(() => {
      router.push(`/tickets?${params.toString()}`);
    });
  }

  return (
    <section className="panel">
      <div className="panel-heading">
        <h2>Queue filters</h2>
        <p>
          This is a client component because it needs router interaction. The tickets page
          around it can remain server-rendered.
        </p>
      </div>

      <div className="filters-grid">
        <label className="field">
          <span>Search</span>
          <input
            type="search"
            value={draftSearch}
            onChange={(event) => setDraftSearch(event.target.value)}
            onBlur={() =>
              pushFilters({
                q: draftSearch,
                status: filters.status,
                priority: filters.priority,
              })
            }
            placeholder="Search title, customer, owner, or tags"
          />
        </label>

        <label className="field">
          <span>Status</span>
          <select
            value={filters.status}
            onChange={(event) =>
              pushFilters({
                q: draftSearch,
                status: event.target.value,
                priority: filters.priority,
              })
            }
          >
            <option value="all">All statuses</option>
            <option value="open">Open</option>
            <option value="in_progress">In progress</option>
            <option value="closed">Closed</option>
          </select>
        </label>

        <label className="field">
          <span>Priority</span>
          <select
            value={filters.priority}
            onChange={(event) =>
              pushFilters({
                q: draftSearch,
                status: filters.status,
                priority: event.target.value,
              })
            }
          >
            <option value="all">All priorities</option>
            <option value="high">High</option>
            <option value="medium">Medium</option>
            <option value="low">Low</option>
          </select>
        </label>
      </div>

      <p className="field-hint">
        {isPending ? "Updating route..." : "Filters are stored in the URL, not hidden local state."}
      </p>
    </section>
  );
}
