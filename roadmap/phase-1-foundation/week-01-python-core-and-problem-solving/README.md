# Week 01: Python Core and Problem Solving

Back to [Phase 1](../README.md)

## Goal

Build enough real Python fluency that the language stops slowing you down.

By the end of this week, you should be able to:

- read small Python programs without feeling lost
- write short scripts from scratch without constant syntax lookup
- choose the right basic data structure for simple problems
- break logic into functions instead of writing one giant script
- debug common beginner errors without panic
- build two small CLI programs that actually work

This week is not about becoming "good at Python" in a broad sense. It is about building the operational base that every later week depends on.

If this week is weak:

- Week 02 will feel harder than it should
- API work in Week 03 will feel confusing
- SQL and data transformation will feel messier
- AI engineering later will be slower because structured data handling will still feel unnatural

If this week is strong, the rest of the roadmap becomes much more mechanical.

## What This Week Is Actually Training

At surface level, Week 01 looks like syntax practice. That is not the real training target.

The deeper skills being trained are:

- translating a vague problem into exact steps
- recognizing when data should be stored as a list, set, tuple, or dict
- separating input, processing, and output
- developing a debugging habit instead of a guessing habit
- learning to make code readable before trying to make it clever

That is why this week matters so much. Most weak beginners do not fail because they do not know enough syntax. They fail because they do not yet think in clear execution steps.

## Scope Boundaries

To avoid confusion, here is what belongs in Week 01 and what does not.

Study deeply this week:

- variables and values
- numbers, strings, booleans, `None`
- lists, tuples, sets, dicts
- `if`, `elif`, `else`
- `for`, `while`, `break`, `continue`
- functions, parameters, return values, scope
- string processing
- file reading and writing
- JSON basics
- `pathlib`
- reading tracebacks
- small CLI projects

Do not spend serious time on these yet:

- classes and object-oriented design
- decorators
- generators
- context manager internals
- advanced typing
- concurrency
- web frameworks
- data science libraries
- AI libraries

Those topics are not wrong. They are simply too early. Week 01 should optimize for clarity and control, not breadth.

## Week 01 Outcomes

You are successful this week if you can do most of the following without heavy assistance:

- explain the difference between mutable and immutable values
- explain when a `list` is better than a `set`
- write a function that takes inputs, computes a result, and returns it cleanly
- iterate through a collection and transform or filter values
- read from a file and write data back safely
- inspect an error message and identify what assumption failed
- build a menu-driven CLI program without collapsing into one giant loop

The target is not perfect memory. The target is working fluency.

## Pre-Week Setup Standard

Before you start the exercises, make sure your setup is stable.

Minimum environment:

- current Python 3.x installed
- editor with Python syntax highlighting
- terminal access
- one dedicated Week 01 working folder

Recommended project conventions from Day 1:

- create a `.venv` for project isolation
- keep one folder for exercises and one for projects
- use meaningful file names
- keep your scripts runnable from the terminal

Windows examples:

```powershell
py -m venv .venv
.venv\Scripts\activate
py --version
```

Cross-platform examples:

```bash
python -m venv .venv
python --version
```

Important practical note:

You do not need third-party packages for Week 01. Staying close to the standard library keeps the mental model clean.

## The Python Mental Model You Must Internalize

### Python is dynamically typed, not typeless

Python lets names point to objects of different types, but types still control behavior. A string is not a number, a list is not a dict, and a bug caused by wrong types is still a type bug.

### Variables are names bound to objects

Beginners often imagine variables as boxes. That mental model breaks down when mutability enters the picture.

This matters early because:

- assigning one list to another name does not create a copy
- updating mutable data can affect later logic unexpectedly
- understanding "what changed where" is a core debugging skill

### Control flow is decision logic

An `if` statement is not just syntax. It is an explicit branch in program behavior. A loop is not just repetition. It is a rule for visiting data or repeating work until a condition changes.

### Functions are your first abstraction boundary

Before classes, before frameworks, before architecture diagrams, your first engineering tool is the function.

A good first-week function:

- has one clear job
- has a name that explains intent
- returns data instead of only printing
- is small enough to reason about in one pass

### Readability is part of correctness

Code that is hard to read is harder to debug, harder to reuse, and easier to break later. In practice, unreadable code becomes incorrect code.

## Core Concepts To Master

## 1. Primitive and Core Built-In Types

You need strong working comfort with:

- `int`
- `float`
- `str`
- `bool`
- `None`
- `list`
- `tuple`
- `set`
- `dict`

Required understanding for each type:

- how to create it
- whether it is ordered
- whether it is mutable
- how to access values
- common operations
- the most typical use case

Practical usage model:

