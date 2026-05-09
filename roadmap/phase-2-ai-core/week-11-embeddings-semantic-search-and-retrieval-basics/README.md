# Week 11: Embeddings, Semantic Search, and Retrieval Basics

Back to [Phase 2](../README.md)

## Goal

Understand how retrieval systems surface relevant information semantically, and build the foundation required before attempting a serious RAG application.

This week is about retrieval mechanics, not yet about polished document assistants.

## Why This Week Matters

Many people say they have built retrieval systems when they have really only:

- chunked text
- embedded it
- queried nearest vectors

That is not enough.

Retrieval quality depends on:

- chunk design
- metadata
- query quality
- search mode
- filtering
- ranking
- evaluation

Week 11 gives you the underlying model needed to reason about why retrieval succeeds or fails before you move into full grounding systems.

## What This Week Is Really Training

At a deeper level, this week trains six important habits.

### 1. Embeddings as application primitives

You should stop thinking of embeddings as abstract model outputs and start thinking of them as reusable search primitives for:

- semantic search
- matching
- clustering
- recommendation
- grounding pipelines

### 2. Search comparison thinking

You should become able to compare:

- keyword retrieval
- semantic retrieval
- hybrid retrieval

without assuming one automatically replaces the others.

### 3. Chunking judgment

Chunking is one of the most important retrieval decisions. This week should train you to ask:

- what unit of meaning am I embedding?
- what context should stay together?
- where do boundaries help or hurt?

### 4. Scope control through metadata

The "most similar" result is often not the most useful result. Metadata and filters often determine whether retrieval is actually in the right scope.

### 5. Retrieval debugging

You should start building the habit of inspecting:

- what was retrieved
- what was missed
- whether the failure came from chunking, embeddings, filters, or ranking

### 6. Evaluation mindset

This week should push you toward:

- known query sets
- expected results
- failure-case logs

That makes Week 12 much stronger.

## Scope Boundary

This week is not for:

- full RAG answer synthesis
- citation formatting
- complex reranking stacks
- production vector databases
- long-document agent workflows

This week is for:

- embeddings intuition
- chunking
- semantic search
- metadata filters
- hybrid search
- retrieval evaluation

## Week 11 Outcomes

By the end of this week, you should be able to:

- explain what embeddings represent at a practical level
- explain similarity search conceptually
- distinguish semantic, keyword, and hybrid search
- chunk documents intentionally
- store vectors and query them in a simple local system
- use metadata filters deliberately
- compare hosted retrieval with self-managed retrieval conceptually
- explain why retrieval quality is a pipeline problem rather than a database-brand problem

## Workspace Structure

This week now includes a full hands-on workspace:

```text
week-11-embeddings-semantic-search-and-retrieval-basics/
|-- README.md
|-- exercises/
|   |-- README.md
|   |-- embedding-intuition/
|   |   `-- 01_similarity_space.py
|   |-- chunking/
|   |   `-- 01_chunk_boundaries.py
|   |-- filtering-and-ranking/
|   |   `-- 01_metadata_filters.py
|   `-- search-modes/
|       `-- 01_keyword_semantic_hybrid.py
|-- projects/
|   `-- semantic-search-playground/
|       |-- README.md
|       |-- .env.example
|       |-- data/
|       |   |-- documents.json
|       |   `-- evaluation_queries.json
|       |-- src/
|       |   |-- __init__.py
|       |   |-- chunking.py
|       |   |-- config.py
|       |   |-- embeddings.py
|       |   |-- evaluation.py
|       |   |-- keyword_search.py
|       |   |-- main.py
|       |   |-- models.py
|       |   |-- ranking.py
|       |   |-- retrieval.py
|       |   `-- store.py
|       `-- tests/
|           |-- test_chunking.py
|           |-- test_evaluation.py
|           |-- test_retrieval.py
|           `-- test_similarity.py
`-- notes/
    |-- 01-week-plan.md
    |-- 02-retrieval-debugging-checklist.md
    `-- 03-hosted-vs-self-managed-notes.md
```

## What To Learn

## 1. Embeddings mental model

An embedding is a numeric representation of content that captures semantic relationships.

You do not need the linear algebra details this week. You do need to understand:

- similar meaning tends to map to nearby vector regions
- embeddings are useful for search, matching, clustering, and grounding workflows
- embeddings are only as useful as the surrounding retrieval design

The project includes both mock embeddings and an optional live embeddings path so you can inspect the mechanics without depending on external setup.

## 2. Similarity search

Learn the intuition behind:

- nearest-neighbor retrieval
- cosine similarity
- why semantically similar text can be found without exact keyword overlap

Important note:

Semantic retrieval is powerful, but not magical. It can still miss critical terms, exact identifiers, or domain-specific distinctions.

## 3. Chunking basics

Chunking is one of the most important design choices in retrieval.

You should think about:

- chunk size
- overlap
- semantic coherence
- whether chunks align with source structure

Too-small chunks lose context.
Too-large chunks reduce precision.

This week’s project makes chunking visible instead of burying it inside a managed pipeline.

## 4. Metadata and filtering

Retrieval quality often improves when vector similarity is combined with structured filters.

Examples:

- category
- audience
- product area
- recency
- access scope

