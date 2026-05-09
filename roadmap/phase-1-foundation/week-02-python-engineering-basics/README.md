# Week 02: Python Engineering Basics

Back to [Phase 1](../README.md)

## Goal

Move from "I can write Python" to "I can organize Python code like a small software project."

Week 01 was about language fluency. Week 02 is about engineering discipline.

By the end of this week, you should be able to:

- split a small project into modules with clear responsibilities
- validate inputs and raise useful errors
- read and write JSON confidently
- add basic type hints that improve readability
- understand when a simple class helps and when it is unnecessary
- write and run first-pass `pytest` tests
- explain why clean structure makes later API and AI work easier

This week is the bridge between beginner scripting and real application thinking.

## What This Week Is Actually Training

At surface level, Week 02 looks like "modules, exceptions, tests, and type hints."

The real training target is deeper:

- separating concerns instead of mixing everything together
- defining clearer function contracts
- making invalid states visible instead of silently tolerated
- learning to verify behavior with tests instead of guesswork
- making code easier for your future self to read and extend

This is why Week 02 matters so much. Later backend and AI engineering work is mostly built out of these exact habits:

- clearly defined data shape
- safe validation
- predictable behavior
- modular structure
- testable logic

## Scope Boundaries

Study deeply this week:

- modules and imports
- project structure
- exceptions and validation
- JSON and file boundaries
- type hints
- small classes and dataclasses
- configuration patterns
- `pytest`
- refactoring a CLI project into better shape

Do not go deep on these yet:

- advanced object-oriented design
- inheritance-heavy architecture
- metaprogramming
- async programming
- packaging for PyPI
- linting and type-checking toolchains beyond basic awareness
- dependency injection frameworks

Week 02 should make you structurally stronger, not overloaded.

## Week 02 Outcomes

You are successful this week if you can do most of the following with confidence:

- explain what each file in a small project is responsible for
- separate UI logic from business logic and storage logic
- raise `ValueError` or `IndexError` intentionally when something is wrong
- describe the expected shape of a JSON file before loading it
- add basic parameter and return type hints to helper functions
- write tests for both successful behavior and failure behavior
- refactor a Week 01 project into something easier to maintain

## How Week 02 Builds On Week 01

Week 01 taught:

- variables, data structures, control flow, functions, files, and basic CLI work

Week 02 assumes you already have:

- basic Python syntax comfort
- no fear of small scripts
- ability to read a traceback
- willingness to split logic into functions

Week 02 adds:

- module boundaries
- stronger validation
- better storage design
- first testing habit
- first serious refactor

That means Week 02 is not a reset. It is an upgrade.

## Core Engineering Concepts To Master

## 1. Modules and Project Structure

A module is simply a Python file that can be imported into another Python file.

This sounds small, but it is the foundation of every real Python codebase.

What you must understand:

- why one large script becomes hard to maintain
- how imports let files cooperate
- how to group related logic by responsibility
- how folder layout affects readability

A healthy beginner project usually separates:

- user interaction
- business rules
- storage or persistence
- data models
- tests

Rule:

If one file is doing input handling, computation, validation, persistence, and printing, it is already begging to be split.

## 2. Function Boundaries and Composition

Week 01 introduced functions. Week 02 makes them more intentional.

You should improve at:

- naming functions after a clear job
- keeping side effects near the outside of the program
- returning values instead of printing from deep inside logic
- composing small functions into bigger flows

Important mental model:

- boundary code talks to the outside world
- core logic transforms or validates data
- storage code reads from or writes to disk

That separation is one of the most important ideas in software engineering.

## 3. Exceptions and Validation

This is one of the biggest engineering upgrades of the week.

You need to understand:

- what an exception is
- why invalid input should be rejected early
- how to raise a useful error message
- where to catch the error
- why broad `except Exception:` often hides real problems

Good pattern:

- validate early
- raise specific errors
- catch errors near the user-facing boundary

Bad pattern:

- let corrupted data move through the system
- catch everything and print vague messages

## 4. JSON and Data Shape

JSON appears everywhere:

- local persistence
- config files
- API responses
- AI tool inputs and outputs

You must become comfortable with:

- `json.loads()` and `json.dumps()`
- `json.load()` and `json.dump()`
- the fact that JSON maps naturally to Python dicts and lists
- checking whether loaded data has the structure you expected

Expert beginner rule:

Whenever you load JSON, ask:

- what top-level type do I expect
- what keys should each record have
- what types should those keys hold

If you cannot describe the data shape clearly, your validation is incomplete.

## 5. Type Hints

