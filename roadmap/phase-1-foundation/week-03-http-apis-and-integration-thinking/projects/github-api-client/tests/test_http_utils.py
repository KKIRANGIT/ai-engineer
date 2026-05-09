import unittest

from github_api.http_utils import build_url, parse_link_header


class HttpUtilityTests(unittest.TestCase):
    def test_build_url_without_params(self):
        url = build_url("https://api.github.com", "/users/octocat")
        self.assertEqual(url, "https://api.github.com/users/octocat")

    def test_build_url_with_params(self):
        url = build_url(
            "https://api.github.com",
            "/users/octocat/repos",
            params={"per_page": 5, "page": 2},
        )
        self.assertIn("per_page=5", url)
        self.assertIn("page=2", url)

    def test_parse_link_header(self):
        header_value = (
            '<https://api.github.com/user/1/repos?page=2>; rel="next", '
            '<https://api.github.com/user/1/repos?page=4>; rel="last"'
        )

        parsed_links = parse_link_header(header_value)

        self.assertEqual(
            parsed_links["next"],
            "https://api.github.com/user/1/repos?page=2",
        )
        self.assertEqual(
            parsed_links["last"],
            "https://api.github.com/user/1/repos?page=4",
        )


if __name__ == "__main__":
    unittest.main()
