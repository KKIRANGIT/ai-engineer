# Week 27: SaaS Architecture and Scaling Patterns

Back to [Phase 3](../README.md)

## Goal

Think about your product like a system designer: where boundaries should live, what the scaling risks are, and how product complexity should shape architecture.

This week is about stage-aware system design, not diagram theater.

## Why This Week Matters

By this point you have many moving pieces:

- UI
- server logic
- auth
- billing
- AI calls
- jobs
- analytics

Without architectural thinking, these pieces become an accidental system.

## What This Week Is Actually Training

Week 27 is training five deeper skills:

1. mapping major system boundaries clearly
2. reasoning about user, workspace, and tenant models
3. identifying the first scaling and reliability bottlenecks
4. choosing where caching, rollout controls, and config boundaries belong
5. writing architecture notes that are useful in a review, not decorative

The real outcome is not "I made a diagram." The real outcome is "I can explain why this product is shaped the way it is."

## Scope Boundary For This Week

This week focuses on:

- component boundaries
- multi-tenant thinking
- bottleneck analysis
- caching and rollout decisions
- secrets and configuration boundaries

This week does not require:

- premature microservice decomposition
- deep infrastructure automation
- hyperscale traffic assumptions
- exhaustive performance benchmarking

The correct goal is to design the architecture that fits the current stage while leaving clear evolution paths.

## Week 27 Outcomes

By the end of this week, you should be able to:

- explain a small SaaS architecture clearly
- reason about multi-tenant boundaries
- identify bottlenecks and scaling risks
- think about caching, feature flags, and secrets management at a practical level
- produce one architecture document that is actually useful

## Best Source Strategy For This Week

Use sources in this order:

1. the local Week 27 workspace
2. official deployment and security references
3. your own architecture notes and risk list

Do not design for imaginary scale. Design for the product you actually have and the next complexity step you expect.

## Recommended Official References

Use these companion references when you want external anchors:

- Next.js deployment guide: <https://nextjs.org/docs/app/guides/deployment>
- OWASP secrets management cheat sheet: <https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html>
- OpenTelemetry concepts: <https://opentelemetry.io/docs/concepts/>

These are enough to reinforce the architectural concerns without dragging the week into platform sprawl.

## Recommended Project Direction For This Workspace

This workspace uses one realistic but manageable product scenario:

- a support operations architecture kit

Why this direction was chosen:

- it connects directly to the product built across Weeks 19 to 26
- it forces a user and workspace model to stay explicit
- it creates a concrete place to analyze expensive AI paths
- it makes rollout and secrets boundaries easier to discuss

## Project Capabilities This Week Includes

The Week 27 project includes:

- an architecture package with overview, bottlenecks, and rollout notes
- small helpers for topology, cache-policy decisions, and feature rollout
- tests for architecture helper behavior

The project stays compact on purpose so the architectural reasoning is easier to inspect than the infrastructure stack.

## Recommended Build Sequence

1. map the major components
2. define user and tenant boundaries
3. trace the AI request and job paths
4. identify the most expensive or fragile flows
5. define cache, rollout, and secrets boundaries
6. write the architecture package

## Recommended Daily Breakdown

### Day 1: Map the current system

### Day 2: Tenant and ownership review

### Day 3: Bottleneck analysis

### Day 4: Caching and config boundaries

### Day 5: Feature rollout strategy

### Day 6: Write the architecture package

### Day 7: Review and refine the design explanation

## Hands-On Workspace Structure

```text
week-27-saas-architecture-and-scaling-patterns/
|-- README.md
|-- exercises/
|   |-- README.md
|   |-- rollout-and-config/
|   |-- system-boundaries/
|   `-- tenant-thinking/
|-- notes/
|   |-- 01-week-plan.md
|   |-- 02-architecture-review-template.md
|   `-- 03-bottleneck-notes.md
`-- projects/
    `-- support-ops-architecture-kit/
```

## Exercises

The exercises isolate the architecture decisions that usually stay in people's heads.

You will practice:

- mapping components and dependencies
- deciding whether ownership is user-centric or workspace-centric
- defining rollout and config boundaries

Start here:

- [Exercises README](exercises/README.md)

## Main Project

Project:

- [support-ops-architecture-kit](projects/support-ops-architecture-kit/README.md)

This project is a lightweight architecture package for a support operations SaaS product. It teaches:

- system mapping
- risk identification
- cache and config judgment
- rollout safety

It is intentionally compact so the design tradeoffs remain easier to inspect than a full deployment stack.

## Deliverables

By the end of this week, you should have:

- one complete architecture workspace
- one architecture package with diagram-level explanation
- one bottleneck and risk list
- one architecture review template you can reuse

## Exit Criteria

You are ready to move to Week 28 only if:

- you can discuss the system at design-review level
- you can identify likely scaling and reliability pain points
- you can justify the tenant and ownership model
- you can explain where secrets and rollout controls belong
- you can explain why the architecture fits the current stage

## Common Mistakes To Avoid

- overengineering a tiny product
- ignoring tenant and ownership implications
- skipping documentation because "the code explains it"
- assuming scaling means only traffic, not workflow complexity
- describing architecture without naming concrete boundaries

## Expert Notes That Matter Early

### Good architecture is stage-aware

It matches current product reality and leaves room to evolve.

### Documentation clarifies design

If you cannot draw and explain the system, you probably do not understand it well enough yet.

### Scaling risk starts before scale

The value of this week is noticing where the product would become painful before the pain arrives in production.

## Final Standard For This Week

The correct outcome of Week 27 is not:

"I made an architecture diagram."

The correct outcome is:

"I can explain the current system, its boundaries, its likely bottlenecks, and why its architecture fits the product's stage."
