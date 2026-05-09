# AI Engineer Preparation Workspace

This repository is a structured, execution-focused workspace for completing a 48-week AI engineer preparation roadmap.

It is not just a reading repository. It is designed to become a working learning system with:

- long-form roadmap guidance
- decomposed phase and weekly study modules
- source-code workspaces for hands-on learning
- notes, exercises, and reference material
- a reusable course agent prompt for guided study sessions

## Repository Purpose

The main goal of this repository is to help you prepare across the full AI engineer path:

- Phase 1: foundation skills
- Phase 2: AI core systems
- Phase 3: full-stack AI product engineering
- Phase 4: real product building
- Phase 5: career, monetization, and positioning

The repository is optimized for:

- beginner clarity
- expert-level depth
- direct execution
- clean study sequencing
- practical project building

## Top-Level Structure

```text
ai-engineer/
|-- README.md
|-- AI_Guide.md
|-- ai-detailed-preparation-guide.md
|-- roadmap-master-reference.md
|-- .agents/
`-- roadmap/
```

## What Each Top-Level File Is For

### `AI_Guide.md`

The concise original guide.

Use this when you want a shorter roadmap view.

### `ai-detailed-preparation-guide.md`

The expanded long-form master guide.

Use this when you want the full 48-week narrative in one file.

### `roadmap-master-reference.md`

The governing repository reference.

Use this when you want:

- structure rules
- update standards
- current completion state
- future update expectations

This should be the first context file for major future updates.

### `roadmap/`

The operational version of the course.

This is where the real phase-by-phase and week-by-week learning content lives.

### `.agents/`

Reusable agent prompts for this workspace.

This is where the course-specific learning agent lives.

## Roadmap Structure

The `roadmap/` folder is organized like this:

```text
roadmap/
|-- README.md
|-- 00-overview/
|-- phase-1-foundation/
|-- phase-2-ai-core/
|-- phase-3-full-stack-ai-product-engineering/
|-- phase-4-build-3-real-products/
|-- phase-5-career-monetization-and-positioning/
`-- 90-reference/
```

### `00-overview/`

Global context for how to use the roadmap, what stack assumptions it uses, and what artifacts you should produce.

### `phase-*`

Each phase contains:

- a phase `README.md`
- weekly folders
- each week folder has its own `README.md`
- some weeks also include exercises, projects, notes, and source code

### `90-reference/`

Cross-phase support material such as:

- execution systems
- project quality standards
- interview preparation
- consulting/freelance readiness
- portfolio sequencing
- official reference links

## Current Implementation Status

At the current stage of the repository:

- all major roadmap phases have expanded planning layers
- `00-overview` has been deeply expanded
- `90-reference` has been deeply expanded
- Phase 1 Week 01 has a full hands-on workspace
- Phase 1 Week 02 has a full hands-on workspace
- Phase 1 Week 03 has a full hands-on workspace
- Phase 1 Week 04 has a full hands-on workspace
- Phase 1 Week 05 has a full hands-on workspace
- Phase 1 Week 06 has a full hands-on workspace
- Phase 1 Week 07 has a full hands-on workspace
- Phase 1 Week 08 has a full hands-on workspace
- Phase 2 Week 09 has a full hands-on workspace
- Phase 2 Week 10 has a full hands-on workspace
- Phase 2 Week 11 has a full hands-on workspace
- Phase 2 Week 12 has a full hands-on workspace
- Phase 2 Week 13 has a full hands-on workspace
- Phase 2 Week 14 has a full hands-on workspace
- Phase 2 Week 15 has a full hands-on workspace
- Phase 2 Week 16 has a full hands-on workspace
- Phase 2 Week 17 has a full hands-on workspace
- Phase 2 Week 18 has a full hands-on workspace
- later weeks mostly have detailed planning but not yet full implementation workspaces

This means the roadmap is structurally mature, but implementation depth is still growing week by week.

## Best Starting Points

If you are new to this workspace, use this order:

1. [roadmap-master-reference.md](roadmap-master-reference.md)
2. [roadmap/README.md](roadmap/README.md)
3. [roadmap/00-overview/05-how-to-use-this-guide.md](roadmap/00-overview/05-how-to-use-this-guide.md)
4. [roadmap/phase-1-foundation/README.md](roadmap/phase-1-foundation/README.md)
5. the current week you are actively studying

If you are starting the course from the beginning:

1. read [week-01-python-core-and-problem-solving/README.md](roadmap/phase-1-foundation/week-01-python-core-and-problem-solving/README.md)
2. work through its `exercises/`
3. build and inspect its `projects/`
4. move to Week 02 only after the Week 01 exit criteria are actually true

## How To Study This Repository Properly

This repository is designed to be used actively.

For each week:

1. read the week `README.md`
2. understand the goal, weekly outcomes, and exit criteria
3. work through the exercises
4. study the project code
5. run the project locally
6. write your own notes
7. do not move forward until you can explain what you built

Do not treat the roadmap as a passive reading list.

## Current Hands-On Weeks

### Week 01

Location:

