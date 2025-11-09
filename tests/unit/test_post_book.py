import json
from unittest import TestCase, mock

from app import app
from app.routes.books import Books


class TestPostBook(TestCase):
    def setUp(self):
        with open("data/mocked_post_book_response.json") as f1:
            self.post_book_response = json.loads(f1.read())
        with open("data/mocked_posting_book_with_same_details_response.json") as f2:
            self.posting_book_with_same_details_response = json.loads(f2.read())

    def test_posting_one_new_book(self):
        with mock.patch(
            "app.routes.books.Books.post", return_value=self.post_book_response
        ):
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
                self.assertEqual(len(response), 6)
                self.assertEqual(status_code, 201)
                self.assertEqual(response[5]["title"], "The Life Impossible")

    def test_posting_same_book_errors_due_to_SQL_UNIQUE_constraint_failed(self):
        with mock.patch(
            "app.routes.books.Books.post",
            return_value=self.posting_book_with_same_details_response,
        ):
            payload = {
                "title": "Onyx Storm (The Empyrean, #3)",
                "author": "Rebecca Yarros",
                "year_published": 2025,
                "genre": "Fantasy",
            }
            with app.test_request_context(
                "/books",
                method="POST",
                json=payload,
            ):
                resource = Books()
                response, status_code = resource.post()
                self.assertEqual(response["error"], "Conflict")
                self.assertEqual(
                    response["message"], "Book already exists. Cannot create this book."
                )
                self.assertEqual(status_code, 409)
