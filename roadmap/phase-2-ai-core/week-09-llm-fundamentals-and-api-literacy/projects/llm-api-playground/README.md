# LLM API Playground

Back to [Week 09](../../README.md)

## Purpose

This project is a Week 09 learning playground for direct-provider API literacy.

It is designed to teach:

- how OpenAI Responses requests are shaped
- how Anthropic Messages requests are shaped
- how to normalize different provider responses into one internal structure
- how to log traces and usage details
- how to think about cost before more advanced AI system layers are introduced

The project supports:

- `mock` mode for offline learning and testing
- live OpenAI mode
- live Anthropic mode

Mock mode is important because the goal of Week 09 is not "spend money to prove an API key works." The goal is to understand request/response and wrapper design deeply enough that live usage becomes deliberate.

## Project Structure

```text
llm-api-playground/
|-- README.md
|-- .env.example
|-- data/
|   `-- .gitkeep
|-- logs/
|   `-- .gitkeep
|-- src/
|   |-- __init__.py
|   |-- clients.py
|   |-- config.py
|   |-- cost_utils.py
|   |-- http_utils.py
|   |-- logger.py
|   |-- main.py
|   |-- models.py
|   |-- prompts.py
|   `-- sample_data.py
`-- tests/
    |-- test_clients.py
    |-- test_cost_utils.py
    `-- test_logger.py
```

## Supported Modes

### Mock mode

Deterministic offline responses for learning, testing, and code inspection.

### OpenAI mode

Uses the OpenAI Responses endpoint with a simple text-input flow.

### Anthropic mode

Uses the Anthropic Messages endpoint with a simple user-message flow.

## Example Commands

From this project folder:

### Run in mock mode

```powershell
python -m src.main ask --provider mock --prompt "Explain embeddings in plain English."
```

### Run in OpenAI mode

```powershell
python -m src.main ask --provider openai --model gpt-5 --prompt "Explain embeddings in plain English."
```

### Run in Anthropic mode

```powershell
python -m src.main ask --provider anthropic --model claude-sonnet-4-20250514 --prompt "Explain embeddings in plain English."
```

### Compare providers in mock mode

```powershell
python -m src.main compare --prompt "Summarize RAG in two sentences."
```

## Environment Variables

Supported values:

- `OPENAI_API_KEY`
- `ANTHROPIC_API_KEY`
- `ANTHROPIC_VERSION`
- `LLM_PLAYGROUND_LOG_PATH`
- `LLM_PLAYGROUND_TIMEOUT_SECONDS`

See [.env.example](.env.example)

## Logging

Each run appends a JSON line to the configured trace log path. Logged fields include:

- provider
- model
- latency
- text output
- usage
- estimated cost
- errors when present

## Architecture Notes

### `models.py`

Defines the internal request and normalized response structures used by the application.

### `clients.py`

Contains provider-specific request builders and response parsers.

### `http_utils.py`

Handles low-level HTTP POST behavior and response decoding.

### `logger.py`

Writes trace entries to a JSONL log file.

### `cost_utils.py`

Calculates rough cost estimates from usage metrics using simple per-million-token rates.

### `main.py`

Provides the CLI entrypoint and ties the pieces together.

## Testing

From this project folder:

```powershell
python -m unittest discover -s tests
```

## Important Learning Rule

Do not treat this project as a generic chatbot.

Use it to answer these questions:

- What did the request actually send?
- What did the provider actually return?
- How does my application extract the useful output?
- What changed between providers?
- What do the usage metrics imply about cost?
