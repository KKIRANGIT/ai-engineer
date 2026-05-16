import test from "node:test";
import assert from "node:assert/strict";
import {
  buildActivityFeed,
  buildQueueStats,
  createTicketFromDraft,
  filterTickets,
  getSelectedTicket,
  validateTicketDraft,
} from "../src/utils.js";
import { seedTickets } from "../src/sampleData.js";

test("validateTicketDraft reports useful field-level errors", () => {
  const errors = validateTicketDraft({
    title: "Short",
    customer: "",
    priority: "high",
    channel: "email",
    summary: "Too short",
    description: "Not enough detail yet.",
    owner: "",
  });

  assert.ok(errors.title);
  assert.ok(errors.customer);
  assert.ok(errors.summary);
  assert.ok(errors.description);
  assert.ok(errors.owner);
});

test("createTicketFromDraft normalizes input and builds a new ticket", () => {
  const ticket = createTicketFromDraft(
    {
      title: "  Refund workflow failed  ",
      customer: "  Acme  ",
      priority: "high",
      channel: "chat",
      summary: "  Customer cannot finish refund action  ",
      description:
        "  The refund action keeps failing after finance confirmed the duplicate charge.  ",
      owner: "  Priya  ",
    },
    new Date("2026-05-10T08:00:00.000Z"),
  );

  assert.equal(ticket.title, "Refund workflow failed");
  assert.equal(ticket.customer, "Acme");
  assert.equal(ticket.owner, "Priya");
  assert.equal(ticket.status, "open");
  assert.equal(ticket.createdAt, "2026-05-10");
});

test("filterTickets applies search and status filters from one source of truth", () => {
  const visibleTickets = filterTickets(seedTickets, {
    search: "refund",
    status: "open",
    priority: "all",
  });

  assert.equal(visibleTickets.length, 1);
  assert.equal(visibleTickets[0].id, "T-2001");
});

test("buildQueueStats derives queue numbers correctly", () => {
  const stats = buildQueueStats(seedTickets);

  assert.equal(stats.total, 4);
  assert.equal(stats.open, 2);
  assert.equal(stats.active, 3);
  assert.equal(stats.highPriority, 2);
});

test("buildActivityFeed keeps the newest tickets first", () => {
  const activities = buildActivityFeed(seedTickets);

  assert.equal(activities.length, 4);
  assert.equal(activities[0].title, "SLA escalation warning triggered too early");
});

test("getSelectedTicket resolves the selected object from the id", () => {
  const ticket = getSelectedTicket(seedTickets, "T-2002");

  assert.equal(ticket?.customer, "Northstar Health");
});
