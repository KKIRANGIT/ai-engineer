# Week 01: Python Core and Problem Solving

Back to [Phase 1](../README.md)

## Goal

Become fluent enough in Python that the language itself stops being the bottleneck. By the end of this week, you should be able to read simple Python comfortably, write small programs without constant syntax lookup, and break basic problems into functions and clear steps.

This week is not about "covering Python." It is about building the minimum level of fluency required for the rest of the roadmap. If this week is weak, every later phase becomes slower and more frustrating.

## Why This Week Matters

Most learners try to learn Python by collecting syntax. That is the wrong target.

The real target is:

- understanding Python's basic mental model
- getting comfortable with core data types
- learning how to think in steps, conditions, and transformations
- writing code that is small, readable, and testable

You do not need advanced Python this week. You need strong control over the basics.

If you do this week properly, later topics become much easier:

- APIs are easier because JSON maps naturally to dicts and lists
- SQL becomes easier because data transformation thinking improves
- AI workflows become easier because prompt inputs and tool outputs are just structured data
- backend work becomes easier because you already know how to decompose logic into functions

## Week 01 Outcomes

By the end of this week, you should be able to:

- explain the difference between a list, tuple, set, and dict
- use conditionals and loops comfortably
- write and call functions with parameters and return values
- read from and write to simple files
- solve small logic problems without writing one giant script
- debug basic syntax, type, and index errors
- structure a CLI program into small functions

## What To Learn

## 1. Python Mental Model

Before learning syntax mechanically, internalize these ideas:

- Python is dynamically typed, but types still matter.
- Variables are names bound to objects, not boxes with fixed types.
- Many beginner bugs come from misunderstanding mutability, indexing, and truthiness.
- Readability is a core design value in Python, not a nice extra.

Important beginner mindset:

- do not write "clever" code
- write obvious code
- name things clearly
- prefer correctness and clarity over compactness

## 2. Core Data Types

You need working fluency with:

- `int`
- `float`
- `str`
- `bool`
- `list`
- `tuple`
- `set`
- `dict`
- `None`

You should understand:

- what each type is for
- how to create it
- how to read values from it
- how to modify it if mutable
- common methods and operations

Key distinctions:

- `list`: ordered, mutable sequence
- `tuple`: ordered, immutable sequence
- `set`: unordered collection of unique items
- `dict`: key-value mapping

Expert note:

Do not only memorize definitions. Learn the typical use case:

- use `list` for ordered collections you will grow or update
- use `tuple` for fixed grouped values
- use `set` for fast membership checks and uniqueness
- use `dict` for named or keyed data

## 3. Expressions, Operators, and Truthiness

Be comfortable with:

- arithmetic operators
- comparison operators
- logical operators: `and`, `or`, `not`
- membership: `in`, `not in`
- identity: `is`, `is not`

Critical note:

- use `==` to compare values
- use `is` mainly for identity checks like `x is None`

Truthiness is important. In Python, these commonly behave as false:

- `0`
- `0.0`
- `""`
- `[]`
- `{}`
- `set()`
- `None`
- `False`

If you do not understand truthiness, your conditions will become fragile.

## 4. Control Flow

You need solid comfort with:

- `if`
- `elif`
- `else`
- `for`
- `while`
- `break`
- `continue`

You should be able to answer:

- when should I use a `for` loop versus `while`
- when is a condition too complicated and should be moved into a helper function
- how do I avoid deeply nested code

Expert rule:

If your control flow starts becoming hard to read, split logic into smaller functions rather than stacking more branches.

## 5. Functions

This is one of the most important parts of the week.

You must understand:

- function definition
- parameters
- arguments
- return values
- local scope
- basic docstring usage

Bad beginner habit:

- writing huge scripts with no functions

Good engineering habit:

- give each function one clear job
- use return values instead of printing everything
- keep function names descriptive

A strong beginner function is:

- short
- readable
- predictable
- easy to reuse

