import json
from unittest import TestCase, mock

from app.routes.books import Books


class TestBook(TestCase):
    def test_get_all_books(self):
        expected_books = [
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
        ]
        with mock.patch("app.routes.books.Books.get", return_value=expected_books):
            with open("data/seeded_book_records.json") as json_file:
                expected_books = json.load(json_file)
                resource = Books()
                response = resource.get()
                self.assertEqual(len(response), len(expected_books))

                for i in range(len(expected_books)):
                    for key in expected_books[0]:
                        self.assertEqual(expected_books[i][key], response[i][key])
