from unittest import mock

from app import app
from app.routes.books import Book, Books


class APIHelpers:
    def requestToBooksAPI(self, method, payload):
        with app.test_request_context(
            "/books",
            method=method,
            json=payload,
        ):
            resource = Books()
            match method:
                case "post":
                    response, statusCode = resource.post()
                case "get":
                    response, statusCode = resource.get()
                case _:
                    raise Exception("Unexpected mock method")
            return response, statusCode

    def mockRequestToBooksAPI(
        self, method, target, mocked_response, payload=None, BookId=None
    ):
        with mock.patch(target, return_value=mocked_response):
            with app.test_request_context(
                f"/books/{BookId}",
                method=method,
                json=payload,
            ):
                if not BookId:
                    resource = Books()
                else:
                    resource = Book()
                match method.upper():
                    case "POST":
                        response, statusCode = resource.post()
                    case "GET":
                        response, statusCode = resource.get(BookId)
                    case _:
                        raise Exception("Unexpected mock method")
                return response, statusCode