## 6. Strings and Basic Text Processing

You should be able to:

- concatenate strings
- split strings
- strip whitespace
- change case
- search for substrings
- use f-strings

Why this matters:

- CLI programs rely on text handling
- APIs rely on text and JSON handling
- AI work often begins with text normalization, formatting, or extraction

Expert rule:

Prefer f-strings for readable formatting.

## 7. Collections and Iteration Patterns

Get comfortable with:

- iterating through lists
- iterating through dicts
- using `enumerate()`
- using `zip()`
- basic list comprehensions

Important note:

List comprehensions are useful, but do not force them everywhere. If the expression becomes hard to read, use a normal loop.

## 8. File I/O

You need to know:

- how to open a file safely
- reading text
- writing text
- appending text
- why context managers matter

Use:

- `with open(...) as f:`

Modern path handling:

- prefer `pathlib.Path` over manual path string manipulation

This matters immediately for the CLI todo app.

## 9. Basic Error Reading and Debugging

This week should already include debugging discipline.

You should learn to inspect:

- `SyntaxError`
- `NameError`
- `TypeError`
- `ValueError`
- `IndexError`
- `KeyError`

Do not panic when code fails. Read the traceback from bottom to top and identify:

- which line failed
- what object had the wrong type or value
- what assumption in your code was false

## 10. Basic Engineering Hygiene

Even in Week 01, start with good habits:

- meaningful variable names
- small functions
- no duplicated logic when avoidable
- comments only when they clarify intent
- simple README for runnable projects

Readability now will save time later.

## Best Learning Sequence For This Week

Use this order instead of jumping randomly:

1. variables, values, and printing
2. strings, numbers, booleans
3. lists and dicts
4. conditionals
5. loops
6. functions
7. file input/output
8. small CLI programs

This sequence works because each step depends naturally on the previous one.

## Recommended Daily Breakdown

This is a strong 7-day structure. If you are part-time, stretch it across more days but keep the order.

### Day 1: Python setup and primitives

Focus:

- install and run Python
- use the interpreter
- variables, types, and printing
- simple expressions

Build:

- tiny script doing arithmetic, string formatting, and input handling

### Day 2: Collections

Focus:

- lists, tuples, sets, dicts
- indexing and slicing
- adding, removing, updating values

Build:

- mini contact-book style data examples

### Day 3: Conditions and loops

Focus:

- branching
- `for` and `while`
- loop control
- truthiness

Build:

- number guessing logic
- menu-driven CLI prototype

### Day 4: Functions

Focus:

- parameters
- returns
- local scope
- decomposition

Build:

- refactor earlier logic into reusable functions

### Day 5: Strings and file I/O

Focus:

- text cleanup
- splitting and joining
- reading and writing files
- `pathlib`

Build:

- save and load simple records from text or JSON

### Day 6: Problem-solving practice

Focus:

- solve multiple small problems
- use functions and loops intentionally
- reduce brute-force messy logic

Build:

- 10-15 focused problems

### Day 7: Mini projects and cleanup

Focus:

- finish CLI calculator
- finish CLI todo app
- organize repo
- write README

## Problem-Solving Method You Should Practice

For each exercise, do not jump directly to code. Use this sequence:

1. Restate the problem in one sentence.
2. Define the inputs.
3. Define the expected output.
4. Write the steps in plain English.
5. Translate the steps into code.
6. Test with normal cases and edge cases.
7. Refactor only after it works.

This method matters more than solving one extra problem quickly.

## What Kind of Problems To Solve

Aim for 30-50 short problems, but choose them intentionally.

Cover these categories:

- arithmetic and conversion
- string manipulation
- list processing
- dict usage
- condition-based decisions
- counting and aggregation
- looping and pattern generation
- file read/write basics
- simple menu-based CLI logic

Good example tasks:

- check palindrome
- count vowels
- remove duplicates from a list
- find max or min manually
- frequency count of words
- reverse a string
- sum even numbers in a range
- merge two dict-like datasets logically
- read a text file and count lines or words

