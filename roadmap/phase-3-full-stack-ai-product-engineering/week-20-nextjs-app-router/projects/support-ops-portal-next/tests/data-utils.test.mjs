import test from "node:test";
import assert from "node:assert/strict";
import {
  buildQueueInsight,
  buildQueueStats,
  filterTickets,
  getAllTickets,
  getTicketById,
  normalizeTicketFilters,
} from "../lib/data.js";
import { buildIntakePreview, validateIntakeDraft } from "../lib/intake.js";

test("normalizeTicketFilters applies stable defaults", () => {
  const filters = normalizeTicketFilters({});

  assert.deepEqual(filters, {
    q: "",
    status: "all",
    priority: "all",
  });
});

test("filterTickets narrows the queue using URL-style filters", () => {
  const tickets = filterTickets(getAllTickets(), {
    q: "billing",
    status: "open",
    priority: "high",
  });

  assert.equal(tickets.length, 1);
  assert.equal(tickets[0].id, "T-3001");
});

test("buildQueueStats derives counts from one ticket source", () => {
  const stats = buildQueueStats(getAllTickets());

  assert.equal(stats.total, 4);
  assert.equal(stats.open, 2);
  assert.equal(stats.active, 3);
  assert.equal(stats.highPriority, 2);
});

test("getTicketById resolves a dynamic route parameter", () => {
  const ticket = getTicketById("T-3002");

  assert.equal(ticket?.customer, "Northstar Health");
});

test("buildQueueInsight highlights a high-priority focus area", () => {
  const insight = buildQueueInsight(getAllTickets());

  assert.match(insight.headline, /high-priority/i);
  assert.match(insight.summary, /active ticket/);
});

test("validateIntakeDraft reports meaningful server-side request errors", () => {
  const errors = validateIntakeDraft({
    title: "Short",
    customer: "",
    severity: "high",
    problem: "Too short",
  });

  assert.ok(errors.title);
  assert.ok(errors.customer);
  assert.ok(errors.problem);
});

test("buildIntakePreview produces a deterministic triage preview", () => {
  const preview = buildIntakePreview({
    title: "Refund action blocked",
    customer: "Acme Logistics",
    severity: "high",
    problem: "Billing retry loop keeps the refund action pending for the customer account.",
  });

  assert.match(preview.headline, /Urgent review/);
  assert.match(preview.recommendedOwner, /finance operations/i);
});
