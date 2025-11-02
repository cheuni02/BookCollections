from . import db


class BookModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), nullable=False)
    year_published = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return (
            f"BookModel("
            f"id = {self.id}, "
            f"title = {self.title}, "
            f"author = {self.author}, "
            f"year_published = {self.year_published}, "
            f"genre = {self.genre})"
        )
