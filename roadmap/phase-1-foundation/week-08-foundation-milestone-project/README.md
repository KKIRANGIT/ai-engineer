# Week 08: Foundation Milestone Project

Back to [Phase 1](../README.md)

## Goal

Combine the Phase 1 skills into one credible, small full-stack product that proves you can design, build, test, document, and explain a working application from end to end.

This week is not another topic week. It is the week where the earlier topics stop being isolated lessons and become one engineering artifact.

## Why This Week Matters

Without a milestone project, Phase 1 can become a false sense of progress:

- you touched Python
- you touched APIs
- you touched SQL
- you touched JavaScript
- you touched Docker

That is not the same as building a real product.

Week 08 matters because it forces you to combine:

- problem framing
- scope control
- backend logic
- data modeling
- API design
- frontend interaction
- validation
- local setup discipline
- documentation quality

The project does not need to be impressive in size. It needs to be coherent, explainable, and complete.

## What This Week Is Really Training

At a deeper level, this milestone trains six professional habits.

### 1. Synthesis

Can you connect separate technical skills into one system instead of treating each topic as isolated practice?

### 2. Product scoping

Can you choose a version of the idea that is small enough to finish but real enough to discuss?

### 3. Architectural judgment

Can you choose a structure that is clean without becoming overengineered?

### 4. Boundary discipline

Can you handle user input, database writes, route errors, and UI states without relying on the happy path?

### 5. Explanation quality

Can you explain what you built, why you structured it that way, and what tradeoffs you chose?

### 6. Finishability

Can you turn a technical week into a portfolio-shaped artifact with code, tests, setup docs, and a reasonable demo story?

## Scope Boundary

This week is not for:

- adding authentication just because it sounds advanced
- building a multi-user production SaaS
- chasing visual perfection
- adopting a framework you do not understand yet
- adding features that exist only to increase scope

This week is for:

- one complete small product
- clear backend logic
- a meaningful UI flow
- a sensible database model
- stable local execution
- a project you can actually demo and discuss

## Week 08 Outcomes

By the end of this week, you should be able to:

- define a small product scope with clear in-scope and out-of-scope boundaries
- design a practical relational schema
- implement a backend with routing, validation, and storage
- connect a browser UI to backend endpoints
- test key backend behavior
- document local setup and architecture clearly
- explain the project like a real engineering artifact instead of a tutorial clone

## Workspace Structure

This week now includes a full milestone workspace:

```text
week-08-foundation-milestone-project/
|-- README.md
|-- exercises/
|   |-- README.md
|   |-- planning/
|   |   `-- 01-milestone-brief-template.md
|   |-- design/
|   |   `-- 02-schema-and-route-worksheet.md
|   `-- review/
|       `-- 03-demo-readiness-checklist.md
|-- projects/
|   `-- study-session-tracker/
|       |-- README.md
|       |-- .env.example
|       |-- Dockerfile
|       |-- data/
|       |   `-- .gitkeep
|       |-- sql/
|       |   `-- schema.sql
|       |-- src/
|       |   |-- app.py
|       |   |-- config.py
|       |   |-- db.py
|       |   |-- repository.py
|       |   |-- response_utils.py
|       |   |-- server.py
|       |   |-- service.py
|       |   |-- static_handler.py
|       |   |-- validation.py
|       |   `-- static/
|       |       |-- app.js
|       |       |-- index.html
|       |       `-- styles.css
|       `-- tests/
|           |-- test_repository.py
|           `-- test_service.py
`-- notes/
    |-- 01-week-plan.md
    |-- 02-architecture-explainer.md
    `-- 03-portfolio-and-demo-guide.md
