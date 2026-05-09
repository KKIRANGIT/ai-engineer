# Incident Assistant Multimodal Lab

Back to [Week 16 README](../../README.md)

## Purpose

This project is a local multimodal incident assistant for Week 16.

It is designed to teach the mechanics of:

- combining multiple context modalities
- comparing text-only and multimodal reasoning
- simulating a realtime session
- streaming partial response chunks
- tracing session events

## What This Project Demonstrates

- text report analysis
- transcript snippet handling
- image-observation fusion
- session event timelines
- partial response streaming
- text-only vs multimodal output comparison

## Project Modes

### `text`

Uses only the written incident report.

### `multimodal`

Uses the written report plus transcript excerpt and image observations.

### `session`

Simulates a realtime-style interaction:

- session start
- input accepted
- transcript step
- vision step
- response chunk streaming
- session complete

## Folder Structure

```text
incident-assistant-multimodal-lab/
|-- README.md
|-- data/
|   `-- incident_cases.json
|-- src/
|   |-- __init__.py
|   |-- analysis.py
|   |-- case_loader.py
|   |-- main.py
|   |-- models.py
|   |-- multimodal_fusion.py
|   |-- session.py
|   |-- streamer.py
|   `-- traces.py
`-- tests/
```

## How To Run

From this project folder:

```powershell
python -m src.main run --case CASE-01 --mode text
python -m src.main run --case CASE-01 --mode multimodal
python -m src.main run --case CASE-02 --mode session
python -m src.main list-cases
```

## What To Inspect

Study:

- how the text-only output differs from the multimodal output
- what extra signal comes from transcript and image observations
- the session event order
- the streamed chunks
- the saved trace

Each run writes a trace to `artifacts/latest_trace.json`.

## Engineering Lessons

This project is intentionally teaching several habits:

- represent modalities explicitly
- make session events visible
- separate context fusion from response generation
- treat streaming as UX behavior, not only output formatting

## Suggested Extensions

After you understand the base version, good next upgrades are:

- attach a live STT/TTS layer
- send image inputs to a real provider
- add interruption handling
- add tool calls during a session
