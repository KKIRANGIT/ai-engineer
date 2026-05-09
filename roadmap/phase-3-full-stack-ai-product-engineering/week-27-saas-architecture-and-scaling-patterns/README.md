# Week 27: SaaS Architecture and Scaling Patterns

Back to [Phase 3](../README.md)

## Goal

Think about your product like a system designer: where boundaries should live, what the scaling risks are, and how product complexity should shape architecture.

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

This week teaches you to step back and ask:

- what are the core components
- how do they communicate
- what breaks first under growth
- what should remain simple for now

## Week 27 Outcomes

By the end of this week, you should be able to:

- explain a small SaaS architecture clearly
- reason about multi-tenant boundaries
- identify bottlenecks and scaling risks
- think about caching, feature flags, and secrets management at a practical level
- produce one architecture document that is actually useful

## What To Learn

## 1. System boundaries

Learn to identify:

- frontend
- app server
- background workers
- database
- third-party services
- AI providers

## 2. Multi-tenant thinking

Even if your app is early-stage, understand:

- tenant isolation
- user vs workspace ownership
- data partitioning assumptions

## 3. Caching and performance

At a practical level:

- what can be cached
- what should stay fresh
- where stale data would be dangerous

## 4. Feature flags and rollout safety

Learn why staged rollout and controlled release matter, especially for expensive or experimental AI features.

## 5. Secrets and config boundaries

You should know where secrets live and which runtime parts should or should not see them.

## Best Learning Sequence For This Week

1. architecture mapping
2. tenant model
3. bottleneck analysis
4. caching and rollout
5. architecture documentation

## Recommended Daily Breakdown

### Day 1: Map the current system

### Day 2: Identify boundaries and dependencies

### Day 3: Identify bottlenecks and expensive paths

### Day 4: Multi-tenant and access review

### Day 5: Caching and rollout strategy

### Day 6: Write the architecture doc

### Day 7: Explain it aloud and refine

## Build Plan

Produce one concise architecture package for your product that includes:

- major components
- data flow
- user and tenant model
- AI request flow
- job flow
- observability points
- likely bottlenecks

## Deliverables

- architecture document
- one diagram
- one bottleneck/risk list

## Exit Criteria

- you can discuss the system at design-review level
- you can identify likely scaling and reliability pain points
- you can explain why the architecture is appropriate for the current stage

## Common Mistakes To Avoid

- overengineering a tiny product
- ignoring tenant and ownership implications
- skipping documentation because "the code explains it"
- assuming scaling means only traffic, not workflow complexity

## Expert Notes That Matter Early

### Good architecture is stage-aware

It matches current product reality and leaves room to evolve.

### Documentation clarifies design

If you cannot draw and explain the system, you probably do not understand it well enough yet.

## Final Standard For This Week

The correct outcome of Week 27 is not "I made an architecture diagram."

The correct outcome is:

"I can explain the current system, its boundaries, its likely bottlenecks, and why its architecture fits the product's stage."
