from dataclasses import dataclass, field


@dataclass
class PolicyDocument:
    document_id: str
    title: str
    section: str
    content: str


@dataclass
class PolicyChunk:
    chunk_id: str
    document_id: str
    title: str
    section: str
    text: str


@dataclass
class RetrievedChunk:
    chunk: PolicyChunk
    score: float


@dataclass
class GroundedAnswer:
    answer_text: str
    citations: list[dict] = field(default_factory=list)
    rewritten_query: str = ""
    retrieved_chunks: list[dict] = field(default_factory=list)
