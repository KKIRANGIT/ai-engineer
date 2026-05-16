# Week 24: Email, Background Jobs, and Durable Execution

Back to [Phase 3](../README.md)

## Goal

Handle long-running AI work correctly so the product stays responsive while slower workflows complete safely in the background.

This week is about operational flow design, not only queue terminology.

## Why This Week Matters

AI tasks often take longer than a standard request-response cycle should tolerate.

If you keep everything inline, you get:

- timeouts
- poor UX
- fragile retries
- failed work with no recovery path

This week introduces the operational backbone for serious AI product workflows.

## What This Week Is Actually Training

Week 24 is training five deeper skills:

1. deciding what belongs in the request path versus the background path
2. modeling long-running work as state transitions
3. handling retries and idempotency intentionally
4. persisting results and workflow status clearly
5. notifying users when slow work completes

The real outcome is not "I used a queue." The real outcome is "I can redesign slow AI work into a dependable product workflow."

## Scope Boundary For This Week

This week focuses on:

- queued and durable workflow mental models
- job-state transitions
- retries and duplicate-protection
- completion persistence
- email as a completion signal

This week does not require:

- distributed task orchestration at large scale
- advanced workflow engines with every feature enabled
- enterprise notification systems

The correct goal is to learn how long-running AI work becomes dependable instead of blocking the user request path.

## Week 24 Outcomes

By the end of this week, you should be able to:

- distinguish synchronous request handling from background execution
- understand retries and idempotency conceptually
- design a job-based AI workflow
- notify the user when work completes
- explain why durable execution matters for AI workloads

## Best Source Strategy For This Week

Use sources in this order:

1. the local Week 24 workspace
2. official durable-execution and email delivery documentation
3. your own workflow-state notes

Do not treat this week as queue vocabulary only. The real lesson is product behavior under slow and failure-prone work.

## Recommended Official References

Use these external references as the primary companion stack:

- Inngest docs: <https://www.inngest.com/docs>
- Resend docs: <https://resend.com/docs>
- Next.js route handlers guide: <https://nextjs.org/docs/app/getting-started/route-handlers>

These are enough to connect the local workspace to realistic tooling without overloading the week.

## Recommended Project Direction For This Workspace

This workspace uses one realistic but manageable product scenario:

- a support operations job runner

Why this direction was chosen:

- it naturally includes slow AI analysis work
- it makes retry and duplicate-processing risks concrete
- it gives email completion a product-facing purpose
- it fits directly after Weeks 21 to 23 without changing the product domain

## Project Capabilities This Week Includes

The Week 24 project includes:

- a small job-state machine
- request submission and job processing helpers
- idempotency protection for duplicate attempts
- completion email generation
- tests for retry-safe behavior and workflow transitions

The project stays local and inspectable on purpose so the workflow logic remains clearer than the infrastructure layer.

## Recommended Build Sequence

1. map the request path and background path
2. define job states
3. write submission logic
4. write processing logic with duplicate protection
5. persist completion information
6. notify the user with a completion message
7. test retries and repeated events

## Recommended Daily Breakdown

### Day 1: Request vs job design

### Day 2: Workflow state design

### Day 3: Retry and idempotency

### Day 4: Completion persistence

### Day 5: Email notification

### Day 6: Logs and state review

### Day 7: Document the workflow

## Hands-On Workspace Structure

```text
week-24-email-background-jobs-and-durable-execution/
|-- README.md
|-- exercises/
|   |-- README.md
|   |-- request-vs-job/
|   |-- retries-and-idempotency/
|   `-- workflow-communication/
|-- notes/
|   |-- 01-week-plan.md
|   |-- 02-workflow-state-map.md
|   `-- 03-idempotency-review.md
`-- projects/
    `-- support-ops-job-runner/
```

## Exercises

The exercises isolate the design questions that get hidden when people jump straight to a queue library.

You will practice:

- deciding what should leave the request path
- identifying duplicate-effect risks
- designing completion communication clearly

Start here:

- [Exercises README](exercises/README.md)

## Main Project

Project:

- [support-ops-job-runner](projects/support-ops-job-runner/README.md)

This project is a small workflow lab for long-running support analysis jobs. It teaches:

- queued job thinking
- workflow-state transitions
- retry-safe processing
- completion email generation

It is intentionally compact so the state machine stays easy to inspect.

## Deliverables

By the end of this week, you should have:

- one complete durable-execution workspace
- one tested background-job project
- one workflow-state note
- one idempotency review checklist

## Exit Criteria

You are ready to move to Week 25 only if:

- slow work no longer blocks the request path conceptually
- you can explain retries and idempotency at a practical level
- the workflow has explicit states
- the user has a clear completion path
- you can identify one duplicate-effect risk and how you prevent it

## Common Mistakes To Avoid

- keeping long tasks inline
- retrying without thinking about duplicate effects
- failing to persist intermediate or final job state
- sending completion email before the durable result exists

## Expert Notes That Matter Early

### Durable execution is a product quality feature

It makes long-running AI feel dependable instead of fragile.

### Async UX must still feel coherent

Users need to know what happened after they trigger a slow action.

### Retries are normal

The mistake is not that a retry happened. The mistake is designing the workflow as if retries never will.

## Final Standard For This Week

The correct outcome of Week 24 is not:

"I used a queue."

The correct outcome is:

"I can redesign slow AI work into a durable background workflow with clear state transitions and user notification."
