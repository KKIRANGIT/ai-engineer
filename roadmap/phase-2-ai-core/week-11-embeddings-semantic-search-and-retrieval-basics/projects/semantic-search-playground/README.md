# Semantic Search Playground

Back to [Week 11](../../README.md)

## Purpose

This project is a Week 11 retrieval playground built to make search mechanics visible.

It is designed to teach:

- document chunking
- local vector storage
- cosine similarity
- metadata filters
- keyword, semantic, and hybrid ranking
- retrieval evaluation

The project supports:

- deterministic mock embeddings for local learning
- optional live OpenAI embeddings

The mock path is important because the main goal of Week 11 is retrieval understanding, not paid API usage.

## Project Structure

```text
semantic-search-playground/
|-- README.md
|-- .env.example
|-- data/
|   |-- documents.json
|   `-- evaluation_queries.json
|-- src/
|   |-- __init__.py
|   |-- chunking.py
|   |-- config.py
|   |-- embeddings.py
|   |-- evaluation.py
|   |-- keyword_search.py
|   |-- main.py
|   |-- models.py
|   |-- ranking.py
|   |-- retrieval.py
|   `-- store.py
`-- tests/
    |-- test_chunking.py
    |-- test_evaluation.py
    |-- test_retrieval.py
    `-- test_similarity.py
```

## Search Modes

### Keyword

Exact-term oriented scoring.

### Semantic

Embedding-based cosine similarity.

### Hybrid

Combines keyword and semantic signals.

## Filters

The project supports filtering by:

- category
- audience

This keeps scope control visible in the retrieval flow.

## Example Commands

From this project folder:

### Inspect chunks

```powershell
python -m src.main inspect-chunks
```

### Run semantic search

```powershell
python -m src.main search --mode semantic --query "How do I get a refund for a duplicate charge?"
```

### Run hybrid search with a category filter

```powershell
python -m src.main search --mode hybrid --query "Why can't I sign in after resetting my password?" --category account_access
```

### Compare modes on one query

```powershell
python -m src.main compare --query "Can I export a CSV report of all invoices?"
```

### Run the evaluation set

```powershell
python -m src.main evaluate --mode hybrid
```

## Environment Variables

- `OPENAI_API_KEY`
- `OPENAI_EMBEDDING_MODEL`
- `EMBEDDING_MODE`

See [.env.example](.env.example)

## Testing

From this project folder:

```powershell
python -m unittest discover -s tests
```

## Important Learning Rule

Do not treat this project as:

"a mini vector database."

Use it to answer these questions:

- What unit of text am I retrieving?
- Why did this result rank above another one?
- Did the filter help or hide the right answer?
- Did keyword or semantic similarity do better for this query?
- What failures should be added to the evaluation set?
