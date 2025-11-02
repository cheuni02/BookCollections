from flask_restful import reqparse

book_args = reqparse.RequestParser()
book_args.add_argument("title", type=str, required=True, help="title is required")
book_args.add_argument("author", type=str, required=True, help="author is required")
book_args.add_argument(
    "year_published", type=int, required=True, help="year is required"
)
book_args.add_argument("genre", type=str, required=True, help="genre is required")
