# AI Engineer Roadmap Master Reference

## Purpose

This document is the single source of truth for how this AI engineer preparation repository is structured, what each major document is for, what standards future updates must follow, and what has already been completed.

Use this file when:

- you want to understand the overall roadmap system quickly
- you want to request updates without repeating earlier decisions
- you want to know where content belongs
- you want to preserve consistency across future expansions

This file is not the study roadmap itself. It is the governing reference for the roadmap.

## Primary Goal

The overall goal of this repository is to provide a complete, detailed, execution-focused preparation system for becoming an AI engineer across a 48-week plan.

The roadmap is intended to support:

- strong technical foundation building
- AI engineering capability development
- full-stack AI product engineering
- product portfolio creation
- career positioning, monetization, and interview readiness

The roadmap should be detailed enough that you can follow it with minimal ambiguity and without constantly wondering what to study next.

## Core Documents

These are the top-level documents and their roles.

### `README.md`

Purpose:

- repository entry point
- quick orientation document
- explains how to use the workspace and the course agent

Rule:

- keep this as the best starting point for someone opening the repository fresh
- it should summarize structure without trying to replace the full roadmap

### `AI_Guide.md`

Purpose:

- original or concise reference guide
- higher-level planning artifact

Rule:

- keep this as the shorter source document
- do not overload it with all implementation details

### `ai-detailed-preparation-guide.md`

Purpose:

- expanded master roadmap for the full 48-week journey
- detailed long-form preparation guide

Rule:

- this is the comprehensive roadmap narrative
- it should remain useful as a standalone long-form guide

### `roadmap/`

Purpose:

- decomposed operational version of the preparation plan
- phase-by-phase and week-by-week implementation structure

Rule:

- detailed day-to-day or week-level execution belongs here

### `.agents/`

Purpose:

- reusable agent prompts for this workspace
- supports guided study sessions and repository-aware assistance

Rule:

- agent prompts should be repository-aware, phase-aware, and consistent with this master reference
- do not store generic prompts here that ignore the local roadmap structure
- keep a practical prompt guide there when the workspace needs reusable prompt templates

### `roadmap-master-reference.md`

Purpose:

- the current file
- central context file for future updates
- source of truth for structure, standards, and current completion state

## Directory Structure Standard

Current structure:

```text
ai-engineer/
|-- README.md
|-- AI_Guide.md
|-- ai-detailed-preparation-guide.md
|-- roadmap-master-reference.md
|-- .agents/
`-- roadmap/
    |-- README.md
    |-- 00-overview/
    |-- phase-1-foundation/
    |-- phase-2-ai-core/
    |-- phase-3-full-stack-ai-product-engineering/
    |-- phase-4-build-3-real-products/
    |-- phase-5-career-monetization-and-positioning/
    `-- 90-reference/
```

## Roadmap Folder Rules

### `roadmap/README.md`

Purpose:

- top-level navigation for the decomposed roadmap
- should link to every phase and major reference section

### `roadmap/00-overview/`

Purpose:

- global context for the roadmap
- usage model, stack guidance, expectations, capability framing, and artifacts

### `roadmap/phase-*`

Purpose:

- each phase contains one phase `README.md`
- each weekly unit has its own folder
- each weekly folder contains its own `README.md`

Important rule:

- weekly content should live inside week-specific folders, not as loose flat files

### `roadmap/90-reference/`

Purpose:

- reusable cross-phase reference material
- execution systems, quality standards, interview prep, consulting readiness, portfolio guidance, common mistakes, and official links

## Weekly Folder Standard

Each week folder should follow this minimum structure:

```text
week-xx-topic/
`-- README.md
```

If that week includes implementation artifacts, it can also include:

```text
week-xx-topic/
|-- README.md
|-- exercises/
|-- projects/
|-- notes/
`-- resources/
```

Rule:

- do not add folders just for visual complexity
- add subfolders only when they serve real study or implementation value

## Week README Standard

Every weekly `README.md` should be written as an execution document, not a skeleton note.

At minimum, each week should include:

- goal
- why the week matters
- what this week is actually training
- scope boundaries where useful
- weekly outcomes
- concept breakdown
- best learning sequence
- daily or staged execution plan
- what to practice
- what to build
- deliverables
- exit criteria
- common mistakes
- expert notes
- final standard for the week

Additional requirement:

- the week should remove ambiguity about what to study next
- the user should be able to follow it directly

## Phase README Standard

Each phase `README.md` should act as the governing document for the phase.

At minimum, each phase README should include:

- phase goal
- why the phase matters
- what the phase should produce
- deeper skills being trained
- success criteria
- how to use the weekly modules
- links to all week folders

## Documentation Sync Standard

