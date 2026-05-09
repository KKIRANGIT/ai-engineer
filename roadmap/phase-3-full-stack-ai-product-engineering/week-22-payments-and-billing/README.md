# Week 22: Payments and Billing

Back to [Phase 3](../README.md)

## Goal

Learn the commercial control plane of SaaS products: plans, subscriptions, billing state, and payment-driven access.

## Why This Week Matters

An app that can create value but cannot gate, meter, or bill for that value is still incomplete as a SaaS product.

This week matters because real products need to answer:

- who is free vs paid
- what happens when a payment succeeds
- what happens when it fails
- what limits apply by plan
- how billing state updates the product automatically

## Week 22 Outcomes

By the end of this week, you should be able to:

- model free and paid plans
- understand Stripe product/price/subscription concepts
- implement checkout flow
- handle webhook-driven billing state changes
- gate features or quotas by plan
- explain how billing state reaches your application reliably

## What To Learn

## 1. Billing mental model

Think in:

- product
- price
- customer
- subscription
- billing state

This is an application-state problem, not just a payments problem.

## 2. Checkout and purchase flow

You should understand:

- how a user begins checkout
- what data your app needs before and after checkout
- what success and cancellation paths look like

## 3. Webhooks and source of truth

Billing state should not be driven only by what the frontend thinks happened.

Learn why webhooks matter:

- they communicate authoritative payment events
- they keep app access in sync with Stripe state

## 4. Plan gating

You should think about:

- which features are free
- which features are paid
- whether limits are boolean or usage-based

This will connect directly to Week 26.

## 5. Billing portal and lifecycle

Users need to:

- upgrade
- downgrade
- cancel
- view or manage billing details

Good SaaS products treat billing operations as part of user experience, not only admin work.

## Best Learning Sequence For This Week

1. billing entities
2. checkout flow
3. webhook model
4. plan gating
5. lifecycle management

## Recommended Daily Breakdown

### Day 1: Stripe mental model

### Day 2: Checkout flow

### Day 3: Webhooks

### Day 4: Plan-based access logic

### Day 5: Billing portal and lifecycle handling

### Day 6: Multi-scenario testing

### Day 7: Document state transitions

## Build Plan

Add billing to an app with:

- free plan
- paid plan
- checkout
- webhook updates
- gated feature or quota

## Deliverables

- working billing flow in test mode
- one note describing billing-state transitions
- one mapping of plan to product behavior

## Exit Criteria

- you can explain how the app knows a user is paid
- you can explain why webhooks matter
- you can gate access based on billing state cleanly

## Common Mistakes To Avoid

- trusting only the frontend redirect result
- mixing billing logic directly into presentation code
- failing to define what paid users actually get

## Expert Notes That Matter Early

### Billing is access control plus state management

Money events change product permissions. Treat them as system events.

### Product clarity matters

Your app should make plan differences understandable, not hidden.

## Final Standard For This Week

The correct outcome of Week 22 is not "I connected Stripe."

The correct outcome is:

"I can model plans, handle subscription state correctly, and connect billing events to real product access."
