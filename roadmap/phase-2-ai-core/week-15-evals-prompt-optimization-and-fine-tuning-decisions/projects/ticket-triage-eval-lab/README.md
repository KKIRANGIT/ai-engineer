# Ticket Triage Eval Lab

Back to [Week 15 README](../../README.md)

## Purpose

This project is a local evaluation harness for a support-ticket triage task.

It is designed to teach the mechanics of:

- running a baseline
- grading outputs
- comparing versions
- diagnosing failure patterns
- deciding what optimization lever to pull next

## What This Project Demonstrates

- a representative eval dataset
- multiple system versions
- programmatic graders
- case-level regression reporting
- simple aggregate metrics
- a decision memo on prompt vs retrieval vs fine-tuning

## System Versions

- `baseline`
- `prompt_v2`
- `retrieval_v1`

The versions are intentionally local and deterministic so the evaluation logic stays visible.

## Task

Each system version receives a support ticket and must produce:

- `category`
- `priority`
- `next_action`
- `customer_reply`

The eval harness grades:

- schema completeness
- category accuracy
- priority accuracy
- next-action alignment
- tone quality
- policy guidance quality

## Folder Structure

```text
ticket-triage-eval-lab/
|-- README.md
|-- data/
|   |-- eval_cases.json
|   `-- sample_finetune_examples.jsonl
|-- src/
|   |-- __init__.py
|   |-- analysis.py
|   |-- dataset.py
|   |-- decision_memo.py
|   |-- graders.py
|   |-- main.py
|   |-- models.py
|   |-- report.py
|   |-- retrieval_knowledge.py
|   `-- systems.py
`-- tests/
```

## How To Run

From this project folder:

```powershell
python -m src.main run --variant baseline
python -m src.main run --variant prompt_v2
python -m src.main run --variant retrieval_v1
python -m src.main compare
python -m src.main memo
```

## What To Inspect

Study:

- per-case scores
- which checks failed most often
- which version improved what
- where prompt improvements helped
- where retrieval improvements helped
- what the decision memo recommends next

Each run writes JSON output to `artifacts/`.

## Engineering Lessons

This project is intentionally teaching several habits:

- keep eval datasets explicit
- grade the same task across multiple versions
- inspect both average scores and failure details
- treat fine-tuning as a decision that follows diagnosis

## Suggested Extensions

After you understand the base version, good next upgrades are:

- add a live provider-backed system version
- add a human rubric column
- add confidence thresholds
- add a dashboard-style summary report
