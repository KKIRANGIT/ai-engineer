# Retrieval Debugging Checklist

Back to [Week 11](../README.md)

Use this checklist whenever a retrieval result looks wrong.

## Chunking

- Did the relevant information get split awkwardly across chunks?
- Was the chunk too large to be precise?
- Was the chunk too small to preserve context?

## Query

- Was the query vague, under-specified, or using unusual language?
- Would keyword retrieval help for this query?
- Would synonyms or reformulation help?

## Metadata

- Did the result come from the wrong audience, product area, or scope?
- Was a filter missing?

## Ranking

- Did keyword search overweight exact terms?
- Did semantic search overweight related but unhelpful meaning?
- Would hybrid ranking be more robust?

## Evaluation

- Is this a one-off odd case or a repeated failure pattern?
- Can you add this query to your evaluation set?