- `int` and `float`: arithmetic and counting
- `str`: user input, formatting, text parsing
- `bool`: decisions and conditions
- `None`: missing value or "no result yet"
- `list`: ordered collection you may change
- `tuple`: fixed grouping of values
- `set`: uniqueness and fast membership checks
- `dict`: keyed records and structured data

Expert note:

Many beginner problems are not algorithm problems. They are wrong-data-structure problems.

## 2. Expressions, Operators, and Truthiness

Be fluent with:

- arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- comparisons: `==`, `!=`, `<`, `<=`, `>`, `>=`
- logic: `and`, `or`, `not`
- membership: `in`, `not in`
- identity: `is`, `is not`

Critical distinction:

- use `==` for value comparison
- use `is` mainly for identity checks such as `value is None`

Truthiness is mandatory knowledge, not optional trivia.

Common falsey values:

- `False`
- `None`
- `0`
- `0.0`
- `""`
- `[]`
- `{}`
- `set()`

If you do not understand truthiness, your conditionals become fragile and your bug fixing becomes guesswork.

## 3. Control Flow

You need confident control over:

- `if`
- `elif`
- `else`
- `for`
- `while`
- `break`
- `continue`

Required judgment:

- use `for` when iterating over a collection or range
- use `while` when repetition depends on a changing condition
- break a complex condition into helper variables or helper functions when readability drops

Early engineering rule:

If branching becomes hard to read, the problem is often not Python syntax. The problem is missing decomposition.

## 4. Functions

This is the most important topic of the week.

You must understand:

- function definition
- parameters and arguments
- return values
- local scope
- default values at a basic level
- docstrings at a basic level

The biggest beginner mistake here is writing code that only prints and never returns.

Why that is a problem:

- returned values can be tested
- returned values can be reused
- returned values make functions composable
- print-heavy code becomes harder to verify and refactor

A good first-week function usually:

- accepts clear inputs
- computes one thing
- returns one clear result
- has a descriptive name

## 5. Strings and Text Handling

You must be comfortable with:

- indexing and slicing
- `.strip()`
- `.split()`
- `.join()`
- `.lower()`, `.upper()`
- substring checks
- f-strings

Why this matters:

- CLI tools are text-heavy
- configuration often starts as strings
- file content is often text
- later AI work relies on text normalization and formatting discipline

Preferred formatting style:

- use f-strings by default for readable interpolation

## 6. Iteration Patterns and Collections

Required patterns:

- iterating through lists
- iterating through dict keys and items
- counting with a dict
- accumulation with a variable
- filtering with `if`
- `enumerate()`
- `zip()`
- simple list comprehensions

Important boundary:

Use list comprehensions when they are clearly simpler. If the expression becomes mentally dense, switch back to a normal loop.

## 7. File I/O and JSON

By the end of the week, file handling should not feel mysterious.

You should know:

- how `with open(...)` works at the usage level
- reading text files
- writing text files
- appending safely
- reading and writing JSON with the `json` module
- why `pathlib.Path` is usually better than hand-building file paths as strings

This directly supports the todo app and also prepares you for later API work.

## 8. Error Reading and Debugging

You should become comfortable reading:

- `SyntaxError`
- `NameError`
- `TypeError`
- `ValueError`
- `IndexError`
- `KeyError`
- `FileNotFoundError`
- `ZeroDivisionError`

Debugging method:

1. Read the last line of the traceback to identify the error type.
2. Read the referenced file and line number.
3. Ask what the code expected to be true.
4. Ask what value or type actually appeared.
5. Reproduce the failure with the smallest possible input.
6. Fix the assumption, not just the symptom.

Strong beginner move:

Use `print()` strategically and, when needed, learn the absolute basics of `pdb` rather than editing code blindly.

## The Best Learning Order For This Week

Do not study this week randomly. Use this order:

1. running Python, variables, values, and expressions
2. strings, numbers, booleans, and type awareness
3. lists, tuples, sets, and dicts
4. conditionals and truthiness
5. loops and iteration patterns
6. functions and decomposition
7. file handling, JSON, and `pathlib`
8. debugging and cleanup
9. mini projects

This order matters because each layer reduces confusion in the next one.

## A No-Doubt Execution Plan For The Week

This is the recommended study sequence if you want clarity and momentum.

### Day 1: Setup, values, and basic execution

Study:

- how to run Python files
- `print()`
- variables
- numbers
- strings
- booleans
- simple expressions

Practice:

- unit conversion scripts
- string formatting examples
- input/output mini scripts

Checkpoint:

- can you explain what `type(value)` is telling you
- can you create and combine values without syntax friction

### Day 2: Core collections

Study:

- lists
- tuples
- sets
- dicts
- indexing
- slicing
- mutation

