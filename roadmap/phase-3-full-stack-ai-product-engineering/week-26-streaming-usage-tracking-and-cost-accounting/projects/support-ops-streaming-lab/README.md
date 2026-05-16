# Support Ops Streaming Lab

This project models a streamed AI workflow with per-user usage accounting.

## What It Demonstrates

- async streamed output
- per-user usage summaries
- plan-aware quota checks
- rough cost estimation

## Files

- `src/stream-session.js`: async chunk generator for streamed responses
- `src/usage-ledger.js`: per-user usage recording and summaries
- `src/quotas.js`: plan limit enforcement helpers
- `src/cost-model.js`: rough request-cost estimation
- `tests/streaming-lab.test.mjs`: streaming, usage, and quota tests

## Suggested Study Order

1. inspect the stream helper
2. inspect the usage ledger
3. inspect the quota logic
4. run the tests
5. add a new plan and see what the limit model requires
