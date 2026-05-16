# Launch Readiness Console

This project is a lightweight workspace for evaluating launch readiness and early launch signal.

## What It Demonstrates

- launch readiness scoring
- distribution channel prioritization
- activation metric review
- launch retrospective framing

## Files

- `data/launch-plan.json`: sample launch setup
- `data/launch-feedback.json`: sample early feedback
- `templates/launch-checklist.md`: readiness checklist
- `templates/channel-plan-template.md`: channel plan structure
- `templates/launch-retro-template.md`: retro structure
- `src/readiness.js`: readiness scoring helper
- `src/channel-prioritizer.js`: channel selection helper
- `src/activation-metrics.js`: launch signal helper
- `tests/launch-console.test.mjs`: readiness and signal checks

## Suggested Study Order

1. inspect the sample launch plan
2. read the templates
3. inspect the readiness and signal helpers
4. run the tests
5. replace the sample inputs with one real product launch plan