Practice:

- create a contact list
- count unique values with a set
- store named records in dicts

Checkpoint:

- can you explain why a dict is better than parallel lists for named records
- can you explain when a set is the cleanest tool

### Day 3: Conditions and loops

Study:

- comparison and logical operators
- truthiness
- `if/elif/else`
- `for`
- `while`
- `break`
- `continue`

Practice:

- grade calculator
- menu-driven prompt
- number guessing flow
- sum/count/filter exercises

Checkpoint:

- can you choose between `for` and `while` intentionally
- can you trace loop execution by hand

### Day 4: Functions and decomposition

Study:

- defining functions
- parameters
- return values
- local variables
- reuse

Practice:

- refactor earlier exercises into helper functions
- write validation functions
- write functions that transform a list or string

Checkpoint:

- can you explain the difference between returning and printing
- can you split one messy script into 3-5 useful functions

### Day 5: Files, JSON, and paths

Study:

- `with open(...)`
- read/write/append
- `json.load()` and `json.dump()`
- `Path` basics

Practice:

- save notes to a text file
- read records from JSON
- update stored tasks

Checkpoint:

- can you safely load and save persistent data
- can you explain why `Path("data") / "tasks.json"` is better than hand-built path strings

### Day 6: Problem-solving and debugging

Study:

- tracebacks
- debugging discipline
- reducing a problem to steps

Practice:

- solve 10-15 short problems
- intentionally revisit bugs from earlier files and fix them
- trace two or three broken examples line by line

Checkpoint:

- can you recover from ordinary errors without copying answers
- can you restate a problem in plain English first

### Day 7: Project completion and review

Build:

- finish CLI calculator
- finish CLI todo app
- clean folder structure
- review notes

Checkpoint:

- can you demo both projects from the terminal
- can you explain how the code is organized

## Problem-Solving Method To Practice On Every Exercise

Use the same disciplined flow every time:

1. Restate the problem in one sentence.
2. Write down the inputs.
3. Write down the expected output.
4. Describe the steps in plain English.
5. Choose the data structure before writing code.
6. Implement the smallest working version.
7. Test normal cases and edge cases.
8. Refactor only after the code works.

This is the real bridge from "learning syntax" to "learning engineering."

## What To Practice

Target range:

- 30-50 small problems across the week

Required categories:

- arithmetic and conversions
- text normalization
- list processing
- dict lookups and counting
- membership checks
- aggregation
- filtering
- basic file operations
- menu-driven CLI flow

Good Week 01 problem types:

- reverse a string
- count vowels
- check palindrome
- remove duplicates
- find a maximum manually
- count word frequency
- sum even numbers in a range
- validate menu choices
- load and update JSON records

## Project Standard For This Week

This week should produce two real mini-projects.

## Project 1: CLI Calculator

Minimum features:

- add
- subtract
- multiply
- divide
- invalid numeric input handling
- divide-by-zero protection
- repeat until user exits

What this project is training:

- input validation
- control flow
- decomposition
- function-level thinking

Correct implementation pattern:

- one function per operation
- one function to parse or validate input
- one main loop for menu control

## Project 2: CLI Todo App With File Storage

Minimum features:

- add task
- list tasks
- mark task complete
- delete task
- save tasks to file
- load tasks at startup

Recommended storage:

- JSON

What this project is training:

- dict-based records
- list updates
- persistence
- path handling
- separating storage logic from application logic

Correct implementation pattern:

- one file or module for storage
- one for business logic if the project grows
- one clear main program entry point

## Week 01 Folder Standard

Recommended structure:

