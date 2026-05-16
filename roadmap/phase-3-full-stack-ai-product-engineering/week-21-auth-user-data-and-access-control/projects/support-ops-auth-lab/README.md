# Support Ops Auth Lab

This project models the minimum access-control layer for a workspace-based support product.

## What It Demonstrates

- session creation and request context
- route-level access decisions
- workspace-scoped data visibility
- mutation permissions for members versus admins

## Files

- `src/data-store.js`: sample users, workspaces, and tickets
- `src/auth-model.js`: session creation and lookup helpers
- `src/policies.js`: reusable visibility and mutation rules
- `src/access-service.js`: request-facing operations that combine session and policy logic
- `tests/access-service.test.mjs`: multi-user behavior tests

## Suggested Study Order

1. inspect the sample data
2. read the policy helpers
3. read the request-facing service functions
4. run the tests
5. weaken one rule and watch which test breaks
