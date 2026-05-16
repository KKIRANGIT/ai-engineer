import { useEffect, useMemo, useState } from "react";
import DashboardShell from "./components/DashboardShell.jsx";
import StatsPanel from "./components/StatsPanel.jsx";
import QueueFilters from "./components/QueueFilters.jsx";
import TicketComposer from "./components/TicketComposer.jsx";
import TicketList from "./components/TicketList.jsx";
import SelectedTicketPanel from "./components/SelectedTicketPanel.jsx";
import ActivityFeed from "./components/ActivityFeed.jsx";
import { defaultFilters, seedTickets } from "./sampleData.js";
import {
  buildActivityFeed,
  buildQueueStats,
  createTicketFromDraft,
  filterTickets,
  getSelectedTicket,
} from "./utils.js";

const STORAGE_KEY = "support-workbench-react-state-v1";

function readInitialState() {
  if (typeof window === "undefined") {
    return {
      tickets: seedTickets,
      filters: defaultFilters,
      selectedTicketId: seedTickets[0]?.id ?? null,
    };
  }

  try {
    const rawState = window.localStorage.getItem(STORAGE_KEY);

    if (!rawState) {
      return {
        tickets: seedTickets,
        filters: defaultFilters,
        selectedTicketId: seedTickets[0]?.id ?? null,
      };
    }

    const parsedState = JSON.parse(rawState);

    return {
      tickets: Array.isArray(parsedState.tickets) ? parsedState.tickets : seedTickets,
      filters: parsedState.filters ?? defaultFilters,
      selectedTicketId:
        parsedState.selectedTicketId ?? parsedState.tickets?.[0]?.id ?? seedTickets[0]?.id,
    };
  } catch {
    return {
      tickets: seedTickets,
      filters: defaultFilters,
      selectedTicketId: seedTickets[0]?.id ?? null,
    };
  }
}

function App() {
  const initialState = useMemo(readInitialState, []);

  const [tickets, setTickets] = useState(initialState.tickets);
  const [filters, setFilters] = useState(initialState.filters);
  const [selectedTicketId, setSelectedTicketId] = useState(initialState.selectedTicketId);

  const visibleTickets = filterTickets(tickets, filters);
  const selectedTicket = getSelectedTicket(tickets, selectedTicketId);
  const stats = buildQueueStats(tickets);
  const activities = buildActivityFeed(tickets);

  function handleFilterChange(nextFilters) {
    setFilters(nextFilters);
  }

  function handleCreateTicket(draft) {
    const newTicket = createTicketFromDraft(draft);

    setTickets((currentTickets) => [newTicket, ...currentTickets]);
    setSelectedTicketId(newTicket.id);
  }

  // Persisting UI state is a real external synchronization problem,
  // so an effect is appropriate here.
  useEffect(() => {
    window.localStorage.setItem(
      STORAGE_KEY,
      JSON.stringify({
        tickets,
        filters,
        selectedTicketId,
      }),
    );
  }, [tickets, filters, selectedTicketId]);

  // The browser tab title is also external to React.
  useEffect(() => {
    document.title = `Support Workbench (${stats.active} active)`;
  }, [stats.active]);

  return (
    <DashboardShell
      title="Support Workbench"
      subtitle="A React fundamentals dashboard focused on state ownership, component composition, and controlled interactions."
    >
      <section className="hero-grid">
        <StatsPanel stats={stats} />
        <TicketComposer onCreateTicket={handleCreateTicket} />
      </section>

      <section className="workspace-grid">
        <div className="workspace-column workspace-column--queue">
          <QueueFilters filters={filters} onChange={handleFilterChange} />
          <TicketList
            tickets={visibleTickets}
            selectedTicketId={selectedTicketId}
            onSelectTicket={setSelectedTicketId}
          />
        </div>

        <div className="workspace-column workspace-column--detail">
          <SelectedTicketPanel ticket={selectedTicket} totalVisibleTickets={visibleTickets.length} />
          <ActivityFeed activities={activities} />
        </div>
      </section>
    </DashboardShell>
  );
}

export default App;
