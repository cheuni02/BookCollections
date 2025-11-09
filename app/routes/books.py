import sqlalchemy
from flask_restful import Resource, abort, marshal_with

from app import db
from app.models import BookModel
from app.schemas import bookFields
from app.validation import book_args


class Books(Resource):
    @marshal_with(bookFields)
    def get(self):
        books = BookModel.query.all()
        if not books:
            abort(404, message="Apologies, Empty book collection")
        return books, 200

    @marshal_with(bookFields)
    def post(self):
        try:
            args = book_args.parse_args()
            book = BookModel(
                title=args["title"],
                author=args["author"],
                year_published=args["year_published"],
                genre=args["genre"],
            )
            db.session.add(book)
            db.session.commit()
            books = BookModel.query.all()
            return books, 201
        except sqlalchemy.exc.IntegrityError:
            db.session.rollback()
            abort(
                409,
                error="Conflict",
                message="Book already exists. Cannot create this book.",
            )


class Book(Resource):
    @marshal_with(bookFields)
    def get(self, id):
        book = BookModel.query.filter_by(id=id).first()
        if not book:
            abort(404, message=f"No book found with id {id}")
        return book, 200

    @marshal_with(bookFields)
    def patch(self, id):
        args = book_args.parse_args()
        book = BookModel.query.filter_by(id=id).first()
        if not book:
            abort(404, message="No book found with that id")
        book.title = args["title"]
        book.author = args["author"]
        book.year_published = args["year_published"]
        book.genre = args["genre"]
        db.session.commit()
        books = BookModel.query.all()
        return books, 201

    @marshal_with(bookFields)
    def delete(self, id):
        book = BookModel.query.filter_by(id=id).first()
        if not book:
            abort(404, message="No book found with that id")
        db.session.delete(book)
        db.session.commit()
        books = BookModel.query.all()
        return books, 204
