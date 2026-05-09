from src import config
from src.models import PolicyChunk, PolicyDocument


def chunk_document(document: PolicyDocument) -> list[PolicyChunk]:
    sentence_group_size = config.get_sentences_per_chunk()
    sentences = [sentence.strip() for sentence in document.content.split(".") if sentence.strip()]
    chunks = []

    for index in range(0, len(sentences), sentence_group_size):
        group = sentences[index : index + sentence_group_size]
        chunk_text = ". ".join(group).strip()
        if not chunk_text.endswith("."):
            chunk_text += "."

        chunk = PolicyChunk(
            chunk_id=f"{document.document_id}_chunk_{index // sentence_group_size + 1}",
            document_id=document.document_id,
            title=document.title,
            section=document.section,
            text=chunk_text,
        )
        chunks.append(chunk)

    return chunks


def chunk_documents(documents: list[PolicyDocument]) -> list[PolicyChunk]:
    all_chunks = []
    for document in documents:
        all_chunks.extend(chunk_document(document))
    return all_chunks
