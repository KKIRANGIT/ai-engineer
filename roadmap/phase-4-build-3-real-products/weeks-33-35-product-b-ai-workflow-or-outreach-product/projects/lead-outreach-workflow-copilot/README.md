# Lead Outreach Workflow Copilot

This project is a workflow product for lead research and outreach drafting.

## What It Demonstrates

- manual workflow decomposition
- deterministic lead-enrichment tools
- structured lead briefs
- approval gates before outreach is ready to send
- audit logs and ROI comparison helpers

## Files

- `data/tasks/lead-tasks.json`: representative workflow tasks
- `docs/product-brief.md`: product framing and user workflow
- `docs/before-vs-after.md`: baseline and assisted workflow comparison
- `docs/feedback-template.md`: tester feedback capture format
- `src/load-tasks.js`: sample task loading
- `src/tools.js`: deterministic enrichment helpers
- `src/structured-output.js`: lead-brief output assembly and validation
- `src/workflow-engine.js`: workflow-state orchestration
- `src/audit-log.js`: execution trace helpers
- `src/roi.js`: simple ROI comparison helpers
- `tests/workflow.test.mjs`: workflow, validation, and ROI tests

## Suggested Study Order

1. read the product brief
2. inspect the sample tasks
3. read the tool and structured-output modules
4. read the workflow engine
5. run the tests
6. adapt one sample task to a different workflow niche
