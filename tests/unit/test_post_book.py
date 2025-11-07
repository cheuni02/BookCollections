import json
from unittest import TestCase, mock

from app import app
from app.routes.books import Books


class TestPostBook(TestCase):
    def setUp(self):
        with open("data/mocked_post_book_response.json") as f:
            self.post_book_response = json.loads(f.read())
        self.patcher = mock.patch(
            "app.routes.books.Books.post", return_value=self.post_book_response
        )
        self.mock_post = self.patcher.start()
        self.addCleanup(self.patcher.stop)

    def test_posting_one_new_book(self):
        payload = {
            "title": "The Life Impossible",
            "author": "Matt Haig",
            "year_published": 2024,
            "genre": "Fiction",
        }
        with app.test_request_context(
            "/books",
            method="POST",
            json=payload,
        ):
            resource = Books()
            response, status_code = resource.post()
            print(response)
            print(status_code)
            self.assertEqual(len(response), 6)
            self.assertEqual(status_code, 201)
            self.assertEqual(response[5]["title"], "The Life Impossible")
