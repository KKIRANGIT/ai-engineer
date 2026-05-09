# RAG Debugging Checklist

Back to [Week 12](../README.md)

Use this checklist whenever the grounded assistant gives a weak answer.

## Query

- Was the original user question retrieval-friendly?
- Would a rewritten query be clearer?
- Was the domain scope obvious from the wording?

## Retrieval

- Did the system retrieve the correct document family?
- Did it retrieve the correct chunk?
- Was a filter missing?

## Context Packing

- Were too many chunks included?
- Were the most relevant chunks pushed too far down?
- Did unrelated chunks add noise?

## Answer Generation

- Did the answer stay within the retrieved evidence?
- Did it overgeneralize beyond the chunks?
- Did it omit relevant evidence already present in context?

## Evidence Presentation

- Could the user actually inspect the source chunk?
- Did the citations point to the right chunk titles and IDs?

## Final Question

Is this a retrieval problem, a context problem, or a synthesis problem?
