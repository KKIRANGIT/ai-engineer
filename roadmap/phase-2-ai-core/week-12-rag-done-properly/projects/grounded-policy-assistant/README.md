# Grounded Policy Assistant

Back to [Week 12](../../README.md)

## Purpose

This project is a Week 12 local RAG lab built around policy-style documents.

It is designed to teach:

- chunk-based retrieval
- query rewriting
- context packing
- grounded answer synthesis
- source citation display
- failure inspection

The project is intentionally local and inspectable. It does not try to hide the pipeline behind a chat-only interface.

## Project Structure

```text
grounded-policy-assistant/
|-- README.md
|-- .env.example
|-- data/
|   |-- evaluation_questions.json
|   `-- policy_documents.json
|-- src/
|   |-- __init__.py
|   |-- answer_generator.py
|   |-- chunking.py
|   |-- config.py
|   |-- context_builder.py
|   |-- debug_tools.py
|   |-- evaluation.py
|   |-- main.py
|   |-- models.py
|   |-- query_rewriter.py
|   |-- rag_pipeline.py
|   |-- retrieval_backend.py
|   `-- store.py
`-- tests/
    |-- test_answer_generator.py
    |-- test_context_builder.py
    |-- test_query_rewriter.py
    `-- test_rag_pipeline.py
```

## What It Does

Given a policy question, the assistant:

1. rewrites the query for retrieval
2. retrieves the most relevant chunks
3. builds a compact evidence context
4. generates a grounded answer from those chunks
5. returns citations and a debug summary

## Example Commands

From this project folder:

### Ask one question

```powershell
python -m src.main ask --question "What should support do when a customer is charged twice?"
```

### Ask with debug information

```powershell
python -m src.main ask --question "How do we handle repeated login failures after a password reset?" --debug
```

### Run the evaluation set

```powershell
python -m src.main evaluate
```

## Output Shape

The assistant returns:

- answer text
- cited sources
- rewritten query
- retrieved chunk summary

This makes the system inspectable instead of opaque.

## Environment Variables

- `RAG_TOP_K`
- `RAG_SENTENCES_PER_CHUNK`

See [.env.example](.env.example)

## Testing

From this project folder:

```powershell
python -m unittest discover -s tests
```

## Important Learning Rule

Do not treat this project as:

"chat with documents."

Use it to answer these questions:

- What query did the system really search with?
- Which chunks were retrieved and why?
- Which chunks were included in context?
- Does the answer stay within that evidence?
- If the answer is bad, which stage caused the failure?
