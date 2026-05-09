# Project Tracker DB

This project is the main Week 05 hands-on artifact.

It is a small relational CRUD demo built with Python's standard-library `sqlite3` module.

## Why SQLite Here

This repository uses SQLite for the runnable code so you can focus on relational thinking without pausing for local database-server setup.

The important ideas still transfer directly to PostgreSQL:

- tables
- joins
- keys
- constraints
- CRUD
- transaction boundaries

## What This Project Teaches

- schema design
- seed data
- CRUD repository functions
- many-to-many relationships through a join table
- report-style query functions
- transaction-aware writes

## Project Structure

```text
project-tracker-db/
|-- app/
|   |-- __init__.py
|   |-- db.py
|   |-- main.py
|   |-- models.py
|   |-- reports.py
|   `-- repository.py
|-- sql/
|   |-- schema.sql
|   `-- seed.sql
|-- tests/
|   `-- test_repository.py
|-- data/
|-- .env.example
|-- .gitignore
`-- README.md
```

## How To Run

```powershell
python -m app.main
```

## How To Run Tests

```powershell
python -m unittest discover -s tests
```

## Environment Variable Pattern

This project supports one optional environment variable:

- `PROJECT_TRACKER_DB_PATH`

If you do not set it, the project uses a default SQLite database file under `data/project_tracker.db`.

## PostgreSQL Mapping

If you later move this project to PostgreSQL, the main conceptual changes are infrastructure-related, not data-model-related:

- server-based database instead of file-based database
- connection string instead of local file path
- driver change from `sqlite3` to a PostgreSQL driver

The schema and query thinking remain the important part.
