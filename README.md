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
- later weeks mostly have detailed planning but not yet full implementation workspaces

This means the roadmap is structurally mature, but implementation depth is still growing week by week.

## Best Starting Points

If you are new to this workspace, use this order:

1. [roadmap-master-reference.md](/d:/Tutorials/InterviewPraparation/ai-engineer/roadmap-master-reference.md)
2. [roadmap/README.md](/d:/Tutorials/InterviewPraparation/ai-engineer/roadmap/README.md)
3. [roadmap/00-overview/05-how-to-use-this-guide.md](/d:/Tutorials/InterviewPraparation/ai-engineer/roadmap/00-overview/05-how-to-use-this-guide.md)
4. [roadmap/phase-1-foundation/README.md](/d:/Tutorials/InterviewPraparation/ai-engineer/roadmap/phase-1-foundation/README.md)
5. the current week you are actively studying

If you are starting the course from the beginning:

1. read [week-01-python-core-and-problem-solving/README.md](/d:/Tutorials/InterviewPraparation/ai-engineer/roadmap/phase-1-foundation/week-01-python-core-and-problem-solving/README.md)
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

- [week-01-python-core-and-problem-solving](</d:/Tutorials/InterviewPraparation/ai-engineer/roadmap/phase-1-foundation/week-01-python-core-and-problem-solving>)

Includes:

- exercises
- CLI calculator
- CLI todo app
- notes
- beginner-friendly source code with explanatory comments

### Week 02

Location:

- [week-02-python-engineering-basics](</d:/Tutorials/InterviewPraparation/ai-engineer/roadmap/phase-1-foundation/week-02-python-engineering-basics>)

Includes:

- engineering exercises
- refactored multi-module todo app
- tests
- `.env.example`
- notes
- stronger module, validation, JSON, and testing patterns

### Week 03

Location:

- [week-03-http-apis-and-integration-thinking](</d:/Tutorials/InterviewPraparation/ai-engineer/roadmap/phase-1-foundation/week-03-http-apis-and-integration-thinking>)

Includes:

- HTTP and API exercises
- public API exploration scripts
- reusable GitHub API client project
- unit tests for parsing and helper logic
- notes for debugging and API workflow

### Week 04

Location:

- [week-04-git-github-linux-cli-and-developer-workflow](</d:/Tutorials/InterviewPraparation/ai-engineer/roadmap/phase-1-foundation/week-04-git-github-linux-cli-and-developer-workflow>)

Includes:

- Git and terminal workflow exercises
- a local Git practice sandbox
- a reusable Python starter template
- a working GitHub Actions workflow example
- notes for command fluency and workflow discipline

### Week 05

Location:

- [week-05-sql-postgres-and-data-modeling](</d:/Tutorials/InterviewPraparation/ai-engineer/roadmap/phase-1-foundation/week-05-sql-postgres-and-data-modeling>)

Includes:

- SQL and schema-design exercises
- a query-lab project with schema, seed, and query files
- a relational CRUD demo built with Python and SQLite
- unit tests for the project repository layer
- notes for query writing and schema review

### Week 06

Location:

- [week-06-async-python-data-pipelines-and-docker](</d:/Tutorials/InterviewPraparation/ai-engineer/roadmap/phase-1-foundation/week-06-async-python-data-pipelines-and-docker>)

Includes:

- async and pipeline exercises
- a Dockerized event-ingestion pipeline project
- generated-output workflow concepts
- unit tests for the pipeline logic
- notes for async, pipeline, and Docker understanding

### Week 07

Location:

- [week-07-javascript-typescript-nodejs-and-backend-basics](</d:/Tutorials/InterviewPraparation/ai-engineer/roadmap/phase-1-foundation/week-07-javascript-typescript-nodejs-and-backend-basics>)

Includes:

- JavaScript, async, TypeScript, backend, and validation exercises
- a dependency-light Node reading-list API
- unit tests using Node's built-in test runner
- a TypeScript reference layer for contract thinking
- notes for Python-vs-JavaScript and backend mental models

### Week 08

Location:

- [week-08-foundation-milestone-project](</d:/Tutorials/InterviewPraparation/ai-engineer/roadmap/phase-1-foundation/week-08-foundation-milestone-project>)

Includes:

- milestone planning and review exercises
- a full-stack study-session tracker
- Python backend, SQLite database, and browser frontend integration
- unit tests for repository and service logic
- notes for architecture, demo framing, and portfolio discussion

## Repository Standards

This workspace follows a few important rules:

- weekly content belongs inside week folders
- roadmap content should remove ambiguity, not create it
- official docs are preferred for technical correctness
- content should be expert-level but beginner-usable
- source code should be readable and teach good habits
- comments should explain intent, not narrate every line

These standards are formalized in [roadmap-master-reference.md](/d:/Tutorials/InterviewPraparation/ai-engineer/roadmap-master-reference.md).

## Documentation Sync Rule

This repository is README-driven by design. That means when a workspace section changes, the related documentation must be updated in the same task so the learning system stays coherent.

The expected sync pattern is:

- week-level changes -> update that week `README.md`
- phase-level changes -> update that phase `README.md`
- roadmap navigation or status changes -> update [roadmap/README.md](/d:/Tutorials/InterviewPraparation/ai-engineer/roadmap/README.md)
- repository-level usage or structure changes -> update this root `README.md`
- repository rules or maintenance standards changes -> update [roadmap-master-reference.md](/d:/Tutorials/InterviewPraparation/ai-engineer/roadmap-master-reference.md)
- agent behavior changes -> update the relevant files in [.agents](</d:/Tutorials/InterviewPraparation/ai-engineer/.agents>)

In this repository, documentation sync is part of the implementation standard, not optional cleanup.

## Using The Course Agent

This repository includes a reusable course agent prompt:

- [.agents/ai-engineer-course-agent.md](/d:/Tutorials/InterviewPraparation/ai-engineer/.agents/ai-engineer-course-agent.md)
- [.agents/workspace-prompt-guide.md](/d:/Tutorials/InterviewPraparation/ai-engineer/.agents/workspace-prompt-guide.md)

Use that file when you want an AI assistant to act as:

- your phase-aware learning coach
- your code explainer
- your implementation guide
- your weekly reviewer
- your debugging and next-step planner

Recommended usage:

1. provide [roadmap-master-reference.md](/d:/Tutorials/InterviewPraparation/ai-engineer/roadmap-master-reference.md)
2. provide the relevant week folder or README
3. tell the agent your current goal
4. ask it to stay aligned with the workspace rules and documentation sync requirements

See [.agents/README.md](/d:/Tutorials/InterviewPraparation/ai-engineer/.agents/README.md) for usage guidance.

If you want copy-paste prompt templates for study sessions, code explanation, repository updates, debugging, and readiness review, start with [.agents/workspace-prompt-guide.md](/d:/Tutorials/InterviewPraparation/ai-engineer/.agents/workspace-prompt-guide.md).

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

- begin building Phase 2 hands-on workspaces
- add a progress tracker across all 48 weeks
- add review templates and project case-study templates
- keep the top-level roadmap index synchronized with detailed content

## Summary

This repository is now a serious AI engineer preparation workspace rather than a loose set of notes.

Use:

- `roadmap-master-reference.md` for rules and structure
- `roadmap/` for the operational learning path
- `.agents/ai-engineer-course-agent.md` for guided study sessions