- [week-01-python-core-and-problem-solving](roadmap/phase-1-foundation/week-01-python-core-and-problem-solving/)

Includes:

- exercises
- CLI calculator
- CLI todo app
- notes
- beginner-friendly source code with explanatory comments

### Week 02

Location:

- [week-02-python-engineering-basics](roadmap/phase-1-foundation/week-02-python-engineering-basics/)

Includes:

- engineering exercises
- refactored multi-module todo app
- tests
- `.env.example`
- notes
- stronger module, validation, JSON, and testing patterns

### Week 03

Location:

- [week-03-http-apis-and-integration-thinking](roadmap/phase-1-foundation/week-03-http-apis-and-integration-thinking/)

Includes:

- HTTP and API exercises
- public API exploration scripts
- reusable GitHub API client project
- unit tests for parsing and helper logic
- notes for debugging and API workflow

### Week 04

Location:

- [week-04-git-github-linux-cli-and-developer-workflow](roadmap/phase-1-foundation/week-04-git-github-linux-cli-and-developer-workflow/)

Includes:

- Git and terminal workflow exercises
- a local Git practice sandbox
- a reusable Python starter template
- a working GitHub Actions workflow example
- notes for command fluency and workflow discipline

### Week 05

Location:

- [week-05-sql-postgres-and-data-modeling](roadmap/phase-1-foundation/week-05-sql-postgres-and-data-modeling/)

Includes:

- SQL and schema-design exercises
- a query-lab project with schema, seed, and query files
- a relational CRUD demo built with Python and SQLite
- unit tests for the project repository layer
- notes for query writing and schema review

### Week 06

Location:

- [week-06-async-python-data-pipelines-and-docker](roadmap/phase-1-foundation/week-06-async-python-data-pipelines-and-docker/)

Includes:

- async and pipeline exercises
- a Dockerized event-ingestion pipeline project
- generated-output workflow concepts
- unit tests for the pipeline logic
- notes for async, pipeline, and Docker understanding

### Week 07

Location:

- [week-07-javascript-typescript-nodejs-and-backend-basics](roadmap/phase-1-foundation/week-07-javascript-typescript-nodejs-and-backend-basics/)

Includes:

- JavaScript, async, TypeScript, backend, and validation exercises
- a dependency-light Node reading-list API
- unit tests using Node's built-in test runner
- a TypeScript reference layer for contract thinking
- notes for Python-vs-JavaScript and backend mental models

### Week 08

Location:

- [week-08-foundation-milestone-project](roadmap/phase-1-foundation/week-08-foundation-milestone-project/)

Includes:

- milestone planning and review exercises
- a full-stack study-session tracker
- Python backend, SQLite database, and browser frontend integration
- unit tests for repository and service logic
- notes for architecture, demo framing, and portfolio discussion

### Week 09

Location:

- [week-09-llm-fundamentals-and-api-literacy](roadmap/phase-2-ai-core/week-09-llm-fundamentals-and-api-literacy/)

Includes:

- LLM concepts, payload, and debugging exercises
- a provider-aware API playground with mock and live modes
- tests for payload building, cost estimation, and trace logging
- notes for provider comparison and API debugging

### Week 10

Location:

- [week-10-prompt-engineering-and-structured-outputs](roadmap/phase-2-ai-core/week-10-prompt-engineering-and-structured-outputs/)

Includes:

- prompt clarity, decomposition, structure, and schema exercises
- a structured-output support-ticket triage lab
- tests for schema validation, prompt rendering, regression behavior, and request payloads
- notes for prompt design and structured-output review

### Week 11

Location:

- [week-11-embeddings-semantic-search-and-retrieval-basics](roadmap/phase-2-ai-core/week-11-embeddings-semantic-search-and-retrieval-basics/)

Includes:

- embeddings, chunking, filtering, and search-mode exercises
- a semantic search playground with keyword, semantic, and hybrid retrieval
- tests for chunking, similarity, retrieval behavior, and evaluation
- notes for retrieval debugging and hosted-vs-self-managed reasoning

### Week 12

Location:

- [week-12-rag-done-properly](roadmap/phase-2-ai-core/week-12-rag-done-properly/)

Includes:

- RAG pipeline, query rewrite, context packing, and failure-analysis exercises
- a grounded policy assistant with retrieval inspection and citations
- tests for query rewriting, context assembly, grounded answer generation, and evaluation
- notes for RAG debugging and grounded UX

### Week 13

Location:

- [week-13-tool-use-and-function-calling](roadmap/phase-2-ai-core/week-13-tool-use-and-function-calling/)

Includes:

- tool-loop, schema-design, validation, and provider-payload exercises
- a local operations assistant with multiple tools and execution traces
- tests for validation, tool execution, and end-to-end orchestration
- notes for tool design, provider differences, and study flow

### Week 14

Location:

- [week-14-agents-and-workflow-orchestration](roadmap/phase-2-ai-core/week-14-agents-and-workflow-orchestration/)

Includes:

