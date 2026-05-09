# Event Ingestion Pipeline

This project is the main Week 06 hands-on artifact.

It is a small end-to-end pipeline that:

- reads event rows from CSV
- reads enrichment metadata from JSON
- loads both sources concurrently using `asyncio`
- normalizes and enriches records
- writes cleaned output files
- can run locally or inside Docker

## What This Project Teaches

- async orchestration for I/O-style work
- clear pipeline stage separation
- CSV parsing and output writing
- local JSON enrichment
- reproducible execution with Docker

## Project Structure

```text
event-ingestion-pipeline/
|-- app/
|   |-- __init__.py
|   |-- config.py
|   |-- data_loader.py
|   |-- main.py
|   |-- models.py
|   |-- pipeline.py
|   `-- reports.py
|-- data/
|   |-- event_scores.json
|   `-- raw_events.csv
|-- output/
|-- tests/
|   `-- test_pipeline.py
|-- .env.example
|-- .dockerignore
|-- Dockerfile
`-- README.md
```

## How To Run Locally

```powershell
python -m app.main
```

## How To Run Tests

```powershell
python -m unittest discover -s tests
```

## Docker Build And Run

Build:

```powershell
docker build -t event-ingestion-pipeline .
```

Run:

```powershell
docker run --rm event-ingestion-pipeline
```

## Output Files

After running the pipeline, the project writes:

- `output/cleaned_events.csv`
- `output/summary_report.json`

## Environment Variable Pattern

This project supports optional path overrides:

- `RAW_EVENTS_FILE`
- `EVENT_SCORES_FILE`
- `PIPELINE_OUTPUT_DIR`

See [.env.example](./.env.example) for the example values.