```text
week-01-python-core-and-problem-solving/
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

This is enough structure. Do not overbuild your workspace this early.

## Best Sources For Week 01

Use sources in this order. This is the part that prevents confusion later.

### Tier 1: Official Python Sources

These should be your primary references.

1. Python tutorial
   Use this for the language fundamentals in the exact order most relevant to Week 01.
   Link: https://docs.python.org/3/tutorial/

2. Python tutorial: control flow tools
   Best source for `if`, `for`, functions, loop control, and pattern basics.
   Link: https://docs.python.org/3/tutorial/controlflow.html

3. Python tutorial: data structures
   Best source for lists, tuples, sets, dicts, and loop helpers.
   Link: https://docs.python.org/3/tutorial/datastructures.html

4. Python tutorial: input and output
   Use this for formatting, reading, and writing files.
   Link: https://docs.python.org/3/tutorial/inputoutput.html

5. Python tutorial: errors and exceptions
   Use this to understand how Python reports failures and how exceptions behave.
   Link: https://docs.python.org/3/tutorial/errors.html

6. `json` library docs
   Important because your todo app persistence should be simple and explicit.
   Link: https://docs.python.org/3/library/json.html

7. `pathlib` docs
   The right modern source for path handling.
   Link: https://docs.python.org/3/library/pathlib.html

8. `venv` docs
   Use this once, then treat it as normal project setup practice.
   Link: https://docs.python.org/3/library/venv.html

9. `pdb` docs
   You do not need all of it, but knowing the basics of stepping through code is valuable.
   Link: https://docs.python.org/3/library/pdb.html

10. PEP 8
    Use this as a style sanity check, not as something to memorize line by line.
    Link: https://peps.python.org/pep-0008/

11. PEP 20
    Short, but important for developing Python taste early.
    Link: https://peps.python.org/pep-0020/

### Tier 2: Best Structured Learning Companion

Use one strong teaching-oriented resource alongside the official docs, not ten mixed tutorials.

1. CS50P
   Best choice if you want a guided sequence with problem sets and solid pedagogy.
   Links:
   - https://cs50.harvard.edu/python/
   - https://pll.harvard.edu/course/cs50s-introduction-programming-python

How to use it for this roadmap:

- use the early CS50P sections to reinforce functions, conditionals, loops, exceptions, and file I/O
- do not let CS50P replace your own project building inside this roadmap
- use it as structured reinforcement, not as an excuse to delay implementation

### Tier 3: Practice Sources

Use one practice source consistently.

1. Exercism Python Track
   Strong for repetition, feedback, and deliberate practice.
   Links:
   - https://exercism.org/tracks/python
   - https://exercism.org/docs/tracks/python

How to use it well:

- solve exercises after you have studied the concept locally
- rewrite solutions in your own words
- do not optimize for exercise count

## Source Strategy That Avoids Confusion

If you mix too many random sources, Week 01 becomes noisy. Use this rule:

- official docs for truth
- one structured course for explanation
- one practice platform for repetition
- your own mini-projects for actual understanding

Recommended stack:

1. Python docs
2. your local exercises
3. CS50P for reinforcement
4. Exercism for extra drills

That stack is enough. Do not add five YouTube playlists and three paid courses on top.

## Exact Study Path Through The Sources

If you want zero ambiguity, use this order:

1. Read the relevant sections of the Python tutorial.
2. Implement the matching local exercises in this Week 01 folder.
3. Review mistakes and rewrite unclear code.
4. Use CS50P material to reinforce weak points.
5. Use Exercism only for extra repetition after the concept feels familiar.
6. Build the calculator.
7. Build the todo app.
8. Review your bugs and note what patterns caused them.

## Deliverables

By the end of the week, you should have:

- 30-50 short solved problems
- categorized exercise files
- one working CLI calculator
- one working CLI todo app with persistent storage
- short run instructions for each project
- a note capturing what felt easy, what felt hard, and what bugs repeated

## Exit Criteria

You are ready for Week 02 only if most of these are true:

- you can write short scripts without constant syntax lookup
- you can choose between `list`, `tuple`, `set`, and `dict` with reasonable confidence
- you can write helper functions naturally
- you can read and write JSON-backed local data
- you can understand common traceback messages
- you can keep a small CLI program organized instead of writing one monolithic script

If these are not true, do not rush forward. Repeat the exercises and improve the projects.

## Common Mistakes That Create Doubt Later

- learning syntax passively without building
- copying solutions too early
- studying advanced topics before the basics feel stable
- using too many tutorial sources at once
- confusing printing with returning
- writing long scripts with no decomposition
- ignoring tracebacks and debugging by random edits
- skipping file I/O because it feels boring

These mistakes compound. Fix them early.

## Expert Notes

### You are not learning Python to become a Python trivia machine

You are learning Python so later backend, data, and AI tasks become straightforward to express.

### Data structure choice is an engineering decision

Choosing the right container early often matters more than writing fancy logic later.

### Debugging is not a side activity

Debugging is part of the skill itself. A learner who debugs well progresses faster than one who only reads well.

### You should leave Week 01 with habits, not just notes

Useful habits:

- restate the problem before coding
- test small pieces early
- return values from functions
- keep files readable
- use clear names

## How Week 01 Connects To Week 02

Week 02 assumes you already have:

- language comfort
- small-function discipline
- file handling basics
- basic project structure awareness

Week 02 will start introducing stronger engineering habits, validation, environments, modules, packaging awareness, and testing discipline. If Python syntax is still shaky, that week will feel much harder.

That is why Week 01 should be taken seriously.

## Final Standard For This Week

The correct outcome is not:

"I finished Python basics."

The correct outcome is:

"I can think in Python well enough to solve beginner problems, organize code into functions, store simple data, debug ordinary failures, and move into the rest of the roadmap without language fear."
