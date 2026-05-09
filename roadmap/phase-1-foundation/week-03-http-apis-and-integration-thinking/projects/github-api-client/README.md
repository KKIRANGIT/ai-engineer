# GitHub API Client

This project is the main Week 03 build artifact.

It is a small reusable client for selected GitHub REST API operations, built with Python's standard library so the project stays dependency-light and transparent.

## What This Project Teaches

- URL and query parameter construction
- explicit timeout handling
- header handling
- token-based configuration
- response parsing
- reusable wrapper design
- basic tests for parsing and helper logic

## Project Structure

```text
github-api-client/
|-- github_api/
|   |-- __init__.py
|   |-- client.py
|   |-- config.py
|   |-- http_utils.py
|   |-- models.py
|   `-- cli.py
|-- tests/
|   |-- test_http_utils.py
|   `-- test_models.py
|-- examples/
|   `-- fetch_profile.py
|-- data/
|   |-- sample_repo_response.json
|   `-- sample_user_response.json
|-- .env.example
`-- README.md
```

## Features

- fetch one GitHub user profile
- list repositories for a given GitHub user
- inspect GitHub rate-limit information
- parse pagination links
- run a simple CLI demo

## How To Run

From this folder:

```powershell
python -m github_api.cli
```

## Example Script

```powershell
python examples/fetch_profile.py
```

## How To Run Tests

This project uses the Python standard library `unittest` module.

From this folder:

```powershell
python -m unittest discover -s tests
```

## Environment Variable Pattern

This project supports one optional environment variable:

- `GITHUB_TOKEN`

If you set it, the client will send an authorization header. That can increase your rate-limit allowance for GitHub API usage.

See [.env.example](./.env.example) for the example format.

## Important Note

This client calls the live GitHub REST API. It requires a network connection to fetch real data.

The unit tests do not require network access because they focus on local parsing and helper logic.