```

## What To Practice This Week

## 1. Project Framing

Before touching implementation, define:

- who the product is for
- what one user can do in the product
- what the core entities are
- what success looks like by the end of the week
- what you are intentionally not building

This is not optional overhead. It is how you prevent scope drift.

## 2. Data Modeling

A milestone project should have a schema you can explain.

For the included project, the model is:

- `subjects`
- `study_sessions`

This lets you practice:

- one-to-many relationships
- foreign keys
- lookup and summary queries
- basic reporting over stored records

## 3. Backend Flow

You should be able to point to each layer and explain its job:

- request entrypoint
- route handling
- validation
- service logic
- repository/database layer
- JSON response shaping

If all logic collapses into one file, the milestone becomes harder to explain and maintain.

## 4. Frontend Integration

The frontend for this week should be simple, but it must be real.

That means:

- forms that send data
- fetch calls to the backend
- rendering lists or summaries
- handling loading, success, and error states at a basic level

Do not mistake "a browser page exists" for actual frontend integration.

## 5. Validation and Error Handling

You should validate:

- missing or empty fields
- invalid numeric values
- invalid date strings
- missing related records
- delete attempts for missing IDs

The app should remain understandable when something goes wrong.

## 6. Documentation and Demo Thinking

A finished milestone project includes:

- clear setup instructions
- route overview
- explanation of data model
- explanation of tradeoffs
- a demo story you can walk through

That is part of the engineering outcome, not decorative cleanup.

## Best Learning Sequence For This Week

Use this order:

1. review the milestone brief and scope
2. inspect the schema and route design
3. understand the backend structure
4. understand the frontend request/response flow
5. run the application
6. inspect the tests
7. write your own short architecture explanation

## Recommended Daily Breakdown

### Day 1: Product framing

Focus:

- read the Week 08 README
- complete the planning exercise
- understand the project boundaries

Deliverable:

- one-page project brief in your own words

### Day 2: Schema and backend structure

Focus:

- study the schema
- inspect repository and service layers
- map each route to the database operations it needs

Deliverable:

- backend flow notes

### Day 3: Validation and API behavior

Focus:

- inspect input validation
- test bad payloads mentally and locally
- understand how error responses are shaped

Deliverable:

- a short list of handled edge cases

### Day 4: Frontend interaction

Focus:

- inspect `index.html`, `styles.css`, and `app.js`
- trace how forms trigger API calls
- understand how the page refreshes state

Deliverable:

- explanation of one full UI workflow

### Day 5: Testing and debugging

Focus:

- run the test suite
- inspect repository and service tests
- connect the tests back to the project requirements

Deliverable:

- test-driven understanding of core logic

### Day 6: Run and review the full app

Focus:

- run the application locally
- create subjects and sessions
- verify summary and delete behavior

Deliverable:

- a working local demo

### Day 7: Portfolio framing

Focus:

- read the portfolio and demo notes
- write your own explanation of tradeoffs and future improvements

Deliverable:

- a stronger project discussion narrative

## Main Project

The included milestone project is:

- [projects/study-session-tracker](projects/study-session-tracker/README.md)

It is intentionally chosen to be:

- small enough to finish and understand
- relational enough to practice real schema thinking
- product-like enough to demo
- simple enough to avoid framework confusion

The project combines:

- Python backend routing
- SQLite persistence
- JSON API endpoints
- browser-based UI
- JavaScript frontend fetch calls
- environment-based configuration
- optional Docker packaging

## Build Quality Standard

For this milestone, "working once" is not enough.

Minimum quality bar:

- the application starts reliably
- the schema is understandable
- the code is split by responsibility
- inputs are validated
- obvious errors are handled
- the frontend can complete the core workflow
- the README explains local execution
- tests cover core backend behavior

## Deliverables

By the end of this week, you should have:

- one complete milestone project
- one planning and scoping exercise set
- one working full-stack app
- a clean project README
- tests for core backend behavior
- architecture and portfolio notes

## Exit Criteria

You are ready to move on to Phase 2 only if:

- you can explain the project scope clearly
- you can explain the schema and relationships clearly
- you can explain how a browser action reaches the backend and the database
- you can demo the main workflow without confusion
- you can explain at least two tradeoffs you made
- another person could run the project locally from the README

## Common Mistakes To Avoid

- choosing abstraction over clarity
- adding features before stabilizing the core workflow
- treating the frontend as an afterthought
- skipping validation because the UI usually sends valid data
- avoiding tests because the app "looks fine"
- writing documentation after you already forgot the reasoning

## Expert Notes That Matter Early

### A small finished product beats a large unfinished idea

Milestone quality is judged by coherence and completion, not by feature count.

### Architecture should fit the scale

This project uses lightweight Python and browser tooling on purpose. The right question is not whether the stack is trendy. The right question is whether the structure teaches the correct engineering habits.

### A portfolio artifact needs a story

If you cannot explain the user, workflow, data model, and tradeoffs, the code alone will not carry the project well in interviews or reviews.

## Suggested References

Prioritize official docs:

1. Python `sqlite3` docs  
   https://docs.python.org/3/library/sqlite3.html
2. Python `wsgiref` docs  
   https://docs.python.org/3/library/wsgiref.html
3. Python `json` docs  
   https://docs.python.org/3/library/json.html
4. Python `pathlib` docs  
   https://docs.python.org/3/library/pathlib.html
5. MDN Fetch API  
   https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
6. MDN HTML forms guide  
   https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms
7. Docker getting started docs  
   https://docs.docker.com/get-started/

Use the docs for correctness, but use this week's workspace as the place where the ideas become concrete.

## Final Standard For This Week

The correct outcome of Week 08 is not:

"I built something small."

The correct outcome is:

"I shipped one small but credible full-stack product, and I can explain its scope, schema, backend flow, frontend flow, validation strategy, and tradeoffs with confidence."
