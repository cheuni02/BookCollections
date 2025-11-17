import unittest
from unittest import TestCase

from app import app
from app.routes.books import Book
from tests.helpers.api_helpers import APIHelpers


class TestGetBook(TestCase):
    @staticmethod
    def expected_book_details():
        return [
            {
                "id": 1,
                "title": "A Particularly Nasty Case",
                "author": "Adam Kay",
                "year_published": 2025,
                "genre": "Fiction",
            },
            200,
        ]

    @unittest.skip("skipped - only run when DB is created, seeded and app is running")
    def test_get_one_book(self):
        with app.app_context():
            test_id = 1
            resource = Book()
            response = resource.get(test_id)[0]
            response_status_code = resource.get(test_id)[1]
            self.assertEqual(response_status_code, 200)
            test_keys = self.expected_book_details()
            for key in test_keys[0]:
                self.assertEqual(response[key], test_keys[0][key])

    def test_get_one_book_with_mock(self):
        mocked_mock_details = [
            {
                "id": 1,
                "title": "A Particularly Nasty Case",
                "author": "Adam Kay",
                "year_published": 2025,
                "genre": "Fiction",
            },
            200,
        ]

        test_id = 1
        response, statusCode = APIHelpers().mockRequestToBooksAPI(
            "GET", "app.routes.books.Book.get", mocked_mock_details, BookId=test_id
        )

        self.assertEqual(statusCode, 200)
        test_keys = self.expected_book_details()
        for key in test_keys[0]:
            self.assertEqual(response[key], test_keys[0][key])
