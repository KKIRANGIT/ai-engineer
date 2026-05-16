# Rollout and Config

## Feature Flags

Use feature flags for:

- new AI workflows
- premium-only features
- expensive analysis modes

## Cache Decisions

- dashboard summaries can be briefly cached
- ticket ownership and plan state should stay fresh
- job completion state should not be stale in a misleading way

## Secrets Boundaries

- browser code should never see provider secrets
- worker and server code can access job and AI credentials
- local development should use environment variables with clear ownership
