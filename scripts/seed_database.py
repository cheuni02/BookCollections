import sys
import time
from importlib import resources

import pandas as pd
import sqlalchemy

from app import BookModel, app, db


class BookDBSeeder:
    seeded_records = [
        {
            "title": "A Particularly Nasty Case",
            "author": "Adam Kay",
            "year_published": 2025,
            "genre": "Fiction",
        },
        {
            "title": "Night Swimmers",
            "author": "Roisin Maguire",
            "year_published": 2024,
            "genre": "Fiction",
        },
        {
            "title": "Green Dot",
            "author": "Madeleine Gray",
            "year_published": 2024,
            "genre": "Humour",
        },
        {
            "title": "The Cyclist",
            "author": "Tim Sullivan",
            "year_published": 2021,
            "genre": "Crime fiction thriller",
        },
        {
            "title": "Onyx Storm (The Empyrean, #3)",
            "author": "Rebecca Yarros",
            "year_published": 2025,
            "genre": "Fantasy",
        },
    ]

    def seed_db_from_json(self):
        with app.app_context():
            for record in self.seeded_records:
                print(record["title"])
                book = BookModel(
                    title=record["title"],
                    author=record["author"],
                    year_published=record["year_published"],
                    genre=record["genre"],
                )
                db.session.add(book)
            db.session.commit()

    def seed_db_from_csv(self, filename):
        with app.app_context():
            with resources.files("data").joinpath(filename).open() as f:
                df = pd.read_csv(f)
                print(df.to_string())

                for index, row in df.iterrows():
                    book = BookModel(
                        title=row["title"],
                        author=row["author"],
                        year_published=row["year_published"],
                        genre=row["genre"],
                    )
                    db.session.add(book)
                db.session.commit()


if __name__ == "__main__":
    print("Seeding database with some book data ...")
    time.sleep(1)
    filename = "seeded_book_records.csv"
    while True:
        choice = int(
            input(
                "Choose from the following:\n"
                "1. Seed from JSON file\n"
                "2. Seed from CSV file\n"
            )
        )
        try:
            match (choice):
                case 1:
                    print("you chose to seed with JSON file\n")
                    BookDBSeeder().seed_db_from_json()
                    break
                case 2:
                    print("you chose to seed with CSV file\n")
                    print(f"will read from this file: {filename}\n")
                    BookDBSeeder().seed_db_from_csv(filename)
                    break
                case _:
                    print("you must choose either 1 or 2, try again ...\n")
        except sqlalchemy.exc.IntegrityError as e:
            print(
                f"Error in seeding - has the database already been seeded?\n"
                f"See stacktrace below:\n{e}"
            )
        except Exception:
            print("Unexpected error:", sys.exc_info()[0])
