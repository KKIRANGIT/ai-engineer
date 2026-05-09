"""
This exercise makes the RAG pipeline visible as a sequence of engineering
stages instead of one black-box "ask documents" step.
"""


def main():
    stages = [
        "Ingest source documents",
        "Chunk the documents into retrievable units",
        "Embed chunks into vectors",
        "Store chunks and metadata",
        "Rewrite or normalize the user query",
        "Retrieve candidate chunks",
        "Pack the best evidence into context",
        "Generate an answer from retrieved evidence",
        "Return the answer with citations and debug information",
    ]

    for index, stage in enumerate(stages, start=1):
        print(f"{index}. {stage}")


if __name__ == "__main__":
    main()
