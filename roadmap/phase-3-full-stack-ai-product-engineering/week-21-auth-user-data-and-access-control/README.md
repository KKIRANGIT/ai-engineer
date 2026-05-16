# Week 21: Auth, User Data, and Access Control

Back to [Phase 3](../README.md)

## Goal

Turn your application from a single-user prototype into a real multi-user product with meaningful account boundaries and user-specific data ownership.

This week is about trust boundaries, not only login screens.

## Why This Week Matters

Many portfolio apps are secretly single-user demos wearing a login screen. This week fixes that.

A real product needs:

- authentication
- session handling
- user-specific data boundaries
- route and action protection
- clear ownership of created content

AI products amplify the importance of this because they often store:

- private documents
- usage history
- generated artifacts
- billing state
- operator activity

Weak access control makes the whole product untrustworthy fast.

## What This Week Is Actually Training

Week 21 is training five deeper skills:

1. separating authentication from authorization
2. designing a user or workspace ownership model intentionally
3. scoping reads and writes to the correct account boundary
4. protecting routes and server-side actions together
5. testing multi-user behavior instead of trusting visual hiding

The real outcome is not "I added auth." The real outcome is "I can enforce who can access what and explain why."

## Scope Boundary For This Week

This week focuses on:

- identity terminology
- sessions and request context
- protected routes and actions
- per-user and per-workspace ownership rules
- data scoping
- threat review for common access mistakes

This week does not require:

- enterprise SSO
- complex organization admin tooling
- fine-grained attribute-based policy engines
- production-ready secrets rotation

The correct goal is to become reliable at multi-user fundamentals before the product adds billing, jobs, and usage accounting.

## Week 21 Outcomes

By the end of this week, you should be able to:

- implement a working auth flow mentally and structurally
- understand session and identity basics
- attach app data to the correct user or workspace
- protect routes and server actions appropriately
- reason about access control beyond "user is logged in"
- explain where record-level restrictions belong

## Best Source Strategy For This Week

Use sources in this order:

1. the local Week 21 workspace
2. official auth and platform documentation for the stack you use
3. your own access-control model notes

Do not learn this week from UI-only auth tutorials. They usually hide the actual authorization problem.

## Recommended Official References

Use these official sources as the primary external reference stack:

- Next.js authentication guide: <https://nextjs.org/docs/app/guides/authentication>
- Supabase auth overview: <https://supabase.com/docs/guides/auth>
- Clerk docs overview: <https://clerk.com/docs>
- OWASP authorization cheat sheet: <https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html>

These are enough to reinforce the concepts without creating source overload.

## Recommended Project Direction For This Workspace

This workspace uses one realistic but manageable product scenario:

- a support operations access lab

Why this direction was chosen:

- it naturally exposes user vs workspace ownership
- it creates both read and write permissions
- it gives protected route rules a concrete purpose
- it sets up later billing, usage, and admin concerns cleanly

## Project Capabilities This Week Includes

The Week 21 project includes:

- sample users, workspaces, and tickets
- session creation and request-context helpers
- route-level access checks
- record-level ticket visibility rules
- mutation permissions for assignees and admins
- Node-based tests for multi-user behavior

The project stays provider-agnostic on purpose so the ownership logic remains visible.

## Recommended Build Sequence

1. define the identity and session vocabulary
2. map who owns each record
3. write route-level access rules
4. write record-level visibility rules
5. write mutation rules for admin vs member behavior
6. test cross-user and cross-workspace scenarios

## Recommended Daily Breakdown

### Day 1: Identity and session model

### Day 2: Protected route thinking

### Day 3: User-owned data and scoping rules

### Day 4: Mutation permissions and threat review

### Day 5: Multi-user tests

### Day 6: Refactor the policy layer

### Day 7: Document the access model

## Hands-On Workspace Structure

```text
week-21-auth-user-data-and-access-control/
|-- README.md
|-- exercises/
|   |-- README.md
|   |-- access-review/
|   |-- identity-and-sessions/
|   `-- user-data-boundaries/
|-- notes/
|   |-- 01-week-plan.md
|   |-- 02-access-control-model.md
|   `-- 03-multi-user-test-scenarios.md
`-- projects/
    `-- support-ops-auth-lab/
```

## Exercises

The exercises isolate the decisions that developers usually blur together.

You will practice:

- separating identity, session, and authorization language
- scoping data to the current user or workspace
- reviewing a feature for hidden access-control failure paths

Start here:

- [Exercises README](exercises/README.md)

## Main Project

Project:

- [support-ops-auth-lab](projects/support-ops-auth-lab/README.md)

This project is a small access-control lab for a support product. It teaches:

- session-aware request handling
- workspace-scoped data visibility
- mutation permissions by role
- the difference between route access and data access

It is intentionally small enough that the policy rules stay easy to inspect.

## Deliverables

By the end of this week, you should have:

- one complete auth and access-control workspace
- one tested project showing user and workspace scoping
- one access-control model note
- one multi-user test checklist you can reuse later

## Exit Criteria

You are ready to move to Week 22 only if:

- different users cannot see each other's restricted data
- you can explain where authentication ends and authorization begins
- you can justify your ownership model
- server-side checks back up any UI-level protection
- you have tested at least one cross-user failure scenario

## Common Mistakes To Avoid

- treating login status as the only security concern
- forgetting to scope queries to the current user or workspace
- relying only on frontend checks
- hiding a button and calling it access control
- mixing route guards and record permissions into one vague rule

## Expert Notes That Matter Early

### Identity design affects everything downstream

Once billing, analytics, and AI usage exist, poor user modeling becomes expensive to fix.

### Access control is a systems concern

It must be true across UI, backend, and data.

### Multi-user tests reveal reality

If your product has never been exercised with conflicting users, you do not yet know whether access is correct.

## Final Standard For This Week

The correct outcome of Week 21 is not:

"I added auth."

The correct outcome is:

"I turned a prototype into a real multi-user product with meaningful user ownership and enforceable access boundaries."
