# Week 22: Payments and Billing

Back to [Phase 3](../README.md)

## Goal

Learn the commercial control plane of SaaS products: plans, subscriptions, billing state, and payment-driven access.

This week is about product state and entitlements, not only payment collection.

## Why This Week Matters

An app that can create value but cannot gate, meter, or bill for that value is still incomplete as a SaaS product.

This week matters because real products need to answer:

- who is free vs paid
- what happens when a payment succeeds
- what happens when it fails
- what limits apply by plan
- how billing state updates the product automatically

## What This Week Is Actually Training

Week 22 is training five deeper skills:

1. modeling plans and product entitlements explicitly
2. understanding how checkout starts and what state it returns
3. treating webhooks as the authoritative subscription event stream
4. translating subscription state into feature access
5. separating billing logic from presentation code

The real outcome is not "I connected Stripe." The real outcome is "I can explain how money events become product permissions."

## Scope Boundary For This Week

This week focuses on:

- plan modeling
- checkout flow shape
- subscription lifecycle states
- webhook-driven updates
- feature or quota gating
- billing portal mental model

This week does not require:

- tax complexity
- invoicing edge cases for large enterprise contracts
- custom metered billing systems
- advanced revenue reporting

The correct goal is to understand subscription state cleanly before Week 26 adds deeper usage economics.

## Week 22 Outcomes

By the end of this week, you should be able to:

- model free and paid plans
- understand Stripe product, price, and subscription concepts
- implement checkout flow conceptually
- handle webhook-driven billing state changes
- gate features or quotas by plan
- explain how billing state reaches your application reliably

## Best Source Strategy For This Week

Use sources in this order:

1. the local Week 22 workspace
2. official Stripe billing documentation
3. your own notes mapping plan state to product behavior

Do not learn billing only from frontend redirect tutorials. They hide the actual source-of-truth problem.

## Recommended Official References

Use these official sources as the primary external reference stack:

- Stripe billing overview: <https://docs.stripe.com/billing>
- Stripe Checkout: <https://docs.stripe.com/payments/checkout>
- Stripe webhooks: <https://docs.stripe.com/webhooks>
- Stripe customer portal: <https://docs.stripe.com/customer-management>

These references are enough to ground the week without overwhelming the study flow.

## Recommended Project Direction For This Workspace

This workspace uses one realistic but manageable product scenario:

- a support operations billing lab

Why this direction was chosen:

- it connects naturally to multi-user product access
- it makes plan gating concrete
- it gives webhook events a clear purpose
- it sets up later usage tracking and SaaS architecture work

## Project Capabilities This Week Includes

The Week 22 project includes:

- plan definitions for free and team tiers
- a checkout-session payload builder
- a subscription-state reducer driven by webhook-like events
- entitlement derivation from billing state
- tests for lifecycle transitions and feature gating

The project stays vendor-light and local on purpose so the billing logic stays inspectable.

## Recommended Build Sequence

1. define plans and entitlements
2. define the checkout request payload
3. map the subscription lifecycle states
4. handle webhook events into local billing state
5. derive feature access from state instead of hardcoding it in UI
6. test success, failure, and cancellation flows

## Recommended Daily Breakdown

### Day 1: Stripe mental model

### Day 2: Checkout shape

### Day 3: Webhook event flow

### Day 4: Plan gating

### Day 5: Lifecycle edge cases

### Day 6: Multi-scenario tests

### Day 7: Document the state transitions

## Hands-On Workspace Structure

```text
week-22-payments-and-billing/
|-- README.md
|-- exercises/
|   |-- README.md
|   |-- billing-model/
|   |-- plan-gating/
|   `-- webhook-state/
|-- notes/
|   |-- 01-week-plan.md
|   |-- 02-billing-state-map.md
|   `-- 03-plan-gating-review.md
`-- projects/
    `-- support-ops-billing-lab/
```

## Exercises

The exercises isolate the billing decisions that usually get hidden behind SDK steps.

You will practice:

- modeling plans and feature differences
- thinking through billing state transitions
- defining what paid access actually changes in the product

Start here:

- [Exercises README](exercises/README.md)

## Main Project

Project:

- [support-ops-billing-lab](projects/support-ops-billing-lab/README.md)

This project is a small billing-state lab for a SaaS support product. It teaches:

- plan and entitlement modeling
- webhook-driven subscription updates
- checkout payload design
- feature gating from billing state

It is intentionally compact so the billing logic remains easier to reason about than a full provider integration.

## Deliverables

By the end of this week, you should have:

- one complete billing workspace
- one tested billing-state project
- one plan-to-entitlement map
- one state-transition note covering success, failure, downgrade, and cancellation paths

## Exit Criteria

You are ready to move to Week 23 only if:

- you can explain how the app knows a user is paid
- you can explain why webhooks matter
- you can point to a single place where entitlements are derived
- your plan differences are explicit instead of implied
- you can describe how failure or cancellation changes access

## Common Mistakes To Avoid

- trusting only the frontend redirect result
- mixing billing rules directly into presentation code
- failing to define what paid users actually get
- treating plan names as entitlements instead of mapping behavior explicitly

## Expert Notes That Matter Early

### Billing is access control plus state management

Money events change product permissions. Treat them as system events.

### Product clarity matters

Your app should make plan differences understandable, not hidden.

### Webhooks protect reality

The product should believe the provider's event stream more than a hopeful browser redirect.

## Final Standard For This Week

The correct outcome of Week 22 is not:

"I connected Stripe."

The correct outcome is:

"I can model plans, handle subscription state correctly, and connect billing events to real product access."
