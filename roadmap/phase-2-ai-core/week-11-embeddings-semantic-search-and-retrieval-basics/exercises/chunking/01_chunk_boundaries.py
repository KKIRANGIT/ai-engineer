"""
This exercise shows how the same source text can be chunked in different ways,
changing what the retrieval system will later be able to return.
"""


def fixed_size_chunks(words: list[str], chunk_size: int, overlap: int) -> list[str]:
    chunks = []
    start = 0
    step = max(1, chunk_size - overlap)

    while start < len(words):
        chunk_words = words[start : start + chunk_size]
        chunks.append(" ".join(chunk_words))
        start += step

    return chunks


def main():
    text = (
        "Embeddings capture semantic relationships. Chunking controls the retrievable unit. "
        "If chunks are too large, retrieval becomes less precise. If chunks are too small, "
        "important context may be lost."
    )
    words = text.split()

    for chunk_size, overlap in [(8, 0), (8, 3), (14, 2)]:
        print(f"\nchunk_size={chunk_size}, overlap={overlap}")
        for chunk in fixed_size_chunks(words, chunk_size, overlap):
            print(f"- {chunk}")


if __name__ == "__main__":
    main()