Python does not require type hints to run, but type hints improve readability and reduce ambiguity.

You should learn:

- parameter type annotations
- return type annotations
- simple container hints like `list[str]`
- `dict[str, int]`
- `Path | None`

Why this matters:

- function contracts become clearer
- editor feedback gets better
- your code becomes easier to read later

Use type hints to clarify thinking, not to perform.

## 6. Small Classes and Dataclasses

You do not need heavy object-oriented design this week.

You do need to understand:

- what a class is
- what attributes are
- what methods are
- what `self` means
- when grouping data and behavior together is useful

For Week 02, the right level is:

- one simple class or dataclass
- clear examples of when it improves organization
- no inheritance gymnastics

The point is judgment, not complexity.

## 7. Testing With `pytest`

Testing begins here because it teaches behavior clarity.

You should learn:

- what a test function is
- how `assert` works
- how to test pure functions
- how to test expected errors
- how to use fixtures like `tmp_path` at a basic level

What to test first:

- validation failures
- helper functions
- business logic
- storage behavior with controlled sample data

Expert beginner rule:

Tests are not just for catching bugs later. They force you to define what "correct" means now.

## 8. Configuration and Environment Thinking

You do not need a full config system yet, but you should learn the pattern.

Understand:

- code should not hardcode every environment-specific setting
- environment variables are one clean way to pass settings
- `.env.example` is documentation for required settings

This matters now because it builds the right habit before API keys and deployment arrive later.

## 9. Refactoring

Refactoring means improving structure without changing the intended behavior.

Week 02 is the right time to practice it because:

- you already built something small in Week 01
- you can now improve it with better structure
- you will feel the benefit directly

Refactoring goals:

- clearer boundaries
- fewer tangled responsibilities
- easier testing
- more readable data flow

## Best Learning Sequence For This Week

Use this order:

1. modules and imports
2. project boundaries
3. exceptions and validation
4. JSON and storage design
5. type hints
6. simple classes or dataclasses
7. tests with `pytest`
8. config patterns
9. refactor the todo app

This order works because tests and config make much more sense once your project has shape.

## A No-Doubt Execution Plan For The Week

### Day 1: Module boundaries

Study:

- what a module is
- imports
- file responsibility
- project folder layout

Practice:

- split a single-file script into two or three files
- move pure logic out of user-interaction code

Checkpoint:

- can you explain what each file is responsible for

### Day 2: Validation and exceptions

Study:

- `ValueError`
- `IndexError`
- `FileNotFoundError`
- raising your own exceptions

Practice:

- reject empty task titles
- reject invalid menu options
- reject invalid list indexes

Checkpoint:

- can you describe where an error should be raised and where it should be caught

### Day 3: JSON and storage boundaries

Study:

- JSON serialization
- JSON parsing
- expected data shape
- file boundary separation

Practice:

- load tasks from JSON
- validate loaded data
- save normalized tasks back to a file

Checkpoint:

- can you explain the difference between raw file text and parsed Python data

### Day 4: Type hints and readability

Study:

- parameter annotations
- return annotations
- list and dict type hints
- `Path` annotations

Practice:

- annotate storage functions
- annotate task-related helpers

Checkpoint:

- can you read a function signature and understand what data it expects

### Day 5: Small class or dataclass thinking

Study:

- when a simple class helps
- dataclass basics
- converting between object form and dict form

Practice:

- represent one task as a small data model

Checkpoint:

- can you explain why a dataclass can make data shape more explicit

### Day 6: Testing with `pytest`

Study:

- test file naming
- test functions
- assertions
- testing expected failures

Practice:

- test task creation
- test invalid input
- test storage with temporary files

Checkpoint:

- can you explain what behavior each test is proving

### Day 7: Full refactor and review

Build:

- finish the refactored todo app
- run tests
- review structure
- compare Week 01 and Week 02 versions

Checkpoint:

- can you explain what became cleaner and why

## Week 02 Workspace Standard

This week should not remain only theoretical. It should produce a real practice workspace.

Recommended structure:

```text
week-02-python-engineering-basics/
|-- exercises/
|   |-- modules/
|   |-- validation/
|   |-- json/
|   |-- type_hints/
|   `-- classes/
|-- projects/
|   `-- refactored-todo-app/
|       |-- todo_app/
|       |-- tests/
|       |-- data/
|       |-- .env.example
|       `-- README.md
|-- notes/
`-- README.md
```

This gives you just enough structure to practice real engineering habits without overcomplicating the week.

## Main Build Goal

