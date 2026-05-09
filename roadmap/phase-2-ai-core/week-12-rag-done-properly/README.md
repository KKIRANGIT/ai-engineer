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

## Week 12 Outcomes

By the end of this week, you should be able to:

- describe the full RAG pipeline clearly
- justify chunk size and overlap choices
- present retrieved evidence with citations or source references
- debug why a retrieved answer failed
- separate retrieval failure from generation failure
- build one grounded document Q&A application

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
- with what instructions to the model

More context is not always better. Noisy context can harm the answer.

## 4. Citations and grounded UX

Grounding only helps if the user can see and verify the source.

You should think about:

- source snippets
- page references
- document names
- confidence and uncertainty communication

Anthropic's citations support is one example of provider-level source attribution that is useful to study.

## 5. Reranking basics

Initial retrieval can be improved by reranking candidate results.

You do not need a production reranker stack immediately, but you should understand the concept:

- first retrieve broader candidate chunks
- then improve ordering using a stronger relevance signal

## 6. Failure analysis

Every RAG miss should be categorized:

- wrong documents retrieved
- right document but wrong chunk
- right chunk but poor answer synthesis
- missing metadata filter
- poor query formulation

This discipline is what separates engineering from demo-building.

## Best Learning Sequence For This Week

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
- choose data sources

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

### Day 4: Answer generation with sources

Focus:

- grounded response instructions
- citation or reference display

### Day 5: Debug interface

Focus:

- show retrieved chunks
- show why the answer was produced

### Day 6: Failure analysis

Focus:

- collect hard queries
- categorize failures

### Day 7: Test set and refinement

Focus:

- run 20 grounded questions
- improve the system based on misses

## Build Plan

Build one document-question-answering assistant with:

- file or document upload
- chunking and storage
- retrieval
- grounded answers
- source display
- retrieval debug view

Good candidate domains:

- policy documents
- SOPs
- product documentation
- meeting archives
- research notes

## Deliverables

- one working RAG app or local prototype
- one 20-question grounded test set
- one debug view or retrieval-inspection output
- one failure-analysis note

## Exit Criteria

- you can explain every stage of your RAG pipeline
- your app can answer from provided documents rather than vague model memory
- users can see where the answer came from
- you can diagnose at least some failures by stage

## Common Mistakes To Avoid

- calling a system "RAG" when retrieval evidence is not actually exposed
- stuffing too many chunks into context
- ignoring chunk-level failure analysis
- assuming all factual failure is a model problem

## Expert Notes That Matter Early

### Grounding is not only retrieval

It is retrieval plus context design plus evidence presentation plus evaluation.

### Inspectability is part of product quality

If you cannot see what was retrieved, debugging will stay weak.

### Trust comes from source visibility

Users are more likely to trust the system when they can inspect support for claims.

## Suggested Official References

- OpenAI retrieval guide
- OpenAI file search guide
- Anthropic citations guide

## Final Standard For This Week

The correct outcome of Week 12 is not "I made chat with documents."

The correct outcome is:

"I built a grounded retrieval-backed assistant that can show its evidence, expose retrieval behavior, and be improved through failure analysis."
