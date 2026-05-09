from src import config
from src.answer_generator import generate_grounded_answer
from src.retrieval_backend import RetrievalBackend


class GroundedPolicyAssistant:
    def __init__(self) -> None:
        self.backend = RetrievalBackend()

    def answer(self, question: str):
        rewritten_query, retrieved_chunks = self.backend.retrieve(question, top_k=config.get_top_k())
        return generate_grounded_answer(question, rewritten_query, retrieved_chunks)
