# Support Ops Job Runner

This project models a slow support analysis workflow that should not block the request path.

## What It Demonstrates

- job submission and state transitions
- retry-safe processing
- idempotency protection
- completion email generation

## Files

- `src/job-store.js`: in-memory job lifecycle helpers
- `src/idempotency.js`: duplicate-attempt protection
- `src/workflow.js`: request submission and job processing logic
- `src/notifications.js`: completion email formatting
- `tests/job-runner.test.mjs`: workflow and retry tests

## Suggested Study Order

1. inspect the job state shape
2. inspect the idempotency helpers
3. read the workflow functions
4. run the tests
5. add a new failure case and see where the model becomes weak