This repository depends on README-driven clarity. That means documentation sync is not optional maintenance. It is part of the actual work.

Whenever a meaningful change is made, the related documentation must be updated in the same change set.

### Sync Rules By Scope

If a week folder changes, update the week `README.md`.

Examples:

- new exercises added
- new project folder added
- new notes added
- code structure changed
- learning sequence changed
- deliverables or exit criteria changed

If a phase structure or week status changes, update the phase `README.md`.

Examples:

- a week becomes a full hands-on workspace
- the phase sequencing changes
- phase-level expectations change

If roadmap-level navigation changes, update `roadmap/README.md`.

Examples:

- new folders added
- phase status materially changes
- reference sections expand or move

If repository-level structure or usage changes, update the root `README.md`.

Examples:

- new top-level files added
- new reusable agent added
- new standard workflow introduced

If repository rules, maintenance expectations, or update discipline change, update `roadmap-master-reference.md`.

Examples:

- new documentation standards
- new source policies
- new structure rules
- new sync requirements

If agent behavior or workflow expectations change, update the related files in `.agents/`.

Examples:

- course agent responsibilities change
- new default context order
- new repository maintenance rules

### Completion Rule

A repository update is not fully complete until the affected documentation layers are synchronized.

At minimum, check:

- local week `README.md`
- parent phase `README.md` when relevant
- `roadmap/README.md` when navigation or status changes
- root `README.md` when repository entry guidance changes
- `roadmap-master-reference.md` when standards or structure rules change
- `.agents/` files when the agent's operating behavior changes

## Content Quality Standard

All expanded roadmap content should follow these principles:

- practical over theoretical
- detailed over vague
- structured over scattered
- expert-level but beginner-usable
- operational rather than inspirational
- clear sequencing rather than topic dumping

Avoid:

- thin checklist-style notes with no learning logic
- generic motivational language
- shallow summaries without execution details
- stuffing too many tools or sources into one week

## Source Selection Standard

When recommending learning sources, use this priority:

1. official documentation
2. one strong structured course if needed
3. one high-quality practice source if needed
4. local exercises and projects as the main proving ground

Important source rule:

- avoid recommending too many mixed resources in the same week
- the roadmap should reduce source confusion, not create it

## Current Source Philosophy

The roadmap has been aligned around modern official sources where time-sensitive topics matter.

Examples of source categories already used:

- Python official documentation
- Python Packaging User Guide
- OpenAI official documentation
- Anthropic official documentation
- React official documentation
- Next.js official documentation
- Supabase official documentation
- official or primary-source references for stack decisions

## Update Standard For Time-Sensitive Topics

For stack choices, APIs, libraries, and platform guidance:

- prefer current official documentation
- avoid relying on stale tutorial assumptions
- include exact versions or concrete names when relevant
- clarify dates when discussing "latest" technology

This especially applies to:

- Python version guidance
- Node.js guidance
- React and Next.js guidance
- OpenAI API usage
- Anthropic API usage
- retrieval, evals, tool use, and agent orchestration guidance

## What Has Already Been Completed

The following major work has already been done.

### 1. Detailed master guide created

Completed:

- `ai-detailed-preparation-guide.md`

Status:

- expanded into a much more complete 48-week preparation guide

### 2. Roadmap decomposed into structured folders

Completed:

- `roadmap/` created
- phase and weekly structure created
- each week moved into its own folder with `README.md`

### 3. `00-overview` expanded

Completed:

- `roadmap/00-overview/*`

Status:

- rewritten with much deeper context, stack framing, usage guidance, artifacts, and capability mapping

### 4. Phase 1 planning layer expanded

Completed:

- `roadmap/phase-1-foundation/README.md`
- Week 01 through Week 08 READMEs

Status:

- detailed execution-focused planning is in place

### 5. Phase 1 Week 01 hands-on workspace created

Completed:

- exercises
- beginner-friendly source code
- CLI calculator
- CLI todo app
- notes and supporting documentation

Location:

- `roadmap/phase-1-foundation/week-01-python-core-and-problem-solving/`

### 6. Phase 1 Week 02 hands-on workspace created

Completed:

- engineering exercises
- refactored multi-module todo app
- tests
- `.env.example`
- notes and supporting documentation

Location:

- `roadmap/phase-1-foundation/week-02-python-engineering-basics/`

### 7. Phase 1 Week 03 hands-on workspace created

Completed:

- HTTP and API exercises
- public API exploration scripts
- reusable GitHub API client project
- unit tests
- notes and supporting documentation

Location:

- `roadmap/phase-1-foundation/week-03-http-apis-and-integration-thinking/`

### 8. Phase 1 Week 04 hands-on workspace created

