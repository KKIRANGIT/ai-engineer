# Policy Evidence Assistant

This project is a narrow document-intelligence product for internal policy and operations questions.

## What It Demonstrates

- document ingestion from a controlled markdown corpus
- frontmatter metadata parsing
- chunking by policy sections
- metadata-aware retrieval
- grounded answers with citations
- query logging and a simple eval set

## Files

- `data/documents/`: representative policy documents
- `data/evals/questions.json`: grounded evaluation questions
- `src/load-documents.js`: parse the corpus and metadata
- `src/chunk-documents.js`: build retrievable chunks
- `src/retrieve.js`: keyword and metadata-aware retrieval logic
- `src/answer.js`: grounded answer assembly with citations
- `src/evals.js`: eval runner
- `src/query-log.js`: query log entry creation
- `docs/product-brief.md`: product framing and user workflow
- `docs/feedback-notes-template.md`: feedback capture format
- `docs/case-study-notes.md`: portfolio and demo framing
- `tests/assistant.test.mjs`: ingestion, retrieval, grounding, and eval tests

## Suggested Study Order

1. read the product brief
2. inspect the sample documents
3. read the loader and chunking code
4. read the retrieval and answer logic
5. run the tests
6. extend the eval set with one failure-focused question