The central project for Week 02 is a refactored todo app that improves on the Week 01 version.

Required improvements:

- package-style structure
- clearer module responsibilities
- stronger validation
- safer JSON handling
- basic type hints
- a simple data model
- automated tests
- documented configuration pattern

Optional stretch ideas:

- task summary counts
- filtering by completion state
- search by keyword
- created timestamps

## Deliverables

By the end of the week, you should have:

- a set of focused engineering exercises
- a refactored todo application with multiple modules
- a `tests/` folder with useful `pytest` coverage
- a `.env.example` file
- a project README explaining structure and usage
- notes explaining what changed between Week 01 and Week 02

## Best Sources For Week 02

Use sources in this order.

### Tier 1: Official Python Sources

1. Python tutorial
   Link: https://docs.python.org/3/tutorial/

2. Python tutorial: modules
   Link: https://docs.python.org/3/tutorial/modules.html

3. Python tutorial: errors and exceptions
   Link: https://docs.python.org/3/tutorial/errors.html

4. Python tutorial: classes
   Link: https://docs.python.org/3/tutorial/classes.html

5. `json` library docs
   Link: https://docs.python.org/3/library/json.html

6. `pathlib` docs
   Link: https://docs.python.org/3/library/pathlib.html

7. `typing` docs
   Link: https://docs.python.org/3/library/typing.html

8. `dataclasses` docs
   Link: https://docs.python.org/3/library/dataclasses.html

9. `unittest` docs
   Link: https://docs.python.org/3/library/unittest.html

10. PEP 8
    Link: https://peps.python.org/pep-0008/

### Tier 2: Project and Environment Guidance

1. Python Packaging User Guide: install packages in a virtual environment
   Link: https://packaging.python.org/en/latest/tutorials/installing-packages/

Use it for:

- understanding why isolated environments matter
- normalizing good project setup habits

### Tier 3: Testing Source

1. Official `pytest` documentation
   Links:
   - https://docs.pytest.org/en/stable/
   - https://docs.pytest.org/en/stable/getting-started.html

Use it for:

- test file structure
- assertions
- expected exceptions
- fixtures like `tmp_path`

## Source Strategy That Avoids Confusion

For Week 02, do not mix random software-engineering tutorials.

Use this stack:

1. official Python docs for language and standard library truth
2. official `pytest` docs for testing workflow
3. your local exercises for reinforcement
4. the refactored todo project for real understanding

That is enough.

## Exact Study Path Through The Sources

If you want the least ambiguity, use this sequence:

1. read the Python modules tutorial
2. do the module-boundary exercise
3. read the exceptions tutorial
4. do the validation exercise
5. read `json`, `pathlib`, and `typing` docs selectively
6. do the JSON and type-hint exercises
7. read the classes tutorial and `dataclasses` docs selectively
8. build the refactored todo app model layer
9. read the `pytest` getting-started docs
10. write and run the project tests

## Exit Criteria

You are ready for Week 03 only if most of these are true:

- you can explain why modular structure helps
- you can separate UI, logic, data model, and storage clearly
- you can use exceptions intentionally
- you can validate loaded JSON rather than blindly trusting it
- you can add readable type hints
- you can write and understand a basic `pytest` suite
- you can explain how your Week 02 project is stronger than your Week 01 version

If these are not true, repeat the refactor and tests before moving on.

## Common Mistakes That Create Confusion Later

- adding classes everywhere just to look advanced
- mixing printing, validation, and storage inside one function
- catching exceptions too broadly
- trusting JSON structure without checking it
- writing tests only for happy paths
- using type hints mechanically without understanding the underlying data
- copying a project structure without understanding why it is organized that way

## Expert Notes

### Structure is a feature

A project that is easier to read and change is objectively better, even if the visible functionality is the same.

### Validation is part of correctness

Programs that only work for perfect input are incomplete.

### Tests are design pressure

If code is hard to test, that often means responsibilities are tangled.

### Refactoring is not cosmetic

Refactoring is how you turn "it works" into "it is maintainable."

## How Week 02 Connects To Week 03

Week 03 introduces HTTP, APIs, requests, and integration thinking.

That week becomes much easier if Week 02 is strong, because API code depends on:

- modular boundaries
- validation
- data-shape awareness
- JSON fluency
- testable helper functions

This is why Week 02 is not optional engineering polish. It is foundational.

## Final Standard For This Week

The correct outcome is not:

"I know OOP and testing."

The correct outcome is:

"I can organize a small Python project cleanly, validate inputs, persist structured data safely, express clearer function contracts, and verify core behavior with tests."
