import test from "node:test";
import assert from "node:assert/strict";

import { createSession } from "../src/auth-model.js";
import { listVisibleTickets, requireRoute, updateTicketStatus } from "../src/access-service.js";

test("members only see tickets from their workspace", () => {
  const session = createSession("u-bob");
  const visible = listVisibleTickets(session.token);

  assert.equal(visible.length, 2);
  assert.ok(visible.every((ticket) => ticket.workspaceId === "w-acme"));
});

test("admins can access admin-only routes", () => {
  const session = createSession("u-alice");
  const result = requireRoute(session.token, "billing");

  assert.equal(result.role, "admin");
});

test("members are blocked from admin-only routes", () => {
  const session = createSession("u-bob");

  assert.throws(() => requireRoute(session.token, "billing"), /Access denied/);
});

test("assignees can mutate their own ticket", () => {
  const session = createSession("u-bob");
  const updated = updateTicketStatus(session.token, "t-101", "resolved");

  assert.equal(updated.status, "resolved");
});

test("cross-workspace mutation is denied", () => {
  const session = createSession("u-bob");

  assert.throws(() => updateTicketStatus(session.token, "t-201", "resolved"), /Mutation denied/);
});
