import json
from unittest import TestCase

from tests.helpers.api_helpers import APIHelpers


class TestPostBook(TestCase):
    def setUp(self):
        with open("data/mocked_post_book_response.json") as f1:
            self.postBookResponse = json.loads(f1.read())
        with open("data/mocked_posting_book_with_same_details_response.json") as f2:
            self.postingBookWithSameDetailsResponse = json.loads(f2.read())

    def testCreateNewBook(self):
        payload = {
            "title": "The Life Impossible",
            "author": "Matt Haig",
            "year_published": 2024,
            "genre": "Fiction",
        }
        self.apiHelper = APIHelpers()
        response, statusCode = self.apiHelper.mockRequestToBooksAPI(
            "POST", "app.routes.books.Books.post", self.postBookResponse, payload
        )
        self.assertEqual(len(response), 6)
        self.assertEqual(statusCode, 201)
        self.assertEqual(response[5]["title"], "The Life Impossible")

    def testConflictWhenAttemptingToCreateAlreadyExistingBook(self):
        payload = {
            "title": "Onyx Storm (The Empyrean, #3)",
            "author": "Rebecca Yarros",
            "year_published": 2025,
            "genre": "Fantasy",
        }
        self.apiHelper = APIHelpers()
        response, statusCode = self.apiHelper.mockRequestToBooksAPI(
            "POST",
            "app.routes.books.Books.post",
            self.postingBookWithSameDetailsResponse,
            payload,
        )
        print(response)
        self.assertEqual(len(response), 2)
        self.assertEqual(statusCode, 409)
        self.assertEqual(response["error"], "Conflict")
        self.assertEqual(
            response["message"], "Book already exists. Cannot create this book."
        )
        self.assertEqual(statusCode, 409)
