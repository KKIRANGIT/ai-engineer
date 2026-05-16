# Workflow State Map

Use these states as a minimum:

- queued
- running
- completed
- failed

Optional additions:

- needs_review
- retrying

For each state, define:

- who or what moves it forward
- what data should be persisted
- what the user can observe
