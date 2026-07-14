import importlib.util
import pathlib
import subprocess
import sys
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


def load_minify_module():
    spec = importlib.util.spec_from_file_location("minify", ROOT / "minify.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class MinifyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.minify = load_minify_module()

    def test_css_is_minified_and_url_is_preserved(self):
        html = """
        <style>
          /* remove me */
          .hero {
            background-image: url("https://example.com/avatar.jpeg");
            color: #fff;
          }
        </style>
        """

        result = self.minify.minify_html(html)

        self.assertNotIn("remove me", result)
        self.assertIn('url("https://example.com/avatar.jpeg")', result)
        self.assertIn(".hero{", result)
        self.assertIn("color:#fff;", result)

    def test_js_comments_are_removed_without_breaking_urls(self):
        html = """
        <script>
          const url = "https://github.com/isamulenko";
          // remove this comment
          const label = "portfolio";
        </script>
        """

        result = self.minify.minify_html(html)

        self.assertIn('"https://github.com/isamulenko"', result)
        self.assertIn('const label = "portfolio";', result)
        self.assertNotIn("remove this comment", result)

    def test_text_content_spacing_is_preserved(self):
        html = """
        <main>
          <p>Staff Frontend Engineer   building polished product systems.</p>
          <span>Selected</span>
          <span>Work</span>
        </main>
        """

        result = self.minify.minify_html(html)

        self.assertIn(
            "Staff Frontend Engineer   building polished product systems.",
            result,
        )
        self.assertIn("</span><span>", result)

    def test_cli_writes_requested_output_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = pathlib.Path(temp_dir)
            source = temp / "index.html"
            output = temp / "s3" / "index.html"
            source.write_text(
                "<html>\n<body>\n<!-- drop -->\n<p>Hello world</p>\n</body>\n</html>",
                encoding="utf-8",
            )

            completed = subprocess.run(
                [sys.executable, str(ROOT / "minify.py"), str(source), str(output)],
                check=True,
                capture_output=True,
                text=True,
            )

            self.assertIn("Minified:", completed.stdout)
            self.assertTrue(output.exists())
            self.assertNotIn("drop", output.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
