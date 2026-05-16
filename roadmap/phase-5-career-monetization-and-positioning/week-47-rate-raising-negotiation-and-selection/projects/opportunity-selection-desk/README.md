# Opportunity Selection Desk

This project is a lightweight workspace for evaluating project fit, pricing logic, and walk-away criteria.

## What It Demonstrates

- opportunity scoring
- pricing guidance from scope and risk
- boundary language support
- bad-fit detection

## Files

- `data/opportunities.json`: sample opportunity briefs
- `data/rate-card.json`: sample pricing multipliers
- `templates/boundary-language-template.md`: boundary phrasing structure
- `templates/negotiation-script-template.md`: negotiation structure
- `templates/scope-clarification-template.md`: scope clarification structure
- `src/opportunity-score.js`: fit scoring helper
- `src/pricing.js`: pricing helper
- `src/fit-flags.js`: bad-fit flag helper
- `tests/opportunity-selection-desk.test.mjs`: fit and pricing checks

## Suggested Study Order

1. inspect the sample opportunities
2. read the templates
3. inspect the source helpers
4. run the tests
5. replace the sample opportunities with real leads
