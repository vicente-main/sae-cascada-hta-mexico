import unittest
from check_commit_metadata import problems

HUMAN = 'Research Author <author@example.org>'

class CommitMetadataTests(unittest.TestCase):
    def test_allows_disclosure_in_body(self):
        self.assertEqual(problems(HUMAN, HUMAN, 'Update publication\n\nPreserve the disclosure of Claude and OpenAI assistance.'), [])

    def test_rejects_tool_author_and_committer(self):
        for author, committer in [('Claude <noreply@anthropic.com>', HUMAN), (HUMAN, 'OpenAI Codex <agent@openai.com>')]:
            with self.subTest(author=author, committer=committer):
                self.assertTrue(problems(author, committer, 'Update'))

    def test_rejects_tool_trailers(self):
        for trailer in ['Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>', 'Signed-off-by: GitHub Copilot <copilot@example.org>', 'Generated with Claude']:
            with self.subTest(trailer=trailer):
                self.assertTrue(problems(HUMAN, HUMAN, 'Update\n\n' + trailer))

    def test_allows_human_coauthor(self):
        self.assertEqual(problems(HUMAN, HUMAN, 'Update\n\nCo-Authored-By: Another Researcher <researcher@example.org>'), [])

if __name__ == '__main__':
    unittest.main()
