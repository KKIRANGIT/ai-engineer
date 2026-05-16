# Support Ops Billing Lab

This project models a simple subscription system for a support operations product.

## What It Demonstrates

- plan definitions and limits
- checkout-session payload design
- webhook-driven subscription transitions
- entitlement derivation from billing state

## Files

- `src/plans.js`: plan definitions and included limits
- `src/checkout.js`: checkout payload construction
- `src/webhooks.js`: billing-state reducer for provider events
- `src/entitlements.js`: feature access derived from billing state
- `tests/billing-lab.test.mjs`: lifecycle and entitlement tests

## Suggested Study Order

1. inspect the plan model
2. read the entitlement derivation logic
3. trace the webhook reducer
4. run the tests
5. add a third plan or new limit and observe what changes
