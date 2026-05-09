# Week 06: Async Python, Data Pipelines, and Docker

Back to [Phase 1](../README.md)

## Goal

Learn how slightly more realistic backend and data-processing workflows are structured, especially when work involves multiple inputs, file movement, I/O waiting, transformations, and repeatable runtime environments.

This week introduces three ideas that show up constantly later:

- concurrency for I/O-heavy work
- data ingestion and transformation
- containerized execution

By the end of this week, you should be able to:

- explain the difference between synchronous and asynchronous I/O
- know when async helps and when it does not
- use `async`, `await`, and `asyncio.gather()` at a practical level
- read and transform CSV data
- understand the stages of a simple data pipeline
- explain what Docker is solving
- run one Dockerized Python pipeline project

This week is where application code starts looking more like real workflow automation.

## What This Week Is Actually Training

At surface level, Week 06 looks like "learn async, learn CSV processing, and try Docker."

The real training target is deeper:

- recognizing where time is spent waiting vs computing
- breaking workflow code into clear pipeline stages
- understanding reproducibility as an engineering requirement
- moving from one-step scripts to multi-stage processing systems
- thinking about input, validation, transformation, enrichment, and output as distinct concerns

That is why this week matters so much. Many later AI and product workflows are pipeline-shaped:

- fetch source material
- parse and validate it
- transform it
- enrich it
- store it
- export or serve it

Week 06 is the early version of that mindset.

## Scope Boundaries

Study deeply this week:

- sync vs async I/O thinking
- `async`, `await`, and `asyncio.gather`
- I/O-bound concurrency
- CSV reading and writing
- simple tabular transformation
- pipeline stages
- Docker mental model
- containerizing one small Python project

Do not go deep on these yet:

- advanced event loop internals
- multiprocessing performance tuning
- orchestration platforms
- distributed pipelines
- advanced Pandas internals
- Kubernetes
- production-grade container security hardening

The goal is operational understanding, not platform specialization.

## Important Implementation Note

This hands-on workspace is designed to be runnable with minimal setup.

That means:

- the main project uses the Python standard library
- async is demonstrated through local file and simulated I/O workflows
- Docker is applied to a small deterministic pipeline project
- Pandas is introduced as an optional learning layer, not as a hard dependency for the main project

This keeps the week beginner-usable while still teaching correct engineering ideas.

## Week 06 Outcomes

You are successful this week if you can do most of the following with confidence:

- explain why async helps some tasks and not others
- identify an I/O-bound workflow
- describe the stages of a pipeline in the correct order
- clean and transform tabular data intentionally
- explain the purpose of Docker in plain English
- read one Dockerfile and explain what each section is doing
- run one local pipeline end-to-end and inspect its outputs

## How Week 06 Builds On Week 05

Week 05 taught you how data should be shaped inside a relational system.

Week 06 teaches you how data often arrives and moves before or around that database layer.

Now the questions are:

- where does the data come from
- what should happen while we wait for it
- how should it be cleaned
- how should transformed output be saved
- how can we make this reproducible on another machine

That is why this week sits naturally after SQL and before more advanced backend work.

## Core Workflow Concepts To Master

## 1. Sync vs Async Mental Model

Synchronous code:

- does one thing at a time
- often waits during network or file operations

Asynchronous code:

- can switch to other work while one task is waiting on I/O
- is especially useful when many tasks spend time waiting

Critical beginner rule:

Async is not automatically faster in every situation. It is mainly valuable when the bottleneck is waiting, not pure CPU computation.

## 2. When Async Helps

Good use cases:

- multiple HTTP requests
- many file reads or writes
- message polling
- waiting on remote services

Poor use cases:

- tiny scripts with no real I/O pressure
- CPU-heavy number crunching
- code made more complicated only to "use async"

Use async because the workload needs it, not because the syntax looks advanced.

## 3. `async`, `await`, and Coroutines

You should understand:

