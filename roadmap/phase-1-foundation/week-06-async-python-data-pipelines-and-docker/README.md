# Week 06: Async Python, Data Pipelines, and Docker

Back to [Phase 1](../README.md)

## Goal

Learn how slightly more realistic backend and data-processing workflows are structured, especially when work involves multiple inputs, external calls, file movement, and repeatable runtime environments.

This week introduces three ideas that show up constantly later:

- concurrency for I/O-heavy work
- data ingestion and transformation
- containerized execution

## Why This Week Matters

By now you have learned syntax, structure, integration basics, and databases. The next step is understanding how real engineering tasks often involve:

- fetching data from multiple places
- transforming it into a useful format
- storing or exporting it
- running the same workflow across machines predictably

This week matters because many later AI tasks are pipeline-shaped:

- fetch content
- parse it
- transform it
- enrich it
- store it
- serve it

Async thinking and pipeline thinking are the early versions of that skill.

## Week 06 Outcomes

By the end of this week, you should be able to:

- explain the difference between synchronous and asynchronous I/O
- know when async is helpful and when it is not
- perform concurrent API requests with `httpx`
- read and process CSV data
- use basic Pandas operations for tabular transformation
- containerize one Python project with Docker
- explain what problem Docker is solving

## What To Learn

## 1. Sync vs Async Mental Model

Before code, understand the runtime idea.

Synchronous code:

- does one thing at a time
- often waits during network or file operations

Asynchronous code:

- can switch tasks while one task is waiting for I/O
- is especially useful for many network-bound operations

Expert beginner rule:

Async does not automatically mean faster in every case. It is mainly useful when time is spent waiting on external I/O.

## 2. When Async Helps

Good use cases:

- multiple API requests
- network scraping
- waiting on remote services

Poor use cases:

- tiny scripts with no I/O pressure
- CPU-heavy workloads where async alone does not solve the bottleneck

This distinction matters. Many beginners misuse async because they learn the syntax before the reason.

## 3. `async`, `await`, and Coroutines

You should understand:

- what an `async def` function is
- what `await` means
- why awaited tasks pause until results are ready
- how coroutines differ from regular functions conceptually

The goal is not to master advanced event loop internals. The goal is to understand enough to use async intentionally.

## 4. Concurrent HTTP Work With `httpx`

This is the most practical async use case for the week.

Learn:

- creating an async client
- sending multiple requests
- collecting results safely
- basic error handling in concurrent tasks

Expert note:

Do not treat concurrency as "send unlimited requests." Responsible concurrency also means being aware of rate limits and load.

## 5. Data Pipeline Mental Model

A pipeline is just a sequence of transformations:

- ingest
- validate
- transform
- enrich
- save

This week should help you think in those stages clearly.

Good pipeline questions:

- where does the data come from
- what format is it in
- what cleaning is needed
- what output do I want
- where should the cleaned data go

## 6. CSV Handling

You should be comfortable with:

- reading CSV files
- inspecting headers
- cleaning missing or malformed values
- writing cleaned output

This is still very practical work. A lot of backend and AI support tasks begin here.

## 7. Basic Pandas

Do not try to learn all of Pandas this week.

Focus on:

- loading tabular data
- filtering rows
- selecting columns
- grouping
- simple transformation

Expert beginner rule:

Use Pandas for tabular manipulation when it helps clarity. Do not force it for every tiny task.

## 8. Environment Isolation and Reproducibility

Before Docker, understand the problem:

- different machines have different environments
- dependencies drift
- "works on my machine" is a real failure mode

This week should make you value reproducibility as an engineering concern.

## 9. Docker Mental Model

You do not need deep container orchestration. You need the basic model:

- Docker packages your app plus its environment
- the image is the build artifact
- the container is the running instance

Understand:

- what a `Dockerfile` does
- why dependency installation goes into the image
- why a container helps environment consistency

## 10. Practical Containerization

For this week, containerization should be simple:

- one Python service or script
- one `Dockerfile`
- one command to run it

The point is to understand the workflow, not to build a production container platform.

## Best Learning Sequence For This Week

Use this order:

1. sync vs async model
2. async syntax
3. concurrent HTTP calls
4. pipeline stages
5. CSV and Pandas basics
6. Docker mental model
7. containerizing one service

## Recommended Daily Breakdown

### Day 1: Async concept and examples

Focus:

- why async exists
- where it helps
- basic syntax

Build:

- tiny async example and comparison with sync flow

### Day 2: Concurrent API requests

Focus:

- async HTTP client
- gathering multiple results

Build:

- small concurrent API fetcher

### Day 3: CSV and data transformation

Focus:

- reading rows
- cleaning values
- transforming fields

Build:

- one small CSV cleaning script

### Day 4: Pandas basics

Focus:

- loading data
- filtering
- grouping
- exporting

Build:

- simple analysis notebook or script

### Day 5: Pipeline assembly

Focus:

- connect fetch, clean, and save stages

Build:

- one end-to-end data pipeline

### Day 6: Docker fundamentals

Focus:

- image vs container
- Dockerfile layers
- run commands

Build:

- Dockerize one Python project

### Day 7: Comparison and review

Focus:

- when async helped
- when it added unnecessary complexity
- what Docker solved

## Build Plan

This week should produce three concrete outputs.

### 1. Async API scraper

Requirements:

- call multiple endpoints
- collect results
- handle failures reasonably
- compare behavior with a sync version if possible

### 2. CSV-to-structured-output pipeline

Requirements:

- load CSV
- clean selected fields
- transform the data
- write the result back to a file or database

### 3. Dockerized Python service or script

Requirements:

- working `Dockerfile`
- documented build and run commands
- minimal assumptions about host machine setup

## Deliverables

By the end of this week, you should have:

- one async HTTP project or script
- one small data pipeline project
- one Dockerized Python project
- one short note comparing sync vs async for your use case
- one README explaining how to run the containerized project

## Exit Criteria

You are ready to move on only if:

- you know when async is appropriate
- you can use `async` and `await` without total confusion
- you can process simple CSV or tabular data
- you can explain the stages of a basic data pipeline
- you can build and run one simple Dockerized Python project

## Common Mistakes To Avoid

- using async for problems that do not benefit from it
- confusing concurrency with parallel CPU execution
- writing pipeline code with no clear stages
- using Pandas for everything without understanding the underlying transformation
- copying Dockerfiles without understanding what each line does

## Expert Notes That Matter Early

### Async is a tool, not a badge

Use it when the workload is I/O-bound and the coordination benefit is real.

### Pipelines are about shape and flow

Clear stages often matter more than clever code.

### Docker solves reproducibility first

Do not frame it only as deployment technology. It is also a consistency tool.

## Suggested References

- Python async documentation
- `httpx` documentation
- CSV and Pandas documentation
- Docker getting-started documentation

## Final Standard For This Week

The correct outcome of Week 06 is not "I tried async and Docker."

The correct outcome is:

"I understand the shape of I/O-heavy data workflows, I can use async where it makes sense, and I can package one Python project into a reproducible container."
