import unittest
import requests
import json
import HtmlTestRunner

class TestJSONPlaceholderAPI(unittest.TestCase):
    def test_response_status_200(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        self.assertEqual(response.status_code, 200)

    def test_match_response(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        posts = json.loads(response.text)
        for post in posts:
            self.assertIsInstance(post["id"], int)
            self.assertIsInstance(post["title"], str)
            self.assertIsInstance(post["body"], str)
            self.assertIsNotNone(post["userId"])

if __name__ == "__main__":
    # Jalankan test case dan hasilkan laporan dalam bentuk HTML
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_report'))
