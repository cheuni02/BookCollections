from flask_restful import fields

bookFields = {
    "id": fields.Integer,
    "title": fields.String,
    "author": fields.String,
    "year_published": fields.Integer,
    "genre": fields.String,
}