This matters because semantic search alone often surfaces relevant-but-wrong-scope content.

## 5. Keyword, semantic, and hybrid search

You should be able to explain:

- keyword search is strong on exact terms
- semantic search is strong on meaning
- hybrid approaches often combine the strengths of both

Expert beginner rule:

Do not assume semantic search replaces all keyword needs.

This week’s lab lets you run the same query through all three modes so the tradeoffs are concrete.

## 6. Hosted retrieval vs self-managed retrieval

Learn both concepts:

- hosted retrieval or file-search style systems
- self-managed vector workflows such as `pgvector`

Hosted systems help you ship quickly.
Self-managed systems teach you the mechanics and tradeoffs.

You should understand what you gain and lose with each:

- speed vs control
- convenience vs configurability
- reduced ops vs deeper understanding

## 7. Indexes and query performance

At a practical level, understand:

- vector search performance matters as data grows
- approximate nearest-neighbor indexes matter at scale
- retrieval quality and query speed are related but distinct concerns

Supabase currently recommends HNSW as the general default choice for `pgvector` indexing. This week does not require you to run `pgvector`, but it does require you to understand why indexing decisions matter.

## 8. Retrieval evaluation mindset

Even before Week 12, begin asking:

- did it retrieve the right document?
- did it retrieve the right chunk?
- did filtering help or hurt?
- which query types fail?

This is how you avoid retrieval systems that feel good in demos but fail under realistic questions.

## Best Learning Sequence For This Week

Use this order:

1. embeddings concept
2. similarity search
3. chunking
4. metadata filtering
5. keyword vs semantic vs hybrid comparison
6. evaluation mindset
7. hosted vs self-managed tradeoffs

## Recommended Daily Breakdown

### Day 1: Embeddings and semantic similarity

Focus:

- what embeddings are for
- what similarity retrieval does

### Day 2: Chunking and metadata

Focus:

- chunk boundaries
- overlap
- metadata design

### Day 3: Keyword vs semantic retrieval

Focus:

- exact match behavior
- semantic match behavior
- where each one fails

### Day 4: Hybrid search and filters

Focus:

- combine ranking signals
- narrow retrieval by scope

### Day 5: Local retrieval pipeline

Focus:

- build chunks
- embed them
- store vectors
- query the store

### Day 6: Evaluation and failure analysis

Focus:

- compare query outcomes
- inspect misses
- document failure reasons

### Day 7: Hosted vs self-managed comparison

Focus:

- convenience vs control
- what you would choose for a real product

## Main Project

The main project for this week is:

- [projects/semantic-search-playground](projects/semantic-search-playground/README.md)

It is intentionally designed to make retrieval mechanics visible.

The project includes:

- document chunking
- a mock embedding model
- optional live OpenAI embeddings
- local vector storage
- cosine similarity search
- keyword search
- hybrid ranking
- metadata filtering
- regression-style evaluation

This keeps the week practical without hiding the logic behind hosted tooling too early.

## Build Quality Standard

For this week, "I stored vectors" is not enough.

Minimum quality bar:

- chunking logic is explicit
- similarity is visible
- metadata filters are usable
- keyword, semantic, and hybrid modes can be compared
- a small evaluation set exists
- the README explains the tradeoffs clearly

## Deliverables

By the end of this week, you should have:

- embeddings and chunking exercises
- one semantic search playground
- keyword, semantic, and hybrid retrieval comparisons
- an evaluation query set
- notes on retrieval failures and tradeoffs

## Exit Criteria

You are ready to move on only if:

- you can explain embeddings and semantic search clearly
- you can describe chunking tradeoffs
- you can use metadata filters intentionally
- you can explain the difference between keyword, semantic, and hybrid retrieval
- you can explain why retrieval quality is more than nearest-neighbor search alone

## Common Mistakes To Avoid

- thinking the vector database itself solves retrieval quality
- choosing chunk size arbitrarily
- ignoring metadata design
- evaluating retrieval only on easy queries
- assuming semantic similarity is always the same as task usefulness

## Expert Notes That Matter Early

### Retrieval is a systems problem

The embed-store-query loop is only the skeleton. Real quality comes from better pipeline decisions.

### Search quality is about scope as much as similarity

The most similar chunk is not always the most useful chunk.

### Debugging retrieval should become habitual

You should be able to inspect what was retrieved and ask why.

## Suggested Official References

Prioritize these official sources:

1. OpenAI Retrieval guide  
   https://platform.openai.com/docs/guides/retrieval
2. OpenAI File Search guide  
   https://platform.openai.com/docs/guides/tools-file-search
3. Supabase `pgvector` guide  
   https://supabase.com/docs/guides/database/extensions/pgvector
4. Supabase vector indexes overview  
   https://supabase.com/docs/guides/ai/vector-indexes
5. Supabase HNSW indexes  
   https://supabase.com/docs/guides/ai/vector-indexes/hnsw-indexes

Use the official docs for correctness, but use this workspace as the place where retrieval mechanics become understandable.

## Final Standard For This Week

The correct outcome of Week 11 is not:

"I stored vectors."

The correct outcome is:

"I understand the mechanics and tradeoffs of chunking, embeddings, search modes, filtering, and evaluation well enough to build and inspect the retrieval foundation of a real grounding system."
