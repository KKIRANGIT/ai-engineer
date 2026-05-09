import unittest

from src.prompt_library import get_ticket_by_id, render_prompt


class PromptLibraryTests(unittest.TestCase):
    def test_render_prompt_inserts_ticket_text(self) -> None:
        ticket = get_ticket_by_id("ticket_001")
        prompt = render_prompt("classify_ticket_v1", ticket.text)

        self.assertIn("charged twice", prompt.lower())
        self.assertIn("billing", prompt.lower())


if __name__ == "__main__":
    unittest.main()
