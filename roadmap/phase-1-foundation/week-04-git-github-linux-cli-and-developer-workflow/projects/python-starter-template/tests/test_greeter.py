import os
import unittest

from app.greeter import build_greeting


class GreeterTests(unittest.TestCase):
    def test_build_greeting_uses_default_prefix(self):
        os.environ.pop("APP_GREETING_PREFIX", None)
        self.assertEqual(build_greeting("Asha"), "Hello, Asha!")

    def test_build_greeting_uses_env_prefix(self):
        os.environ["APP_GREETING_PREFIX"] = "Hi"
        self.assertEqual(build_greeting("Ravi"), "Hi, Ravi!")

    def test_build_greeting_rejects_empty_name(self):
        with self.assertRaises(ValueError):
            build_greeting("   ")


if __name__ == "__main__":
    unittest.main()
