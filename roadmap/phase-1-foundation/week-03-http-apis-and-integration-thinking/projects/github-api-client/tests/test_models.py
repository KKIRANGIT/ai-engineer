import json
import unittest
from pathlib import Path

from github_api.models import RepoSummary, UserProfile


class ModelParsingTests(unittest.TestCase):
    def setUp(self):
        self.data_folder = Path(__file__).resolve().parent.parent / "data"

    def test_user_profile_from_sample_json(self):
        sample_path = self.data_folder / "sample_user_response.json"
        sample_data = json.loads(sample_path.read_text(encoding="utf-8"))

        user_profile = UserProfile.from_api_response(sample_data)

        self.assertEqual(user_profile.login, "octocat")
        self.assertEqual(user_profile.public_repos, 8)
        self.assertEqual(user_profile.profile_url, "https://github.com/octocat")

    def test_repo_summary_from_sample_json(self):
        sample_path = self.data_folder / "sample_repo_response.json"
        sample_data = json.loads(sample_path.read_text(encoding="utf-8"))

        repo_summary = RepoSummary.from_api_response(sample_data[0])

        self.assertEqual(repo_summary.name, "Spoon-Knife")
        self.assertEqual(repo_summary.language, "HTML")
        self.assertEqual(repo_summary.stars, 13000)


if __name__ == "__main__":
    unittest.main()
