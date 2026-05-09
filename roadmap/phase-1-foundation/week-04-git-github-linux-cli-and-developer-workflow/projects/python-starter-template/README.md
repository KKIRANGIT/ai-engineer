# Python Starter Template

This project is the main Week 04 reusable starter repository.

## What This Project Teaches

- a clean small-project layout
- a useful `README.md`
- config hygiene with `.env.example`
- ignore rules with `.gitignore`
- a small local test command
- a matching GitHub Actions workflow

## Project Structure

```text
python-starter-template/
|-- .github/workflows/python-checks.yml
|-- app/
|   |-- __init__.py
|   |-- greeter.py
|   `-- main.py
|-- tests/
|   `-- test_greeter.py
|-- scripts/
|   `-- run_checks.py
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

## How To Run Local Checks

```powershell
python scripts/run_checks.py
```

## Why This Template Matters

Later weeks will keep introducing new tools and systems. A reusable starter project helps you begin cleanly instead of re-solving repository structure every time.
