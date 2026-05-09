# Week 12: RAG Done Properly

Back to [Phase 2](../README.md)

## Goal

Build a retrieval-augmented generation system that is meaningfully grounded, inspectable, and more trustworthy than a generic chat demo.

This week is where retrieval becomes an application.

## Why This Week Matters

RAG is one of the most overclaimed and underexamined areas in AI application development.

Weak RAG systems usually fail because they ignore:

- chunk quality
- metadata design
- query rewriting
- retrieval debugging
- source presentation
- grounded evaluation

The point of Week 12 is to build a system that can answer from documents and show why its answer should be trusted.

## What This Week Is Really Training

At a deeper level, this week trains six important habits.

### 1. Pipeline thinking

RAG is not one step. It is a pipeline with multiple failure boundaries.

### 2. Retrieval-generation separation

You must learn to separate:

- retrieval failure
- context-packing failure
- answer-generation failure

Without that separation, debugging becomes guesswork.

### 3. Grounded UX design

A grounded system is not just one that retrieved chunks. It is one that presents evidence in a way a user can inspect.

### 4. Query improvement judgment

User questions are not always retrieval-ready queries. This week should train you to think about normalization, rewriting, and scope refinement.

### 5. Failure categorization

Every miss should be categorized. This is the difference between a demo and a system that can improve.

### 6. Evidence-first trust building

Trust in RAG comes from source visibility, not from confident answer tone.

## Scope Boundary

This week is not for:

- production frontend polish
- long-running agent workflows
- multi-stage reranking stacks
- advanced multi-hop retrieval research patterns

This week is for:

- one local grounded Q&A application
- inspectable retrieval
- clear chunk citations
- failure analysis
- a small grounded test set

## Week 12 Outcomes

By the end of this week, you should be able to:

- describe the full RAG pipeline clearly
- justify chunk size and overlap choices
- present retrieved evidence with citations or source references
- debug why a retrieved answer failed
- separate retrieval failure from generation failure
- build one grounded document Q&A application
- inspect query rewriting, context packing, and evidence selection

## Workspace Structure

This week now includes a full hands-on workspace:

```text
week-12-rag-done-properly/
|-- README.md
|-- exercises/
|   |-- README.md
|   |-- pipeline-thinking/
|   |   `-- 01_rag_pipeline_map.py
|   |-- query-rewriting/
|   |   `-- 01_query_rewrite_patterns.py
|   |-- context-packing/
|   |   `-- 01_context_packing_tradeoffs.py
|   `-- failure-analysis/
|       `-- 01_failure_categories.py
|-- projects/
|   `-- grounded-policy-assistant/
|       |-- README.md
|       |-- .env.example
|       |-- data/
|       |   |-- evaluation_questions.json
|       |   `-- policy_documents.json
|       |-- src/
|       |   |-- __init__.py
|       |   |-- answer_generator.py
|       |   |-- chunking.py
|       |   |-- config.py
|       |   |-- context_builder.py
|       |   |-- debug_tools.py
|       |   |-- evaluation.py
|       |   |-- main.py
|       |   |-- models.py
|       |   |-- query_rewriter.py
|       |   |-- rag_pipeline.py
|       |   |-- retrieval_backend.py
|       |   `-- store.py
|       `-- tests/
|           |-- test_answer_generator.py
|           |-- test_context_builder.py
|           |-- test_query_rewriter.py
|           `-- test_rag_pipeline.py
`-- notes/
    |-- 01-week-plan.md
    |-- 02-rag-debugging-checklist.md
    `-- 03-grounded-ux-notes.md
```

## What To Learn

## 1. RAG mental model

Retrieval-augmented generation is not one step. It is at least:

1. ingest
2. chunk
3. embed
4. store
5. retrieve
6. optionally rerank
7. pack context
8. generate answer
9. present sources

Understanding these stages is more valuable than memorizing one framework abstraction.

This week’s project keeps those stages separate on purpose.

## 2. Query construction and rewriting

User questions are not always ideal search queries.

You should think about:

- normalization
- query rewriting
- whether the question should be split
- whether metadata filters should be added

This matters because retrieval often fails before generation even begins.

## 3. Context packing

Once you retrieve chunks, you still need to decide:

