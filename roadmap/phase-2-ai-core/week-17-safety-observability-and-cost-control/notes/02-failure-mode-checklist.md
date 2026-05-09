# Failure-Mode Checklist

Back to [Week 17 README](../README.md)

Use this checklist when hardening an AI workflow.

## Input Risks

- user prompt contains malicious instructions
- retrieved note contains override-like text
- request is too long or too expensive

## Workflow Risks

- tool parameters are malformed
- retrieval returns poor evidence
- timeout happens during a model or tool step
- fallback path is unclear

## Observability Risks

- trace is missing the failing step
- token or cost estimate is absent
- latency spikes are not visible

## Business Risks

- dangerous requests are answered too freely
- budget is exceeded without warning
- logs include more sensitive detail than needed
