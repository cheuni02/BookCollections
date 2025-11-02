# app/routes/__init__.py
from app import api
from app.routes.books import Book, Books

api.add_resource(Books, "/api/books")
api.add_resource(Book, "/api/books/<int:id>")
