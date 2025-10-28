from flask import Flask
from flask_restful import Api, Resource, abort, fields, marshal_with, reqparse
from flask_sqlalchemy import SQLAlchemy

# import and initialise framework
app = Flask(__name__)

# db configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# initialise API
api = Api(app)

# Define model
class BookModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), nullable=False)
    year_published = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"BookModel(id = {self.id}, title = {self.title}, author = {self.author}, year_published = {self.year_published}), genre = {self.genre})"

# input validation
book_args = reqparse.RequestParser()
book_args.add_argument("title", type=str, required=True, help="title is required")
book_args.add_argument("author", type=str, required=True, help="author is required")
book_args.add_argument("year_published", type=int, required=True, help="year is required")
book_args.add_argument("genre", type=str, required=True, help="genre is required")

# define shape of data / serialisation
bookFields = {
    "id": fields.Integer,
    "title": fields.String,
    "author": fields.String,
    "year_published": fields.Integer,
    "genre": fields.String,
}

# defining resource classes: Book, Books
class Books(Resource):
    @marshal_with(bookFields)
    def get(self):
        books = BookModel.query.all()
        if not books:
            abort(404, message="Apologies, Empty book collection")
        return books, 200

    @marshal_with(bookFields)
    def post(self):
        args = book_args.parse_args()
        book = BookModel(
            title = args["title"],
            author = args["author"],
            year_published = args["year_published"],
            genre = args["genre"]
        )
        db.session.add(book)
        db.session.commit()
        books = BookModel.query.all()
        return books, 201

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


# registering routes
api.add_resource(Books, '/api/books')
api.add_resource(Book, '/api/books/<int:id>')

# healthcheck
@app.route('/')
def homepage():
    return '<h1> Health check </h1>>'
