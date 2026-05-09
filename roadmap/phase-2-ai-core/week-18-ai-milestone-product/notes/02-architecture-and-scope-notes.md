# Architecture and Scope Notes

Back to [Week 18 README](../README.md)

## Why This Architecture

The support-ops copilot uses:

- structured output
- retrieval
- deterministic tools
- guardrails
- traces
- evals

It does not use:

- an agent loop
- multiple providers
- browser actions
- background orchestration

That is deliberate. The use case benefits from grounded lookup and deterministic operations, but not from open-ended autonomy.

## Why This Is A Good Milestone Product

It proves:

- pattern selection judgment
- workflow design
- retrieval plus structure integration
- operational awareness
- evaluation discipline

That makes it much stronger than a generic chatbot demo.
