# Week 11: Embeddings, Semantic Search, and Retrieval Basics

Back to [Phase 2](../README.md)

## Goal

Understand how retrieval systems surface relevant information semantically, and build the foundation required before attempting a serious RAG application.

This week is about retrieval mechanics, not yet about polished document assistants.

## Why This Week Matters

Many people say they have built RAG systems when they have really only:

- chunked text
- embedded it
- queried nearest vectors

That is not enough.

Retrieval quality depends on:

- chunk design
- metadata
- query quality
- index behavior
- filtering
- ranking
- evaluation

Week 11 gives you the underlying model needed to reason about why retrieval succeeds or fails.

## Week 11 Outcomes

By the end of this week, you should be able to:

- explain what embeddings represent at a practical level
- understand similarity search conceptually
- distinguish semantic, keyword, and hybrid search
- store and query vectors
- use metadata filters
- compare hosted retrieval with self-managed vector storage
- explain why retrieval is a pipeline problem rather than a database-brand problem

## What To Learn

## 1. Embeddings mental model

An embedding is a numeric representation of content that captures semantic relationships.

You do not need the linear algebra details this week. You do need to understand:

- similar meaning tends to map to nearby vector regions
- embeddings are useful for search, matching, clustering, and grounding workflows
- embeddings are only as useful as the surrounding retrieval design

## 2. Similarity search

Learn the intuition behind:

- nearest-neighbor retrieval
- cosine similarity and related distance measures
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

## 4. Metadata and filtering

Retrieval quality often improves when vector similarity is combined with structured filters.

Examples:

- document type
- date
- customer ID
- section name
- access scope

This matters because semantic search alone often surfaces relevant-but-wrong-scope content.

## 5. Keyword, semantic, and hybrid search

You should be able to explain:

- keyword search is strong on exact terms
- semantic search is strong on meaning
- hybrid approaches often combine the strengths of both

Expert beginner rule:

Do not assume semantic search replaces all keyword needs.

## 6. Hosted retrieval vs self-managed retrieval

Learn both:

- hosted retrieval or file-search style systems
- self-managed `pgvector` or equivalent

Hosted systems help you ship quickly.
Self-managed systems teach you the mechanics and tradeoffs.

You should understand what you gain and lose with each:

- speed vs control
- convenience vs configurability
- reduced ops vs deeper understanding

## 7. Indexes and query performance

At a practical level, understand:

- vector search performance matters as data grows
- indexes like HNSW improve search speed
- retrieval quality and query speed are related but distinct concerns

Supabase currently recommends HNSW as the general default choice for `pgvector` indexing.

## 8. Retrieval evaluation mindset

Even before Week 12, begin asking:

- did it retrieve the right document
- did it retrieve the right passage
- did filtering help or hurt
- what kinds of queries fail

This is how you avoid building retrieval systems that feel good in demos but fail under realistic questions.

## Best Learning Sequence For This Week

1. embeddings concept
2. similarity search
3. chunking
4. metadata filtering
5. hosted retrieval
6. self-managed vectors
7. evaluation mindset

## Recommended Daily Breakdown

### Day 1: Embeddings and semantic search

Focus:

- what embeddings are for
- what similarity retrieval does

### Day 2: Chunking and metadata

Focus:

- chunk boundaries
- overlap
- metadata design

### Day 3: Hosted retrieval

Focus:

- provider-managed vector stores or file search
- fast setup and search behavior

### Day 4: Self-managed retrieval

Focus:

- `pgvector`
- vector table design
- metadata columns

### Day 5: Filters and query experiments

Focus:

- narrow search by metadata
- compare query quality

### Day 6: Compare approaches

Focus:

- control vs convenience
- debugging differences

### Day 7: Document failures

Focus:

- collect failed retrieval cases
- describe why they failed

## Build Plan

Build two retrieval prototypes over the same small dataset:

### 1. Hosted retrieval version

Use:

- vector-store or file-search style provider tooling

### 2. Self-managed retrieval version

Use:

- Supabase `pgvector`
- metadata columns
- a basic vector index

Dataset size target:

- 100-500 documents or chunks

## Deliverables

- one hosted retrieval prototype
- one `pgvector` retrieval prototype
- one comparison note
- one small failure-case log

## Exit Criteria

- you can explain embeddings and semantic search clearly
- you can describe chunking tradeoffs
- you can use metadata filters intentionally
- you understand the difference between hosted and self-managed retrieval
- you can explain why retrieval quality is more than nearest-neighbor search alone

## Common Mistakes To Avoid

- thinking the vector database itself solves retrieval quality
- choosing chunk size arbitrarily
- ignoring metadata design
- evaluating retrieval only on easy, obvious queries

## Expert Notes That Matter Early

### Retrieval is a systems problem

The embed-store-query loop is only the skeleton. Real quality comes from better pipeline decisions.

### Search quality is about scope as much as similarity

The most similar chunk is not always the most useful chunk.

### Debugging retrieval should become habitual

You should be able to inspect what was retrieved and ask why.

## Suggested Official References

- OpenAI retrieval guide
- OpenAI file search guide
- Supabase vector index guidance

## Final Standard For This Week

The correct outcome of Week 11 is not "I stored vectors."

The correct outcome is:

"I understand the mechanics and tradeoffs of semantic retrieval well enough to build and inspect the foundation of a real grounding system."