- workflow-vs-agent, ReAct, state, retry, and framework-positioning exercises
- a research brief orchestrator implemented in direct, graph, and agent-loop styles
- tests for workflow behavior and orchestration modes
- notes for orchestration judgment, review checkpoints, and framework choice

### Week 15

Location:

- [week-15-evals-prompt-optimization-and-fine-tuning-decisions](roadmap/phase-2-ai-core/week-15-evals-prompt-optimization-and-fine-tuning-decisions/)

Includes:

- success-criteria, dataset-design, grader, regression, and fine-tuning-decision exercises
- a ticket triage eval lab with multiple system variants and comparison reports
- tests for graders, variant analysis, and decision memo generation
- notes for eval design, optimization discipline, and fine-tuning judgment

### Week 16

Location:

- [week-16-multimodal-and-realtime-ai](roadmap/phase-2-ai-core/week-16-multimodal-and-realtime-ai/)

Includes:

- multimodal, voice, vision, streaming, and session-design exercises
- an incident assistant multimodal lab with text-only, multimodal, and session modes
- tests for session behavior and streaming chunk generation
- notes for modality design, latency, and realtime tradeoffs

### Week 17

Location:

- [week-17-safety-observability-and-cost-control](roadmap/phase-2-ai-core/week-17-safety-observability-and-cost-control/)

Includes:

- trust-boundary, guardrail, observability, retry, and cost-control exercises
- a guarded support assistant lab with trace logging, safety screening, retries, and budget checks
- tests for guardrails, budget estimation, and guarded request processing
- notes for failure-mode review, hardening logic, and safety-cost design

### Week 18

Location:

- [week-18-ai-milestone-product](roadmap/phase-2-ai-core/week-18-ai-milestone-product/)

Includes:

- capstone exercises for scope control, pattern selection, retrieval design, evaluation, and case-study framing
- a support-ops copilot milestone product with retrieval, structured output, tools, traces, guardrails, and evals
- tests for retrieval, integrated ticket analysis, and the milestone eval suite
- notes for architecture framing, scope discipline, and portfolio storytelling

## Repository Standards

This workspace follows a few important rules:

- weekly content belongs inside week folders
- roadmap content should remove ambiguity, not create it
- official docs are preferred for technical correctness
- content should be expert-level but beginner-usable
- source code should be readable and teach good habits
- comments should explain intent, not narrate every line

These standards are formalized in [roadmap-master-reference.md](roadmap-master-reference.md).

## Documentation Sync Rule

This repository is README-driven by design. That means when a workspace section changes, the related documentation must be updated in the same task so the learning system stays coherent.

The expected sync pattern is:

- week-level changes -> update that week `README.md`
- phase-level changes -> update that phase `README.md`
- roadmap navigation or status changes -> update [roadmap/README.md](roadmap/README.md)
- repository-level usage or structure changes -> update this root `README.md`
- repository rules or maintenance standards changes -> update [roadmap-master-reference.md](roadmap-master-reference.md)
- agent behavior changes -> update the relevant files in [.agents](.agents/)

In this repository, documentation sync is part of the implementation standard, not optional cleanup.

## Using The Course Agent

This repository includes a reusable course agent prompt:

- [.agents/ai-engineer-course-agent.md](.agents/ai-engineer-course-agent.md)
- [.agents/workspace-prompt-guide.md](.agents/workspace-prompt-guide.md)

Use that file when you want an AI assistant to act as:

- your phase-aware learning coach
- your code explainer
- your implementation guide
- your weekly reviewer
- your debugging and next-step planner

Recommended usage:

1. provide [roadmap-master-reference.md](roadmap-master-reference.md)
2. provide the relevant week folder or README
3. tell the agent your current goal
4. ask it to stay aligned with the workspace rules and documentation sync requirements

See [.agents/README.md](.agents/README.md) for usage guidance.

If you want copy-paste prompt templates for study sessions, code explanation, repository updates, debugging, and readiness review, start with [.agents/workspace-prompt-guide.md](.agents/workspace-prompt-guide.md).

## Suggested Update Workflow

When requesting future improvements to this repository, use this pattern:

1. mention `roadmap-master-reference.md`
2. specify the target week, phase, or reference section
3. say whether you want planning, source code, notes, templates, or all of them
4. say whether the update should optimize for beginner clarity, interview depth, or production realism

Example:

`Use roadmap-master-reference.md as context and expand Week 03 with source code, exercises, and notes.`

## Verification Notes

Some Python workspaces in this repository have already been syntax-checked with `python -m compileall`.

Testing support exists for Week 02, but `pytest` is not currently installed in the active environment, so the tests are present but may require installation before execution.

## Recommended Next Steps

The highest-value next repository upgrades are:

- continue building the remaining Phase 2 hands-on workspaces from Week 13 onward
- add a progress tracker across all 48 weeks
- add review templates and project case-study templates
- keep the top-level roadmap index synchronized with detailed content

## Summary

This repository is now a serious AI engineer preparation workspace rather than a loose set of notes.

Use:

- `roadmap-master-reference.md` for rules and structure
- `roadmap/` for the operational learning path
- `.agents/ai-engineer-course-agent.md` for guided study sessions