- `async def` defines a coroutine function
- calling an async function gives you a coroutine object
- `await` pauses until an awaited operation is ready
- `asyncio.gather()` lets you wait for multiple tasks together

You do not need deep event-loop theory this week. You do need enough practical understanding to reason about the code.

## 4. Pipeline Thinking

A pipeline is a sequence of stages such as:

- ingest
- validate
- normalize
- enrich
- save
- report

Pipeline thinking is powerful because it forces you to separate concerns. That makes workflows easier to debug and extend later.

## 5. CSV and Tabular Data

You should become comfortable with:

- reading CSV files
- inspecting headers
- cleaning malformed values
- filtering rows
- writing cleaned output

This is still very real engineering work. Many integration and support systems start with messy tabular data.

## 6. Pandas as an Optional Analysis Layer

You do not need all of Pandas this week.

You should understand:

- why tabular libraries exist
- how they can simplify filtering and grouping
- that they are a tool, not a replacement for relational thinking

The exercise layer includes an optional Pandas demo, but the main project avoids requiring it.

## 7. Docker Mental Model

Before commands, understand the problem Docker solves:

- environment drift
- dependency mismatch
- "works on my machine"

You need to know:

- image = build artifact
- container = running instance
- `Dockerfile` describes how to build the image

Docker is a reproducibility tool before it is a deployment story.

## 8. Practical Containerization

For this week, containerization should stay simple:

- one Python application
- one `Dockerfile`
- one run command
- one deterministic output flow

This is enough to make the concept real.

## Best Learning Sequence For This Week

Use this order:

1. sync vs async model
2. `async` / `await` basics
3. concurrent I/O thinking
4. pipeline stages
5. CSV and transformation work
6. optional Pandas awareness
7. Docker mental model
8. containerizing the local pipeline project

## A No-Doubt Execution Plan For The Week

### Day 1: Async mental model

Study:

- waiting vs computing
- sync vs async flow
- coroutines

Practice:

- run the async-basics exercise
- compare the sync and async timing behavior

Checkpoint:

- can you explain why the async example overlaps waiting time

### Day 2: Concurrent orchestration

Study:

- `asyncio.gather`
- task coordination
- error awareness

Practice:

- run the concurrency exercise
- inspect how multiple I/O-style tasks are collected

Checkpoint:

- can you explain what work is happening concurrently

### Day 3: CSV processing

Study:

- headers
- row cleaning
- value normalization

Practice:

- run the CSV cleaning exercise
- inspect the output rows carefully

Checkpoint:

- can you explain which rows needed cleaning and why

### Day 4: Pipeline stages

Study:

- ingest
- validate
- transform
- enrich
- save

Practice:

- run the pipeline-thinking exercise
- map each step in the main project to one stage

Checkpoint:

- can you describe the pipeline as a sequence of stages without talking about code first

### Day 5: Optional Pandas awareness

Study:

- why Pandas exists
- when it helps

Practice:

- run the optional Pandas demo if Pandas is installed
- otherwise read the code and compare it to the pure-Python workflow

Checkpoint:

- can you explain where Pandas would help and where simple Python is enough

### Day 6: End-to-end project

Build:

- run the event-ingestion pipeline
- inspect the generated outputs
- read the repository structure and Dockerfile

Checkpoint:

- can you explain each file's role in the project

### Day 7: Docker and review

Study:

- Dockerfile structure
- image build idea
- run command

Practice:

- inspect the Dockerfile and README
- compare local execution to containerized execution

Checkpoint:

- can you explain what Docker solved for this project

## Week 06 Workspace Standard

This week now includes a real hands-on pipeline workspace.

Actual structure:

```text
week-06-async-python-data-pipelines-and-docker/
|-- exercises/
|   |-- async-basics/
|   |-- concurrency/
|   |-- csv-processing/
|   |-- pandas-basics/
|   |-- pipeline-thinking/
|   |-- docker-reading/
|   `-- README.md
|-- projects/
|   `-- event-ingestion-pipeline/
|       |-- app/
|       |-- data/
|       |-- output/
|       |-- tests/
|       |-- .env.example
|       |-- .dockerignore
|       |-- Dockerfile
|       `-- README.md
|-- notes/
`-- README.md
```

