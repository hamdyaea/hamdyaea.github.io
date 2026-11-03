# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
from html.parser import HTMLParser
from pathlib import Path
import unittest


class Tags(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.tags = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


class PageTests(unittest.TestCase):
    def test_icon_links_have_names_and_isolation(self):
        page = Tags(Path("index.html").read_text())
        links = [attrs for tag, attrs in page.tags if tag == "a"]
        self.assertEqual(len(links), 4)
        for attrs in links:
            self.assertTrue(attrs.get("aria-label"))
            self.assertIn("noopener", attrs.get("rel", "").split())
            self.assertIn("noreferrer", attrs.get("rel", "").split())

    def test_images_have_alternatives(self):
        for tag, attrs in Tags(Path("index.html").read_text()).tags:
            if tag == "img":
                self.assertTrue(attrs.get("alt"))


if __name__ == "__main__":
    unittest.main()
