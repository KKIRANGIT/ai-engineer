# Support Ticket Triage Lab

Back to [Week 10](../../README.md)

## Purpose

This project is a Week 10 structured-output lab built around a practical classification task.

It is designed to teach:

- prompt template organization
- schema-driven output design
- OpenAI structured output request construction
- refusal and validation handling
- regression testing over prompt variants

The project uses support-ticket triage because it naturally requires:

- messy real-world input
- stable output fields
- clear categories
- ambiguity handling

## Project Structure

```text
support-ticket-triage-lab/
|-- README.md
|-- .env.example
|-- data/
|   |-- regression_cases.json
|   `-- sample_tickets.json
|-- prompt_library/
|   |-- classify_ticket_v1.md
|   |-- classify_ticket_v2_few_shot.md
|   `-- classify_ticket_v3_xml.md
|-- schemas/
|   `-- ticket_triage_schema.json
|-- src/
|   |-- __init__.py
|   |-- config.py
|   |-- main.py
|   |-- mock_engine.py
|   |-- models.py
|   |-- openai_structured_client.py
|   |-- prompt_library.py
|   |-- regression.py
|   `-- validators.py
`-- tests/
    |-- test_openai_structured_client.py
    |-- test_prompt_library.py
    |-- test_regression.py
    `-- test_validators.py
```

## Task

Given a support ticket, return structured output with:

- category
- priority
- short summary
- whether human follow-up is needed
- confidence note

## Prompt Variants

### `classify_ticket_v1.md`

Clear baseline prompt.

### `classify_ticket_v2_few_shot.md`

Adds representative examples.

### `classify_ticket_v3_xml.md`

Uses XML-like sections to organize instructions, labels, examples, and input.

## Schema

The schema lives in [schemas/ticket_triage_schema.json](schemas/ticket_triage_schema.json).

It defines:

- required fields
- supported enums
- object shape boundaries

## Modes

### Mock mode

Deterministic local output for learning and testing.

### Live OpenAI structured-output mode

Builds a Responses API request using `text.format` with `type: "json_schema"`.

This requires:

- a real `OPENAI_API_KEY`
- network access

## Example Commands

From this project folder:

### Show one prompt variant

```powershell
python -m src.main show-prompt --template classify_ticket_v1 --ticket-id ticket_001
```

### Run one case in mock mode

```powershell
python -m src.main run-case --mode mock --template classify_ticket_v2_few_shot --ticket-id ticket_001
```

### Run the regression set in mock mode

```powershell
python -m src.main regress --mode mock --template classify_ticket_v3_xml
```

### Show the live OpenAI request payload shape

```powershell
python -m src.main show-request --template classify_ticket_v1 --ticket-id ticket_001
```

## Environment Variables

- `OPENAI_API_KEY`
- `OPENAI_MODEL`

See [.env.example](.env.example)

## Testing

From this project folder:

```powershell
python -m unittest discover -s tests
```

## Important Learning Rule

Do not treat this project as:

"one more classifier."

Use it to answer these questions:

- Is the task clearly specified?
- Is the output contract explicit?
- Are failures visible?
- Can prompt variants be compared on the same cases?
- Can the application trust the output shape?