## Main Build Goals

This week has one core project plus focused exercises.

### Layer 1: Async and data-processing drills

The exercises help you isolate:

- async mental model
- concurrency patterns
- CSV cleanup
- pipeline stage thinking
- optional Pandas comparison

### Layer 2: End-to-end event-ingestion pipeline

The main project demonstrates:

- async orchestration of data loading
- CSV normalization
- JSON enrichment
- output generation
- containerization with Docker

## Deliverables

By the end of the week, you should have:

- completed the async and pipeline exercises
- run the local pipeline project
- inspected the generated output files
- reviewed the Dockerfile and run instructions
- written a short note on when async helped and when it would be unnecessary

## Best Sources For Week 06

Use sources in this order.

### Tier 1: Official Python Sources

1. Python `asyncio` documentation
   Link: https://docs.python.org/3/library/asyncio.html

2. Python `csv` documentation
   Link: https://docs.python.org/3/library/csv.html

3. Python `asyncio.gather` task docs
   Link: https://docs.python.org/3/library/asyncio-task.html

### Tier 2: Optional Tabular Tooling

1. Pandas 10 minutes to pandas
   Link: https://pandas.pydata.org/docs/user_guide/10min.html

Use this selectively. It is an optional comparison layer this week, not the center of the main project.

### Tier 3: Official Docker Sources

1. Docker get started
   Link: https://docs.docker.com/get-started/

2. Dockerfile reference
   Link: https://docs.docker.com/reference/dockerfile/

Use these to understand how the local pipeline gets packaged into a reproducible runtime.

## Source Strategy That Avoids Confusion

For Week 06, use this source stack:

1. official Python docs for async and CSV truth
2. local exercises for mental-model reinforcement
3. optional Pandas docs only after the pure-Python path is clear
4. official Docker docs for container understanding
5. the local event-ingestion pipeline for real understanding

That stack is enough.

## Exact Study Path Through The Sources

If you want the least ambiguity, use this sequence:

1. read the `asyncio` overview
2. run the async-basics and concurrency exercises
3. read the `csv` docs selectively
4. run the CSV and pipeline-thinking exercises
5. inspect the event-ingestion pipeline project
6. optionally review the Pandas quickstart
7. read the Docker get-started and Dockerfile reference
8. inspect the Dockerfile and project README

## Exit Criteria

You are ready for Week 07 only if most of these are true:

- you know when async is appropriate
- you can read `async` and `await` code without panic
- you can describe a simple pipeline in stages
- you can clean and transform tabular data intentionally
- you can explain what Docker is solving
- you can run and explain the local pipeline project

If these are not true, repeat the async and pipeline work before moving on.

## Common Mistakes That Create Confusion Later

- using async for work that has no real I/O waiting
- confusing concurrency with parallel CPU execution
- writing pipeline code with no clear stages
- forcing Pandas into problems that simple Python can already express clearly
- copying Dockerfiles without understanding what each line is for

## Expert Notes

### Async is a tool, not a badge

Use it when waiting is the bottleneck and the coordination benefit is real.

### Pipelines are about flow and boundaries

Clear stages usually matter more than clever code.

### Docker solves reproducibility first

Do not frame Docker only as deployment technology. It is also a consistency tool.

## How Week 06 Connects To Week 07

Week 07 introduces JavaScript, TypeScript, Node.js, and backend basics.

That week becomes easier if Week 06 is strong because workflow thinking already improves:

- data flow reasoning
- project structure
- environment awareness
- runtime reproducibility

Week 06 helps you reason about systems, not just files.

## Final Standard For This Week

The correct outcome is not:

"I tried async and Docker."

The correct outcome is:

"I understand the shape of I/O-heavy data workflows, I can use async where it makes sense, I can reason about pipeline stages clearly, and I can package one Python project into a reproducible container."
