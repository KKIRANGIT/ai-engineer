# Architecture Explainer

Back to [Week 08](../README.md)

## Project Goal

The included milestone project is a study-session tracker.

It lets a user:

- create study subjects
- log study sessions
- review recent sessions
- see simple summary information
- remove a session if it was logged incorrectly

## Why This Is A Good Milestone

This project is strong for Phase 1 because it combines:

- relational data
- backend API design
- frontend forms and fetch requests
- validation
- basic reporting

It is large enough to feel like a product, but small enough to understand without hiding behind a heavy framework.

## Layer Responsibilities

### `server.py`

Starts the local server.

### `app.py`

Acts as the request entrypoint and route dispatcher.

### `validation.py`

Protects the service layer from invalid input.

### `service.py`

Holds the application rules and summary logic.

### `repository.py`

Handles direct SQLite access.

### `static/`

Contains the browser UI and fetch-based integration.

## Important Design Choice

The backend is intentionally lightweight and dependency-free.

That is not because larger frameworks are bad. It is because this stage benefits more from seeing the request/response and database flow directly than from adopting abstractions too early.
