# Guarded Support Assistant Lab

Back to [Week 17 README](../../README.md)

## Purpose

This project is a local guarded support assistant for Week 17.

It is designed to teach the mechanics of:

- trust-boundary classification
- simple prompt-injection screening
- trace logging
- retry and fallback behavior
- request cost estimation
- budget guardrails

## What This Project Demonstrates

- safe vs suspicious request handling
- explicit trust-boundary notes
- request-level trace events
- timeout and retry simulation
- cost estimation and budget checks

## Project Behavior

The project accepts a local support request and:

1. classifies trust boundaries
2. screens for suspicious content
3. estimates tokens and cost
4. blocks or warns if a budget rule is exceeded
5. simulates a guarded response path
6. records a trace

## Folder Structure

```text
guarded-support-assistant-lab/
|-- README.md
|-- data/
|   `-- request_cases.json
|-- src/
|   |-- __init__.py
|   |-- budget.py
|   |-- case_loader.py
|   |-- guardrails.py
|   |-- main.py
|   |-- models.py
|   |-- processor.py
|   |-- retry_logic.py
|   |-- traces.py
|   `-- trust.py
`-- tests/
```

## How To Run

From this project folder:

```powershell
python -m src.main run --case CASE-01
python -m src.main run --case CASE-02
python -m src.main run --case CASE-03
python -m src.main list-cases
```

## What To Inspect

Study:

- trust-boundary classification
- whether the request was flagged or blocked
- estimated token and cost totals
- retry or fallback events
- the saved trace

Each run writes a trace to `artifacts/latest_trace.json`.

## Engineering Lessons

This project is intentionally teaching several habits:

- model inputs are not all equally trustworthy
- guardrails should be explicit, not implied
- logs should explain what happened
- cost needs to be visible at request time

## Suggested Extensions

After you understand the base version, good next upgrades are:

- add role-based approval paths
- add output filtering
- add live token usage from provider responses
- connect to an external trace store
