# Week 24: Email, Background Jobs, and Durable Execution

Back to [Phase 3](../README.md)

## Goal

Handle long-running AI work correctly so the product stays responsive while slower workflows complete safely in the background.

## Why This Week Matters

AI tasks often take longer than a standard request-response cycle should tolerate.

If you keep everything inline, you get:

- timeouts
- poor UX
- fragile retries
- failed work with no recovery path

This week introduces the operational backbone for serious AI product workflows.

## Week 24 Outcomes

By the end of this week, you should be able to:

- distinguish synchronous request handling from background execution
- understand retries and idempotency conceptually
- design a job-based AI workflow
- notify the user when work completes
- explain why durable execution matters for AI workloads

## What To Learn

## 1. Request path vs background path

Not every user action should finish inside one HTTP request.

Long-running work often belongs in:

- background job system
- durable workflow runner

## 2. Event-driven workflow design

Think in stages:

- user requests action
- system stores job
- worker executes task
- result is saved
- user is notified

## 3. Retries and idempotency

If work can fail and retry, you must think carefully about duplicate effects.

Important mindset:

- retries are normal
- double-processing should not corrupt state

## 4. Durable execution

This matters especially for:

- AI calls
- external dependencies
- multi-step tasks
- human review steps

## 5. Email as product infrastructure

Email is often the easiest reliable completion signal for long-running or asynchronous workflows.

## Best Learning Sequence For This Week

1. background-job mental model
2. event flow
3. retries and idempotency
4. durable execution tools
5. completion notifications

## Recommended Daily Breakdown

### Day 1: Request vs job design

### Day 2: Build one background task

### Day 3: Add completion persistence

### Day 4: Add retry-safe logic

### Day 5: Add email notification

### Day 6: Inspect logs and traces

### Day 7: Document workflow states

## Build Plan

Take one slow AI workflow and redesign it as:

- queued or durable job
- saved progress/result
- email notification on completion

## Deliverables

- working background AI workflow
- completion email
- one workflow-state diagram or note

## Exit Criteria

- slow work no longer blocks user requests
- you can explain retries and idempotency at a practical level
- the user has a clear completion path

## Common Mistakes To Avoid

- keeping long tasks inline
- retrying without thinking about duplicate effects
- failing to persist intermediate or final job state

## Expert Notes That Matter Early

### Durable execution is a product quality feature

It makes long-running AI feel dependable instead of fragile.

### Async UX must still feel coherent

Users need to know what happened after they trigger a slow action.

## Final Standard For This Week

The correct outcome of Week 24 is not "I used a queue."

The correct outcome is:

"I can redesign slow AI work into a durable background workflow with clear state transitions and user notification."
