import json
import sys
import time
from importlib import resources

import pandas as pd
import sqlalchemy

from app import BookModel, app, db


class BookDBSeeder:
    def seed_db_from_json(self, filename):
        with app.app_context():
            with resources.files("data").joinpath(filename).open() as f:
                books = json.load(f)
                for record in books:
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
    csv_filename = "seeded_book_records.csv"
    json_filename = "seeded_book_records.json"
    while True:
        choice = int(
            input(
                "Choose from the following:\n"
                "1. Seed from JSON file\n"
                "2. Seed from CSV file\n"
                "Please enter your choice:\n"
            )
        )
        try:
            match choice:
                case 1:
                    print("you chose to seed with JSON file\n")
                    BookDBSeeder().seed_db_from_json(json_filename)
                    break
                case 2:
                    print("you chose to seed with CSV file\n")
                    print(f"will read from this file: {csv_filename}\n")
                    BookDBSeeder().seed_db_from_csv(csv_filename)
                    break
                case _:
                    print("you must choose either 1 or 2, try again ...\n")
        except sqlalchemy.exc.IntegrityError as e:
            print(
                f"Error in seeding - has the database already been seeded?\n"
                f"See stacktrace below:\n{e}"
            )
        except Exception as e:
            print("Unexpected error:", sys.exc_info()[0])
            print(f"See stacktrace below:\n{e}")
        finally:
            print("taking you back to the options screen\n")
            time.sleep(2)
