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

### 25. Phase 3 Week 19 hands-on workspace created

Completed:

- React fundamentals exercises for components, state, forms, and effects
- support workbench React dashboard project
- helper tests for filtering, validation, stats, activity feeds, and selection logic
- notes and supporting documentation

Location:

- `roadmap/phase-3-full-stack-ai-product-engineering/week-19-react-fundamentals/`

### 26. Phase 3 Week 20 hands-on workspace created

Completed:

- Next.js App Router exercises for route structure, boundaries, route handlers, search params, and streaming
- support ops portal Next.js project with layouts, pages, dynamic routes, route handlers, and a streamed dashboard section
- helper tests for filtering, stats, route-facing data logic, and intake preview behavior
- notes and supporting documentation

Location:

- `roadmap/phase-3-full-stack-ai-product-engineering/week-20-nextjs-app-router/`

### 27. Phase 4 planning layer expanded

Completed:

- `roadmap/phase-4-build-3-real-products/README.md`
- product-track READMEs for Weeks 29 through 38

### 28. Phase 5 planning layer expanded

Completed:

- `roadmap/phase-5-career-monetization-and-positioning/README.md`
- Week 39 through Week 48 READMEs

### 29. `90-reference` expanded

Completed:

- all reference documents under `roadmap/90-reference/`

Status:

- now functions as a full companion operating handbook rather than a short appendix

### 30. Week 01 Python guide deepened further

Completed:

- `roadmap/phase-1-foundation/week-01-python-core-and-problem-solving/README.md`

Status:

- strengthened with stricter learning boundaries, no-doubt study order, stronger source strategy, and better official references

### 31. Repository entry README and course agent created

Completed:

- `README.md`
- `.agents/README.md`
- `.agents/ai-engineer-course-agent.md`

Status:

- repository now has a clear entry point and a reusable workspace-specific learning agent prompt

### 32. Workspace prompt guide created

Completed:

- `.agents/workspace-prompt-guide.md`

Status:

- repository now includes reusable prompt templates for learning, code explanation, debugging, repository updates, and documentation-sync-aware agent usage

### 33. Phase 3 Week 21 hands-on workspace created

Completed:

- auth and access-control exercises
- support ops access lab with sessions, policy helpers, and mutation checks
- tests for multi-user visibility and protected behavior
- notes and supporting documentation

Location:

- `roadmap/phase-3-full-stack-ai-product-engineering/week-21-auth-user-data-and-access-control/`

### 34. Phase 3 Week 22 hands-on workspace created

Completed:

- billing and entitlement exercises
- support ops billing lab with checkout payloads, webhook state, and plan gating
- tests for lifecycle transitions and feature access
- notes and supporting documentation

Location:

- `roadmap/phase-3-full-stack-ai-product-engineering/week-22-payments-and-billing/`

### 35. Phase 3 Week 23 hands-on workspace created

Completed:

- hierarchy, state-feedback, and onboarding exercises
- support ops polish kit with preview UI, guidance copy, and state helpers
- tests for UI messaging and state interpretation
- notes and supporting documentation

Location:

- `roadmap/phase-3-full-stack-ai-product-engineering/week-23-ui-ux-and-product-polish/`

### 36. Phase 3 Week 24 hands-on workspace created

Completed:

- durable-execution and idempotency exercises
- support ops job runner with workflow states, duplicate protection, and completion email logic
- tests for background processing behavior
- notes and supporting documentation

Location:

- `roadmap/phase-3-full-stack-ai-product-engineering/week-24-email-background-jobs-and-durable-execution/`

### 37. Phase 3 Week 25 hands-on workspace created

Completed:

- observability, analytics, and feedback-loop exercises
- support ops observability lab with event taxonomy, funnel summaries, and error grouping
- tests for product visibility helpers
- notes and supporting documentation

Location:

- `roadmap/phase-3-full-stack-ai-product-engineering/week-25-monitoring-analytics-and-feedback-loops/`

### 38. Phase 3 Week 26 hands-on workspace created

Completed:

- streaming, usage-ledger, and quota-design exercises
- support ops streaming lab with async chunks, usage summaries, quota checks, and cost estimation
- tests for streamed output and accounting behavior
- notes and supporting documentation

Location:

- `roadmap/phase-3-full-stack-ai-product-engineering/week-26-streaming-usage-tracking-and-cost-accounting/`

### 39. Phase 3 Week 27 hands-on workspace created

Completed:

- system-boundary, tenant-model, and rollout exercises
- support ops architecture kit with overview, risk, rollout, and cache documents
- tests for architecture helper logic
- notes and supporting documentation

Location:

- `roadmap/phase-3-full-stack-ai-product-engineering/week-27-saas-architecture-and-scaling-patterns/`

### 40. Phase 3 Week 28 hands-on workspace created

Completed:

- milestone brief, integration, and launch-readiness exercises
- support ops SaaS milestone blueprint with auth, billing, jobs, usage, and launch docs
- tests for milestone capability coverage
- notes and supporting documentation

Location:

- `roadmap/phase-3-full-stack-ai-product-engineering/week-28-full-stack-ai-saas-milestone/`

### 41. Phase 4 Product A hands-on workspace created

Completed:

- week-structured exercises for scope, retrieval, quality, and feedback
- policy evidence assistant project with document ingestion, metadata-aware retrieval, grounded answers, citations, query logging, and evals
- representative sample policy documents and grounded question set
- notes and supporting documentation for debugging, tester interviews, and case-study preparation

Location:

- `roadmap/phase-4-build-3-real-products/weeks-29-32-product-a-document-intelligence/`

### 42. Phase 4 Product B hands-on workspace created

Completed:

- week-structured exercises for workflow mapping, structured outputs, and ROI comparison
- lead outreach workflow copilot project with deterministic tools, structured lead briefs, review gating, audit events, and ROI helpers
- representative workflow tasks and before-vs-after notes
- notes and supporting documentation for review boundaries, ROI framing, and case-study preparation

Location:

- `roadmap/phase-4-build-3-real-products/weeks-33-35-product-b-ai-workflow-or-outreach-product/`

### 43. Phase 4 Product C hands-on workspace created

Completed:

- week-structured exercises for niche scoring, minimum-credible workflow definition, and strategic review
- IELTS writing feedback coach project with rubric-shaped scoring, structured feedback, study-plan guidance, and cost modeling
- representative student submissions plus pricing and next-step roadmap notes
- notes and supporting documentation for niche selection, validation, and strategic review

Location:

- `roadmap/phase-4-build-3-real-products/weeks-36-38-product-c-niche-product-of-your-own/`

### 44. Phase 5 Week 39 hands-on workspace created

Completed:

- positioning, project-selection, and profile-consistency exercises
- positioning workbench project with project-ranking helpers, profile-audit logic, and reusable profile templates
- sample positioning and project inventory data
- notes and supporting documentation for profile cleanup and positioning review

Location:

- `roadmap/phase-5-career-monetization-and-positioning/week-39-positioning-and-profile-cleanup/`

### 45. Phase 5 Week 40 hands-on workspace created

Completed:

- resume-framing, proposal-architecture, and project-walkthrough exercises
- career asset studio project with resume bullet, portfolio summary, and proposal helpers
- reusable asset templates for resume bullets, portfolio summaries, proposals, and walkthroughs
- notes and supporting documentation for bullet quality, case-study framing, and asset consistency

Location:

- `roadmap/phase-5-career-monetization-and-positioning/week-40-resume-portfolio-and-proposal-assets/`

### 46. Phase 5 Week 41 hands-on workspace created

Completed:

- channel-selection, message-personalization, and follow-up-rhythm exercises
- opportunity pipeline tracker project with stage summaries, personalization helpers, and weekly rhythm logic
- reusable outreach templates for LinkedIn, founder outreach, and follow-up messaging
- notes and supporting documentation for channel selection, message quality, and pipeline review

Location:

- `roadmap/phase-5-career-monetization-and-positioning/week-41-outreach-and-opportunity-pipeline/`

### 47. Phase 5 Week 42 hands-on workspace created

Completed:

- discovery-question-bank, risk-language, and statement-of-work exercises
- scoping conversation kit project with discovery questions, risk extraction, and scope-draft helpers
- reusable templates for discovery calls, AI audits, and compact statements of work
- notes and supporting documentation for scope boundaries, risk wording, and ambiguity reduction

Location:

- `roadmap/phase-5-career-monetization-and-positioning/week-42-discovery-scoping-and-technical-communication/`

### 48. Phase 5 Week 43 hands-on workspace created

Completed:

- story-compression, tradeoff-drill, and design-walkthrough exercises
- interview story lab project with intro, walkthrough, and design-outline helpers
- reusable templates for self-intros, project walkthroughs, and design answers
- notes and supporting documentation for tradeoff framing, story compression, and mock-interview review

Location:

- `roadmap/phase-5-career-monetization-and-positioning/week-43-interviews-and-system-design-preparation/`

### 49. Phase 5 Week 44 hands-on workspace created

Completed:

- launch-readiness, channel-prioritization, and launch-retrospective exercises
- launch readiness console project with readiness scoring, channel ranking, and activation metrics
- reusable templates for launch checklists, channel plans, and launch retrospectives
- notes and supporting documentation for distribution fit, readiness audits, and signal review

Location:

- `roadmap/phase-5-career-monetization-and-positioning/week-44-product-launch-and-distribution/`

### 50. Phase 5 Week 45 hands-on workspace created

Completed:

- proof-theme-selection, post-structure, and repurposing exercises
- proof content studio project with theme planning, proof checks, and repurposing helpers
- reusable templates for build logs, architecture posts, and lesson-oriented content
- notes and supporting documentation for content quality, proof distribution, and repurposing discipline

Location:

- `roadmap/phase-5-career-monetization-and-positioning/week-45-content-and-proof-distribution/`

### 51. Phase 5 Week 46 hands-on workspace created

Completed:

- workflow-audit, checklist-design, and template-reuse exercises
- delivery leverage kit project with workflow summaries, reuse ranking, and checklist helpers
- reusable templates for kickoff, QA, and handoff assets
- notes and supporting documentation for process clarity, leverage boundaries, and repeated-work review

Location:

- `roadmap/phase-5-career-monetization-and-positioning/week-46-delivery-process-and-leverage/`

### 52. Phase 5 Week 47 hands-on workspace created

Completed:

- opportunity-filters, boundary-language, and negotiation-scenario exercises
- opportunity selection desk project with fit scoring, pricing logic, and bad-fit flag helpers
- reusable templates for scope clarification, negotiation structure, and boundary language
- notes and supporting documentation for selection quality, rate logic, and opportunity filters

Location:

- `roadmap/phase-5-career-monetization-and-positioning/week-47-rate-raising-negotiation-and-selection/`

### 53. Phase 5 Week 48 hands-on workspace created

Completed:

- year-review, path-selection, and quarter-priority exercises
- next-year planning workbench project with yearly review, path selection, and quarter-plan helpers
- reusable templates for yearly review, path-decision memos, and quarter planning
- notes and supporting documentation for strategic review, path clarity, and next-year planning

Location:

- `roadmap/phase-5-career-monetization-and-positioning/week-48-final-review-and-next-12-month-plan/`

## Current Completion State

At this point:

- all major phase planning layers are expanded
- all overview and reference layers are expanded
- Week 01, Week 02, Week 03, Week 04, Week 05, Week 06, Week 07, Week 08, Week 09, Week 10, Week 11, Week 12, Week 13, Week 14, Week 15, Week 16, Week 17, Week 18, Week 19, Week 20, Week 21, Week 22, Week 23, Week 24, Week 25, Week 26, Week 27, and Week 28 have both planning and implementation artifacts
- Phase 4 Product A now has both planning and implementation artifacts
- Phase 4 Product B now has both planning and implementation artifacts
- Phase 4 Product C now has both planning and implementation artifacts
- Phase 5 Week 39, Week 40, Week 41, Week 42, Week 43, Week 44, Week 45, Week 46, Week 47, and Week 48 now have both planning and implementation artifacts

This means the roadmap now has full hands-on implementation coverage across all five phases.

## What Future Updates Should Usually Focus On

The highest-value next steps usually fall into one of these categories:

### 1. Add study-operating assets

Examples:

- progress tracker
- cross-phase review templates
- project case-study templates

### 2. Improve top-level navigation

Examples:

- keep `roadmap/README.md` synchronized with all expanded sections
- improve cross-linking between phases and references

### 3. Continue source-hardening

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