## Build Requirements

This week should produce two small but real programs.

## Project 1: CLI Calculator

Minimum features:

- add
- subtract
- multiply
- divide
- invalid input handling
- repeated menu loop until user exits

What this project should teach:

- branching
- functions
- user input
- validation
- clean control flow

Expert standard:

- separate math operations into functions
- do not put the entire program in one loop with tangled logic

## Project 2: CLI Todo App With File Storage

Minimum features:

- add task
- list tasks
- mark task complete
- delete task
- save tasks to file
- load tasks when program starts

Recommended storage:

- JSON file for simplicity and clarity

What this project should teach:

- lists of records
- dict-based task structure
- file persistence
- menu-driven CLI flow
- decomposition into helper functions

Expert standard:

- use one function per action
- keep storage logic separate from menu logic
- handle missing file or empty file safely

## Strong Folder Structure For Week 01

Recommended structure:

```text
week-01-python-core/
|-- exercises/
|   |-- basics/
|   |-- strings/
|   |-- lists/
|   |-- dicts/
|   |-- loops/
|   `-- functions/
|-- projects/
|   |-- cli-calculator/
|   `-- cli-todo-app/
|       `-- data/
|-- notes/
`-- README.md
```

This is enough structure for Week 01. Do not over-engineer it.

## Deliverables

By the end of this week, you should have:

- 30-50 Python practice problems
- one folder of categorized exercises
- one working CLI calculator
- one working CLI todo app with file persistence
- one short README explaining how to run both apps
- one short note summarizing what you learned and what confused you

## Exit Criteria

You are ready to move to Week 02 only if most of these are true:

- you can solve basic problems without constant syntax lookup
- you can choose between `list`, `set`, `tuple`, and `dict` for simple tasks
- you can write small functions comfortably
- you can debug common beginner errors without getting stuck for long
- you can read and write a simple file
- you can structure a CLI script into small pieces instead of one long script

If these are not true, repeat the week's exercises with better discipline instead of rushing forward.

## Common Beginner Mistakes To Avoid

- writing everything in one file with no functions
- using unclear variable names like `x`, `a`, `temp2` everywhere
- printing instead of returning from helper functions
- mutating data accidentally without realizing it
- confusing `=` with `==`
- using `is` when value comparison should use `==`
- skipping edge cases like empty input or divide-by-zero
- copying solutions without rewriting them from your own understanding

## Expert Notes That Matter Early

These are not advanced, but they separate strong beginners from weak ones.

### Clarity beats compactness

Shorter code is not automatically better. Readable code is better.

### Correctness before elegance

First make it work. Then make it cleaner.

### Functions are your first abstraction tool

Before learning classes or frameworks, learn to organize with functions well.

### Data structure choice matters

Many beginner solutions become messy simply because the wrong structure was chosen at the start.

### Debugging is part of learning

A week with many debugging cycles can be better than a week with passive reading.

## Suggested Official References

Use official Python docs first. These are especially useful for this week:

- Python Tutorial: introduction and core tutorial sections
- Control flow tools
- Data structures
- Modules
- `venv`
- `pathlib`
- PEP 8 style guidance

Official links:

- Python tutorial: https://docs.python.org/3/tutorial/
- Control flow: https://docs.python.org/3/tutorial/controlflow.html
- Data structures: https://docs.python.org/3/tutorial/datastructures.html
- Modules: https://docs.python.org/3/tutorial/modules.html
- `venv`: https://docs.python.org/3/library/venv.html
- `pathlib`: https://docs.python.org/3/library/pathlib.html
- PEP 8: https://peps.python.org/pep-0008/

## Final Standard For This Week

The correct outcome of Week 01 is not "I finished Python basics."

The correct outcome is:

"I can now think in Python well enough to build small programs, organize logic into functions, and move into the rest of the roadmap without syntax fear."
