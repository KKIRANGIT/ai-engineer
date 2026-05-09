from src.models import Chunk, Document


def chunk_document(document: Document, sentence_group_size: int = 2) -> list[Chunk]:
    sentences = [sentence.strip() for sentence in document.content.split(".") if sentence.strip()]
    chunks = []

    for index in range(0, len(sentences), sentence_group_size):
        group = sentences[index : index + sentence_group_size]
        chunk_text = ". ".join(group).strip()
        if not chunk_text.endswith("."):
            chunk_text += "."

        chunk = Chunk(
            chunk_id=f"{document.document_id}_chunk_{index // sentence_group_size + 1}",
            document_id=document.document_id,
            title=document.title,
            category=document.category,
            audience=document.audience,
            text=chunk_text,
            metadata={"category": document.category, "audience": document.audience},
        )
        chunks.append(chunk)

    return chunks


def chunk_documents(documents: list[Document]) -> list[Chunk]:
    all_chunks = []
    for document in documents:
        all_chunks.extend(chunk_document(document))
    return all_chunks
