from dataclasses import dataclass, field


@dataclass
class Document:
    document_id: str
    title: str
    category: str
    audience: str
    content: str


@dataclass
class Chunk:
    chunk_id: str
    document_id: str
    title: str
    category: str
    audience: str
    text: str
    metadata: dict[str, str] = field(default_factory=dict)


@dataclass
class SearchResult:
    chunk: Chunk
    score: float
    keyword_score: float = 0.0
    semantic_score: float = 0.0
