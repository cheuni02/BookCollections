import json
from unittest import TestCase

from tests.helpers.api_helpers import APIHelpers


class TestBook(TestCase):
    def test_get_all_books(self):
        mocked_books_response = [
            [
                {
                    "id": 1,
                    "title": "A Particularly Nasty Case",
                    "author": "Adam Kay",
                    "year_published": 2025,
                    "genre": "Fiction",
                },
                {
                    "id": 2,
                    "title": "Night Swimmers",
                    "author": "Roisin Maguire",
                    "year_published": 2024,
                    "genre": "Fiction",
                },
                {
                    "id": 3,
                    "title": "Green Dot",
                    "author": "Madeleine Gray",
                    "year_published": 2024,
                    "genre": "Humour",
                },
                {
                    "id": 4,
                    "title": "The Cyclist",
                    "author": "Tim Sullivan",
                    "year_published": 2021,
                    "genre": "Crime fiction thriller",
                },
                {
                    "id": 5,
                    "title": "Onyx Storm (The Empyrean, #3)",
                    "author": "Rebecca Yarros",
                    "year_published": 2025,
                    "genre": "Fantasy",
                },
            ],
            200,
        ]

        with open("data/seeded_book_records.json") as json_file:
            expected_books_response = json.load(json_file)
            response, statusCode = APIHelpers().mockRequestToBooksAPI(
                "GET", "app.routes.books.Books.get", mocked_books_response
            )

            self.assertEqual(len(response), len(expected_books_response))
            for i in range(len(expected_books_response)):
                for key in expected_books_response[0]:
                    if key == "id":
                        continue
                    self.assertEqual(response[i][key], expected_books_response[i][key])
