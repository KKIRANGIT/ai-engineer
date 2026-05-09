# Week 11 Study Plan

Back to [Week 11](../README.md)

## Objective

Use this week to understand retrieval as a pipeline rather than a single vector query.

The main success condition is not:

"I did similarity search."

It is:

- I understand how chunks are created
- I understand how vectors are compared
- I understand how filters change retrieval quality
- I can compare retrieval modes and inspect failures

## Suggested Order

### Day 1

- read the Week 11 README
- complete the embedding intuition exercise
- explain cosine similarity in plain English

### Day 2

- complete the chunking exercise
- inspect how chunk size and overlap change retrievable units

### Day 3

- complete the filtering exercise
- explain why scope filters often matter as much as semantic similarity

### Day 4

- complete the search-mode exercise
- compare keyword, semantic, and hybrid tradeoffs

### Day 5

- inspect the semantic search playground project
- read the chunking, embeddings, and retrieval modules in order

### Day 6

- run several queries in keyword, semantic, and hybrid mode
- inspect the returned chunks and note where each mode succeeds or fails

### Day 7

- run the evaluation set
- read the hosted-vs-self-managed note
- write your own summary of which retrieval mode is strongest for which query type

## Minimum Success Definition

You should not leave this week saying:

"I know what embeddings are."

You should leave saying:

"I understand how chunking, embeddings, filters, ranking, and evaluation interact to determine retrieval quality."
