# Support Ops Observability Lab

This project models the minimum visibility layer for a support operations product.

## What It Demonstrates

- event taxonomy design
- activation funnel summaries
- error grouping
- evidence-based product observations

## Files

- `src/event-taxonomy.js`: event catalog and validation helpers
- `src/analytics.js`: event recording and funnel summary helpers
- `src/error-monitor.js`: error grouping for triage
- `src/feedback-loop.js`: product observation helpers
- `tests/observability-lab.test.mjs`: event, funnel, and monitoring tests

## Suggested Study Order

1. inspect the event taxonomy
2. inspect the funnel summary helper
3. inspect the error grouping rules
4. run the tests
5. add one event and decide whether it belongs
