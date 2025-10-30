from api import app, db, BookModel

# just for testing purposes
seeded_records = [
  {
    "title": "A Particularly Nasty Case",
    "author": "Adam Kay",
    "year_published": 2025,
    "genre": "Fiction"
  },
  {
    "title": "Night Swimmers",
    "author": "Roisin Maguire",
    "year_published": 2024,
    "genre": "Fiction"
  },
  {
    "title": "Green Dot",
    "author": "Madeleine Gray",
    "year_published": 2024,
    "genre": "Humour"
  },
  {
    "title": "The Cyclist",
    "author": "Tim Sullivan",
    "year_published": 2021,
    "genre": "Crime fiction thriller"
  },
  {
    "title": "Onyx Storm (The Empyrean, #3)",
    "author": "Rebecca Yarros",
    "year_published": 2025,
    "genre": "Fantasy"
  }
]


if __name__ == "__main__":
    with app.app_context():
        for record in seeded_records:
            print(record["title"])
            book = BookModel(
                title=record["title"],
                author=record["author"],
                year_published=record["year_published"],
                genre=record["genre"],
            )
            db.session.add(book)
        db.session.commit()