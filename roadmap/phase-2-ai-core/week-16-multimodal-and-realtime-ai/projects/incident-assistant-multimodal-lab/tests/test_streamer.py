from __future__ import annotations

import unittest

from src.streamer import stream_text


class StreamerTests(unittest.TestCase):
    def test_stream_text_splits_long_output(self) -> None:
        chunks = stream_text("a" * 200, chunk_size=50)
        self.assertEqual(len(chunks), 4)


if __name__ == "__main__":
    unittest.main()
