# Study Session Tracker

Back to [Week 08](../../README.md)

## Purpose

This project is a small full-stack milestone application for Phase 1.

It helps a learner:

- create study subjects
- log study sessions
- view recent sessions
- review simple summary metrics
- remove incorrectly logged sessions

The project is intentionally small, but it proves the core Phase 1 skills in one place:

- Python backend structure
- HTTP routing and JSON APIs
- SQLite data modeling
- input validation
- browser-based JavaScript integration
- project documentation

## Project Structure

```text
study-session-tracker/
|-- README.md
|-- .env.example
|-- Dockerfile
|-- data/
|   `-- .gitkeep
|-- sql/
|   `-- schema.sql
|-- src/
|   |-- app.py
|   |-- config.py
|   |-- db.py
|   |-- repository.py
|   |-- response_utils.py
|   |-- server.py
|   |-- service.py
|   |-- static_handler.py
|   |-- validation.py
|   `-- static/
|       |-- app.js
|       |-- index.html
|       `-- styles.css
`-- tests/
    |-- test_repository.py
    `-- test_service.py
```

## Features

- create subjects with a category and weekly target
- log study sessions for a subject
- view recent sessions with subject names
- see total session count and total minutes
- see minutes grouped by subject
- delete a session

## Data Model

### `subjects`

Stores:

- subject name
- category
- weekly target in minutes
- creation timestamp

### `study_sessions`

Stores:

- subject relationship
- session date
- duration in minutes
- focus score from 1 to 5
- optional notes
- creation timestamp

## API Endpoints

### `GET /api/health`

Basic health response.

### `GET /api/subjects`

Returns all subjects.

### `POST /api/subjects`

Creates a subject.

Expected JSON body:

```json
{
  "name": "Python Foundations",
  "category": "backend",
  "target_minutes_per_week": 300
}
```

### `GET /api/sessions`

Returns recent sessions.

### `POST /api/sessions`

Creates a study session.

Expected JSON body:

```json
{
  "subject_id": 1,
  "session_date": "2026-05-09",
  "duration_minutes": 90,
  "focus_score": 4,
  "notes": "Practiced API integration and debugging."
}
```

### `GET /api/summary`

Returns total session count, total minutes, and minutes by subject.

### `DELETE /api/sessions/<id>`

Deletes one session.

## Local Setup

### 1. Create a virtual environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Start the server

```powershell
python src/server.py
```

Default URL:

`http://127.0.0.1:8000`

### 3. Open the app

Open the URL in your browser.

The database file is created automatically inside `data/`.

## Environment Variables

Supported environment variables:

- `HOST`
- `PORT`
- `APP_DB_PATH`

See [.env.example](/d:/Tutorials/InterviewPraparation/ai-engineer/roadmap/phase-1-foundation/week-08-foundation-milestone-project/projects/study-session-tracker/.env.example)

## Testing

From this project folder:

```powershell
python -m unittest discover -s tests
```

## Docker

Build:

```powershell
docker build -t study-session-tracker .
```

Run:

```powershell
docker run -p 8000:8000 study-session-tracker
```

## Architecture Notes

### `app.py`

Handles request routing and coordinates the backend flow.

### `validation.py`

Rejects invalid input before database work happens.

### `service.py`

Contains the application rules and summary assembly.

### `repository.py`

Contains SQL access and persistence behavior.

### `static/app.js`

Connects the browser UI to the backend with `fetch`.

## Tradeoffs

- SQLite is used for simple local setup and easy inspection.
- A small built-in Python server is used so the request/response flow remains visible.
- The frontend is intentionally simple because the milestone is about engineering synthesis, not UI complexity.
