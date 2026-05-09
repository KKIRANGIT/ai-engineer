# Research Brief Orchestrator

Back to [Week 14 README](../../README.md)

## Purpose

This project solves one research-brief task in three orchestration styles:

- direct workflow
- graph-style orchestration
- lightweight agent loop

The project is intentionally local-first and deterministic so the orchestration logic stays visible.

## What This Project Demonstrates

- topic classification
- local retrieval
- drafting with evidence
- quality gates
- retry and review logic
- explicit state transitions
- comparison of orchestration styles

## Modes

### `direct`

Fixed step order:

1. classify topics
2. retrieve docs
3. draft brief
4. quality gate
5. finalize or flag for review

### `graph`

State-machine style execution:

- classification node
- retrieval node
- assessment node
- optional query refinement edge
- draft node
- review node
- final node

### `agent`

Lightweight ReAct-style loop:

- choose next search action
- search
- observe
- continue until enough evidence exists
- synthesize final brief

## Folder Structure

```text
research-brief-orchestrator/
|-- README.md
|-- data/
|   `-- documents.json
|-- src/
|   |-- __init__.py
|   |-- agent_loop.py
|   |-- data_access.py
|   |-- direct_workflow.py
|   |-- graph_runtime.py
|   |-- graph_workflow.py
|   |-- main.py
|   |-- models.py
|   |-- quality.py
|   |-- retrieval.py
|   |-- topic_router.py
|   `-- traces.py
`-- tests/
```

## How To Run

From this project folder:

```powershell
python -m src.main run --mode direct --query "Prepare a brief about refund policy for enterprise customers."
python -m src.main run --mode graph --query "Summarize travel reimbursement and security requirements."
python -m src.main run --mode agent --query "Create a brief about laptop requests and refund exceptions."
python -m src.main show-sample-queries
```

## What To Inspect

Study:

- chosen topics
- retrieved evidence
- state transitions
- retry or review flags
- final brief structure
- trace file

Each run writes a trace to `artifacts/latest_trace.json`.

## Engineering Lessons

This project is teaching several important habits:

- keep state explicit
- separate retrieval from orchestration
- make retry logic visible
- use human review when evidence is weak
- compare orchestration styles on the same task instead of comparing unrelated demos

## Suggested Extensions

After the base version is clear, good next upgrades are:

- replace local drafting with a live model
- swap the lightweight graph runtime for LangGraph
- add persistence between runs
- add approval checkpoints before final delivery
