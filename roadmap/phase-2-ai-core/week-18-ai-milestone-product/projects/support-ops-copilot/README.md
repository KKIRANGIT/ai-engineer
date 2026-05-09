# Support Ops Copilot

Back to [Week 18 README](../../README.md)

## Purpose

This project is the Week 18 capstone for Phase 2.

It is a local support operations copilot that combines the main Phase 2 capabilities into one coherent workflow.

## What This Project Demonstrates

- structured analysis output
- retrieval over support policies
- deterministic tool support
- safety screening
- trace logging
- cost estimation
- evaluation discipline

## User Problem

Support teams often need quick, consistent triage help:

- what category does this ticket belong to
- how urgent is it
- what policy applies
- should it be escalated
- what SLA should be used

This is a good AI-assisted workflow because it benefits from:

- text understanding
- policy grounding
- structured output
- deterministic business logic

## Architecture

The workflow is intentionally simple:

1. load ticket
2. run safety screen
3. retrieve relevant policy notes
4. produce structured analysis
5. compute SLA and escalation outputs
6. estimate request cost
7. record a trace

Important design choice:

This project uses a workflow, not an agent loop. That is deliberate because the task is structured and the step order is mostly known.

## Folder Structure

```text
support-ops-copilot/
|-- README.md
|-- data/
|   |-- eval_cases.json
|   |-- policies.json
|   `-- tickets.json
|-- src/
|   |-- __init__.py
|   |-- analyzer.py
|   |-- case_loader.py
|   |-- cost.py
|   |-- evals.py
|   |-- guardrails.py
|   |-- main.py
|   |-- models.py
|   |-- retrieval.py
|   |-- tools.py
|   `-- traces.py
`-- tests/
```

## How To Run

From this project folder:

```powershell
python -m src.main list-tickets
python -m src.main run --ticket T-1001
python -m src.main run --ticket T-1003
python -m src.main evaluate
```

## What To Inspect

Study:

- the structured analysis output
- retrieved policy support
- escalation and SLA decisions
- trace output
- cost estimate
- evaluation summary

Each ticket run writes a trace to `artifacts/latest_trace.json`.

## Why This Is A Strong Milestone

This project is strong because it shows:

- appropriate AI pattern selection
- grounded response generation
- deterministic integration where it matters
- visible internal quality story
- evaluation beyond demo vibes

## Suggested Extensions

After the base version is clear, good next upgrades are:

- replace the local deterministic analyzer with a live model call
- add a small frontend
- add real vector retrieval
- add human review mode for medium-confidence cases
