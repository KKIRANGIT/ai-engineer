import unittest

from src.chunking import chunk_document
from src.models import Document


class ChunkingTests(unittest.TestCase):
    def test_chunk_document_creates_multiple_chunks(self) -> None:
        document = Document(
            document_id="doc_test",
            title="Chunk Test",
            category="testing",
            audience="customers",
            content="Sentence one. Sentence two. Sentence three. Sentence four.",
        )

        chunks = chunk_document(document, sentence_group_size=2)

        self.assertEqual(len(chunks), 2)
        self.assertTrue(chunks[0].text.endswith("."))


if __name__ == "__main__":
    unittest.main()
