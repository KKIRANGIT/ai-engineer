# Week 21: Auth, User Data, and Access Control

Back to [Phase 3](../README.md)

## Goal

Turn your application from a single-user prototype into a real multi-user product with meaningful account boundaries and user-specific data ownership.

## Why This Week Matters

Many portfolio apps are secretly single-user demos wearing a login screen. This week fixes that.

A real product needs:

- authentication
- session handling
- user-specific data boundaries
- access checks
- clear ownership of created content

This week is important because AI products often handle:

- private documents
- usage history
- billing state
- generated artifacts

Weak access control makes the product untrustworthy fast.

## Week 21 Outcomes

By the end of this week, you should be able to:

- implement a working auth flow
- understand session and identity basics
- attach app data to the correct user
- protect routes and server actions appropriately
- reason about access control beyond "user is logged in"
- explain where row-level or record-level restrictions belong

## What To Learn

## 1. Identity, session, and authorization

Distinguish clearly:

- authentication: who are you
- authorization: what are you allowed to access
- session: how does the system remember you across requests

Confusing these concepts causes weak product design.

## 2. Auth flows

You should understand:

- email/password or passwordless basics
- OAuth basics
- login, signup, logout flow
- protected routes or views

The goal is not to implement every possible auth method. It is to understand the product and backend implications of identity.

## 3. User data ownership

Every important record should have a clear ownership model:

- who created it
- who can read it
- who can modify it
- who can delete it

For AI products, this usually includes:

- uploaded documents
- chat history
- generated outputs
- usage or billing records

## 4. Organizations and team models

You do not need full multi-org SaaS complexity this week, but you should understand the concept:

- some products are user-centric
- some are workspace-centric

That architectural choice changes your data model later.

## 5. Access control enforcement

You should think about protection at:

- UI layer
- route or API layer
- data layer

Important rule:

Hiding a button is not access control.

## Best Learning Sequence For This Week

1. auth terminology
2. login/signup flow
3. protected routes
4. user-owned data
5. access enforcement

## Recommended Daily Breakdown

### Day 1: Identity and session model

### Day 2: Auth integration

### Day 3: Protected UI and route boundaries

### Day 4: User-specific records

### Day 5: Access checks and threat review

### Day 6: Multi-user test scenarios

### Day 7: Documentation and edge-case review

## Build Plan

Add auth to an existing app and ensure:

- users can sign in and out
- protected routes are enforced
- each user sees only their own data
- server-side checks back up UI-level behavior

## Deliverables

- working auth flow
- per-user data isolation
- one note documenting your access-control model

## Exit Criteria

- different users cannot see each other's data
- you can explain where auth ends and authorization begins
- your app enforces access beyond visual hiding alone

## Common Mistakes To Avoid

- treating login status as the only security concern
- forgetting to scope queries to the current user
- relying only on frontend checks
- storing sensitive user context in the wrong place

## Expert Notes That Matter Early

### Identity design affects everything downstream

Once billing, analytics, and AI usage exist, poor user modeling becomes expensive to fix.

### Access control is a systems concern

It must be true across UI, backend, and data.

## Final Standard For This Week

The correct outcome of Week 21 is not "I added auth."

The correct outcome is:

"I turned a prototype into a real multi-user product with meaningful user ownership and enforceable access boundaries."
