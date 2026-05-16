# Phase 2: AI Core

Back to [Roadmap Index](../README.md)

## Goal

Learn how modern AI applications are actually built, not how AI demos are marketed.

Phase 2 is where the roadmap stops being "software engineering with AI curiosity" and becomes "AI application engineering with product and systems discipline." The purpose of this phase is to build real fluency in the core building blocks of useful LLM-powered systems:

- model APIs
- prompt and instruction design
- structured outputs
- embeddings and retrieval
- grounding and citations
- tool use
- workflow orchestration
- evals
- multimodal and realtime patterns
- safety, observability, and cost control

## Why This Phase Matters

Many learners jump into AI development by copying a chatbot template and swapping in an API key. That path creates weak understanding.

This phase is designed to correct that by forcing you to understand:

- what the model is doing
- what the application is doing
- where the failure boundaries are
- how to measure whether the system is actually good

The difference between a weak AI app and a strong AI app usually does not come from one "secret prompt." It comes from stronger systems thinking across context design, tool boundaries, retrieval quality, structured outputs, evaluation, and user experience.

## What This Phase Should Produce

By the end of Phase 2, you should be able to:

- call major provider APIs directly and understand their current primitives
- compare model families and choose them intentionally
- design prompts around measurable goals
- generate structured outputs that can safely drive application logic
- build and debug retrieval-based systems
- connect tools to models safely
- reason clearly about workflows vs agents
- evaluate model behavior instead of relying on demo vibes
- build at least one serious AI application with evidence of grounding and reliability

## The Execution Model For Phase 2

Treat this phase as a sequence of layers, not a list of unrelated topics.

### Layer 1: Direct provider fluency

Weeks 09-10 build fluency with the core provider interfaces and prompt behavior.

You should exit this layer understanding:

- how to talk to models directly
- how instructions shape behavior
- how to get useful, controlled output

### Layer 2: Grounding and retrieval

Weeks 11-12 teach how to connect models to external knowledge.

You should exit this layer understanding:

- embeddings
- vector search
- retrieval pipelines
- chunking
- citations
- why many RAG systems fail

### Layer 3: Action and orchestration

Weeks 13-14 teach how models can interact with tools and multi-step workflows.

You should exit this layer understanding:

- function or tool calling
- tool-result loops
- workflow boundaries
- when agents are useful
- when they are unnecessary complexity

### Layer 4: Measurement and specialization

Week 15 teaches you to optimize systems with evidence instead of intuition.

You should exit this layer understanding:

- eval sets
- grading and regression testing
- when prompt engineering is enough
- when retrieval is enough
- when fine-tuning is justified

### Layer 5: Multimodal and production reality

Weeks 16-17 take you beyond text-only systems and into the realities of production usage:

- audio
- vision
- realtime interfaces
- safety
- observability
- latency
- cost

### Layer 6: AI product proof

Week 18 converts all of the above into one serious product artifact.

## Current Technical Direction This Phase Assumes

This phase is aligned to current official platform guidance as of May 9, 2026.

Key assumptions:

- OpenAI: Responses API is the default path for new projects, with structured outputs, hosted tools, and retrieval primitives available directly in the platform.
- Anthropic: Messages API and modern tool-use patterns are core for Claude-based applications.
- Retrieval: learn both hosted retrieval and self-managed vector workflows such as `pgvector`.
- Tool use: treat tool calling as a first-class application capability, not as a novelty.
- Realtime and multimodal: voice, image, and low-latency interaction are now practical application skills, not niche extras.
- Evals: optimization should start with measurable criteria and representative test cases.

## Recommended Learning Attitude For This Phase

Be careful about three traps:

### Trap 1: confusing prompt tricks with system design

Prompt quality matters, but it is only one layer of the system.

### Trap 2: building "agent" systems before understanding simpler loops

Many tasks are better solved with:

- direct API calls
- explicit tool loops
- retrieval plus structured outputs

before introducing agent frameworks.

### Trap 3: assuming a plausible answer means a good system

Plausibility is not quality. This phase should train you to ask:

- was it grounded
- was it correct
- was it useful
- was it cost-effective
- can I reproduce the result reliably

## Phase Success Criteria

You should consider Phase 2 successful only if most of these are true:

- you can call frontier model APIs directly without heavy wrapper dependence
- you can choose between plain generation, structured outputs, retrieval, and tools intentionally
- you can explain the difference between semantic search, RAG, and tool-calling systems
- you can run a basic eval loop and compare system changes
- you can discuss failure modes honestly
- you can ship one meaningful AI-powered application that is more than a toy chatbot

## Current Workspace Status

The Phase 2 planning layer is fully expanded.

Current status:

- Week 09 includes exercises, a provider-aware API playground, tests, and notes
- Week 10 includes prompt exercises, a structured-output project, tests, and notes
- Week 11 includes embeddings exercises, a semantic search playground, tests, and notes
- Week 12 includes RAG pipeline exercises, a grounded policy assistant, tests, and notes
- Week 13 includes tool-loop exercises, a local operations assistant lab, tests, and notes
- Week 14 includes orchestration exercises, a research brief orchestrator, tests, and notes
- Week 15 includes eval-design exercises, a ticket triage eval lab, tests, and notes
- Week 16 includes multimodal exercises, an incident assistant multimodal lab, tests, and notes
- Week 17 includes safety exercises, a guarded support assistant lab, tests, and notes
- Week 18 includes capstone exercises, a support ops copilot milestone project, tests, and notes

This means Phase 2 is now fully backed by hands-on implementation workspaces from Week 09 through Week 18.

## How To Use The Weekly Modules

Each weekly folder in this phase should be treated as an execution module.

Read each week in this order:

1. Goal
2. Why the week matters
3. Weekly outcomes
4. What to learn
5. Recommended daily breakdown
6. Build plan
7. Deliverables
8. Exit criteria

Do not advance just because the concepts sound familiar. Advance when you have a working artifact and you can explain the tradeoffs.

## Weeks

- [Week 09: LLM Fundamentals and API Literacy](week-09-llm-fundamentals-and-api-literacy/README.md)
- [Week 10: Prompt Engineering and Structured Outputs](week-10-prompt-engineering-and-structured-outputs/README.md)
- [Week 11: Embeddings, Semantic Search, and Retrieval Basics](week-11-embeddings-semantic-search-and-retrieval-basics/README.md)
- [Week 12: RAG Done Properly](week-12-rag-done-properly/README.md)
- [Week 13: Tool Use and Function Calling](week-13-tool-use-and-function-calling/README.md)
- [Week 14: Agents and Workflow Orchestration](week-14-agents-and-workflow-orchestration/README.md)
- [Week 15: Evals, Prompt Optimization, and Fine-Tuning Decisions](week-15-evals-prompt-optimization-and-fine-tuning-decisions/README.md)
- [Week 16: Multimodal and Realtime AI](week-16-multimodal-and-realtime-ai/README.md)
- [Week 17: Safety, Observability, and Cost Control](week-17-safety-observability-and-cost-control/README.md)
- [Week 18: AI Milestone Product](week-18-ai-milestone-product/README.md)