Completed:

- Git and terminal workflow exercises
- local Git practice sandbox
- reusable Python starter template
- GitHub Actions workflow example
- notes and supporting documentation

Location:

- `roadmap/phase-1-foundation/week-04-git-github-linux-cli-and-developer-workflow/`

### 9. Phase 1 Week 05 hands-on workspace created

Completed:

- SQL and schema-design exercises
- SQL query lab
- relational CRUD demo project
- unit tests
- notes and supporting documentation

Location:

- `roadmap/phase-1-foundation/week-05-sql-postgres-and-data-modeling/`

### 10. Phase 1 Week 06 hands-on workspace created

Completed:

- async and pipeline exercises
- Dockerized event-ingestion pipeline project
- unit tests
- notes and supporting documentation

Location:

- `roadmap/phase-1-foundation/week-06-async-python-data-pipelines-and-docker/`

### 11. Phase 1 Week 07 hands-on workspace created

Completed:

- JavaScript and TypeScript exercises
- dependency-light Node backend project
- unit tests using Node's built-in test runner
- TypeScript reference layer
- notes and supporting documentation

Location:

- `roadmap/phase-1-foundation/week-07-javascript-typescript-nodejs-and-backend-basics/`

### 12. Phase 1 Week 08 hands-on workspace created

Completed:

- milestone planning exercises
- full-stack study-session tracker project
- repository and service tests
- architecture and portfolio notes
- supporting documentation

Location:

- `roadmap/phase-1-foundation/week-08-foundation-milestone-project/`

### 13. Phase 2 planning layer expanded

Completed:

- `roadmap/phase-2-ai-core/README.md`
- Week 09 through Week 18 READMEs

Status:

- rewritten into detailed expert-level planning documents

### 14. Phase 2 Week 09 hands-on workspace created

Completed:

- concepts, payload, and debugging exercises
- provider-aware LLM API playground
- tests for clients, cost estimation, and logging
- notes and supporting documentation

Location:

- `roadmap/phase-2-ai-core/week-09-llm-fundamentals-and-api-literacy/`

### 15. Phase 2 Week 10 hands-on workspace created

Completed:

- prompt clarity, decomposition, and schema exercises
- structured-output support-ticket triage lab
- tests for prompt rendering, validation, regression, and payload construction
- notes and supporting documentation

Location:

- `roadmap/phase-2-ai-core/week-10-prompt-engineering-and-structured-outputs/`

### 16. Phase 2 Week 11 hands-on workspace created

Completed:

- embeddings, chunking, filtering, and search-mode exercises
- semantic search playground project
- tests for similarity, chunking, retrieval, and evaluation
- notes and supporting documentation

Location:

- `roadmap/phase-2-ai-core/week-11-embeddings-semantic-search-and-retrieval-basics/`

### 17. Phase 2 Week 12 hands-on workspace created

Completed:

- RAG pipeline, query rewrite, context packing, and failure-analysis exercises
- grounded policy assistant project
- tests for query rewriting, context building, answer generation, and evaluation
- notes and supporting documentation

Location:

- `roadmap/phase-2-ai-core/week-12-rag-done-properly/`

### 18. Phase 2 Week 13 hands-on workspace created

Completed:

- tool-loop, schema-design, validation, and provider-payload exercises
- local operations assistant lab
- tests for validation, deterministic tools, and orchestration
- notes and supporting documentation

Location:

- `roadmap/phase-2-ai-core/week-13-tool-use-and-function-calling/`

### 19. Phase 2 Week 14 hands-on workspace created

Completed:

- orchestration exercises covering workflows, ReAct loops, state, retries, and framework positioning
- research brief orchestrator project with direct, graph-style, and agent-loop modes
- tests for workflow behavior and orchestration modes
- notes and supporting documentation

Location:

- `roadmap/phase-2-ai-core/week-14-agents-and-workflow-orchestration/`

### 20. Phase 2 Week 15 hands-on workspace created

Completed:

- eval-design exercises covering success criteria, dataset quality, graders, regressions, and fine-tuning decisions
- ticket triage eval lab with baseline, prompt-improved, and retrieval-aware system variants
- tests for grading, analysis, and decision memo behavior
- notes and supporting documentation

Location:

- `roadmap/phase-2-ai-core/week-15-evals-prompt-optimization-and-fine-tuning-decisions/`

### 21. Phase 2 Week 16 hands-on workspace created

Completed:

- multimodal exercises covering modality transitions, voice pipelines, vision task framing, and streaming sessions
- incident assistant multimodal lab with text-only, multimodal, and session modes
- tests for session behavior and streaming output
- notes and supporting documentation

Location:

- `roadmap/phase-2-ai-core/week-16-multimodal-and-realtime-ai/`

### 22. Phase 2 Week 17 hands-on workspace created

Completed:

- safety exercises covering trust boundaries, prompt-injection awareness, observability, retries, and cost control
- guarded support assistant lab with trace logging, safety screening, retry behavior, and budget checks
- tests for guardrails, budget estimation, and request processing
- notes and supporting documentation

Location:

- `roadmap/phase-2-ai-core/week-17-safety-observability-and-cost-control/`

### 23. Phase 2 Week 18 hands-on workspace created

Completed:

- capstone exercises covering pattern selection, retrieval and structure design, evaluation, and case-study framing
- support ops copilot milestone product with retrieval, structured output, deterministic tools, guardrails, traces, cost estimation, and evals
- tests for retrieval, integrated ticket analysis, and the milestone evaluation suite
- notes and supporting documentation

Location:

- `roadmap/phase-2-ai-core/week-18-ai-milestone-product/`

### 24. Phase 3 planning layer expanded

Completed:

- `roadmap/phase-3-full-stack-ai-product-engineering/README.md`
- Week 19 through Week 28 READMEs

### 25. Phase 4 planning layer expanded

Completed:

- `roadmap/phase-4-build-3-real-products/README.md`
- product-track READMEs for Weeks 29 through 38

### 26. Phase 5 planning layer expanded

Completed:

- `roadmap/phase-5-career-monetization-and-positioning/README.md`
- Week 39 through Week 48 READMEs

### 27. `90-reference` expanded

Completed:

- all reference documents under `roadmap/90-reference/`

Status:

- now functions as a full companion operating handbook rather than a short appendix

### 28. Week 01 Python guide deepened further

Completed:

- `roadmap/phase-1-foundation/week-01-python-core-and-problem-solving/README.md`

Status:

- strengthened with stricter learning boundaries, no-doubt study order, stronger source strategy, and better official references

### 29. Repository entry README and course agent created

Completed:

- `README.md`
- `.agents/README.md`
- `.agents/ai-engineer-course-agent.md`

Status:

- repository now has a clear entry point and a reusable workspace-specific learning agent prompt

### 30. Workspace prompt guide created

Completed:

- `.agents/workspace-prompt-guide.md`

Status:

- repository now includes reusable prompt templates for learning, code explanation, debugging, repository updates, and documentation-sync-aware agent usage

## Current Completion State

At this point:

- all major phase planning layers are expanded
- all overview and reference layers are expanded
- Week 01, Week 02, Week 03, Week 04, Week 05, Week 06, Week 07, Week 08, Week 09, Week 10, Week 11, Week 12, Week 13, Week 14, Week 15, Week 16, Week 17, and Week 18 have both planning and implementation artifacts
- later weeks mostly have planning layers but not yet full source-code workspaces

This means the roadmap is structurally strong, but implementation depth is still uneven across weeks.

## What Future Updates Should Usually Focus On

The highest-value next steps usually fall into one of these categories:

### 1. Build implementation workspaces for later weeks

Examples:

- later Phase 2 and Phase 3 project folders

### 2. Improve top-level navigation

Examples:

- keep `roadmap/README.md` synchronized with all expanded sections
- improve cross-linking between phases and references

### 3. Add study-operating assets

Examples:

- progress tracker
- weekly review templates
- project case study templates
- interview prep templates

### 4. Continue source-hardening

Examples:

- adding stronger official references inside specific weeks
- removing ambiguity from later technical weeks

## How To Request Future Updates

To keep future updates clean, reference this file and then specify:

1. the target file or folder
2. whether you want planning, implementation, or both
3. whether you want source code, notes, templates, or references
4. whether the update should optimize for beginner clarity, interview preparation, or production realism

Example request:

"Use `roadmap-master-reference.md` as context and expand Week 03 with expert-level planning plus source code workspace."

## Non-Negotiable Standards For Future Work

- preserve existing structure unless there is a clear upgrade path
- keep week-specific content inside week folders
- keep documentation synchronized with structural and content changes
- do not replace detailed execution guidance with generic summaries
- keep explanations beginner-readable even when the content is expert-level
- prefer official references for technical accuracy
- update time-sensitive guidance when necessary
- do not create duplicate roadmap layers unless there is a clear purpose

## Short Operating Summary

If you need the shortest possible summary of the repository:

- `AI_Guide.md` is the concise origin
- `ai-detailed-preparation-guide.md` is the long-form master roadmap
- `roadmap/` is the operational decomposed version
- this file defines the structure, standards, and current state

## Final Note

When future updates are requested, use this file as the default context anchor first, then apply changes to the specific phase, week, or reference area.