- how many chunks to include
- in what order
- with what metadata
- with what answer instructions

More context is not always better. Noisy context can harm the answer.

## 4. Citations and grounded UX

Grounding only helps if the user can see and verify the source.

You should think about:

- source snippets
- chunk IDs
- document titles
- confidence and uncertainty communication

Anthropic’s citations support is useful to study conceptually, but this week’s local project implements explicit chunk citations so the mechanism is visible.

## 5. Reranking basics

Initial retrieval can be improved by reranking candidate results.

This week uses a simpler ranking path, but you should still understand the concept:

- retrieve broader candidate chunks
- improve ordering using a stronger signal

That keeps you ready for later retrieval upgrades.

## 6. Failure analysis

Every RAG miss should be categorized:

- wrong documents retrieved
- right document but wrong chunk
- right chunk but poor answer synthesis
- missing metadata filter
- poor query formulation

This discipline is what separates engineering from demo-building.

## Best Learning Sequence For This Week

Use this order:

1. full RAG pipeline
2. chunking decisions
3. query rewriting
4. retrieval debugging
5. context packing
6. citations and answer UX
7. failure analysis

## Recommended Daily Breakdown

### Day 1: Pipeline architecture

Focus:

- map the full RAG flow
- inspect the local policy-document dataset

### Day 2: Ingestion and chunking

Focus:

- chunk shape
- overlap
- metadata assignment

### Day 3: Retrieval and context building

Focus:

- query execution
- candidate chunks
- context assembly

### Day 4: Grounded answer generation

Focus:

- answer instructions
- chunk citations
- uncertainty messaging

### Day 5: Debug interface

Focus:

- show rewritten query
- show retrieved chunks
- show why the answer was produced

### Day 6: Failure analysis

Focus:

- collect hard queries
- categorize failures

### Day 7: Test set and refinement

Focus:

- run the grounded evaluation set
- inspect misses by failure type

## Main Project

The main project for this week is:

- [projects/grounded-policy-assistant](projects/grounded-policy-assistant/README.md)

It is intentionally built around policy-style documents because:

- the questions benefit from retrieval
- the answers should cite sources
- users need evidence, not just fluency

The project includes:

- local document storage
- chunking
- query rewriting
- retrieval
- context packing
- grounded answer generation
- chunk-level citations
- debug output
- evaluation questions

## Build Quality Standard

For this week, "it answers from documents" is not enough.

Minimum quality bar:

- the retrieval stage is inspectable
- the answer includes source references
- the context builder is visible
- failures can be categorized
- the evaluation set is usable
- the README explains how trust is built

## Deliverables

By the end of this week, you should have:

- pipeline and failure-analysis exercises
- one grounded local RAG assistant
- one evaluation set
- one retrieval debug view
- one failure-analysis note

## Exit Criteria

You are ready to move on only if:

- you can explain every stage of your RAG pipeline
- your app answers from provided documents rather than vague model memory
- users can see where the answer came from
- you can diagnose at least some failures by stage

## Common Mistakes To Avoid

- calling a system "RAG" when retrieval evidence is not exposed
- stuffing too many chunks into context
- ignoring chunk-level failure analysis
- assuming all factual failure is a model problem
- hiding retrieval behavior behind a chat-only interface

## Expert Notes That Matter Early

### Grounding is not only retrieval

It is retrieval plus context design plus evidence presentation plus evaluation.

### Inspectability is part of product quality

If you cannot see what was retrieved, debugging will stay weak.

### Trust comes from source visibility

Users are more likely to trust the system when they can inspect support for claims.

## Suggested Official References

Prioritize these official sources:

1. OpenAI Retrieval guide  
   https://developers.openai.com/api/docs/guides/retrieval
2. OpenAI File Search guide  
   https://developers.openai.com/api/docs/guides/tools-file-search
3. Anthropic citations guide  
   https://platform.claude.com/docs/en/docs/build-with-claude/citations

Use the official docs for correctness, but use this workspace as the place where a grounded assistant becomes inspectable.

## Final Standard For This Week

The correct outcome of Week 12 is not:

"I made chat with documents."

The correct outcome is:

"I built a grounded retrieval-backed assistant that can show its evidence, expose retrieval behavior, and be improved through failure analysis."
