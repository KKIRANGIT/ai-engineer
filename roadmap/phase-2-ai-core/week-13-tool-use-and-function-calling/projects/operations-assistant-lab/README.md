# Operations Assistant Lab

Back to [Week 13 README](../../README.md)

## Purpose

This project is a local, inspectable tool-enabled assistant for Week 13.

It is designed to teach the real mechanics of tool use without hiding them behind a framework or a live provider dependency.

## What This Project Demonstrates

- a small tool registry
- strong tool descriptions and schemas
- a planner that proposes tool calls
- validation before execution
- deterministic tool implementations
- trace logging
- provider payload builders for OpenAI and Anthropic

## Tools In This Project

- `lookup_ticket`
- `search_policy_docs`
- `calculate_refund`
- `get_weather_snapshot`

## Why This Project Is Local-First

The goal of Week 13 is understanding. Local data and deterministic tools make the control flow visible:

- which tool was requested
- what arguments were used
- which validation rules ran
- what output came back
- how the final answer was composed

Once you understand that loop, live provider integrations become easier to reason about.

## Folder Structure

```text
operations-assistant-lab/
|-- README.md
|-- .env.example
|-- data/
|   |-- knowledge_base.json
|   |-- tickets.json
|   `-- weather.json
|-- src/
|   |-- __init__.py
|   |-- assistant.py
|   |-- data_access.py
|   |-- main.py
|   |-- models.py
|   |-- planner.py
|   |-- providers.py
|   |-- tool_schemas.py
|   |-- tools.py
|   |-- traces.py
|   `-- validators.py
`-- tests/
```

## How To Run

From this project folder:

```powershell
python -m src.main run --query "Look up ticket T-1002 and explain the refund policy."
python -m src.main run --query "What is 35 percent of 1200?"
python -m src.main run --query "Check the weather in Bengaluru and then look up ticket T-1004."
python -m src.main show-openai-tools
python -m src.main show-anthropic-tools
```

## What To Inspect

When you run the assistant, study:

- planned tool calls
- validated arguments
- tool results
- final answer
- generated trace file

The trace file is written to `artifacts/latest_trace.json`.

## Sample Questions

- `Look up ticket T-1001 and summarize the issue.`
- `Search the refund policy and tell me the main rule.`
- `What is 50 percent of 1400?`
- `What is the weather in Bengaluru?`
- `Look up ticket T-1002, search the refund policy, and calculate 50 percent of 1200.`

## Engineering Lessons

This project is intentionally teaching several expert habits:

- tools are defined separately from their execution code
- provider payload building is separate from internal schemas
- validation happens before execution
- deterministic work stays deterministic
- traces are treated as part of the product

## Suggested Extensions

After you understand the base version, good next upgrades are:

- add a live LLM provider wrapper that consumes the same tool registry
- add a tool-choice policy switch for explicit versus model-chosen routing
- add a permission gate for high-risk actions
- add multi-step clarification behavior for missing arguments
