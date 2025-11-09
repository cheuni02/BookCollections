from unittest import mock

from app import app
from app.routes.books import Books


class APIHelpers:
    def requestToBooksAPI(self, method, target, payload, mocked_response):
        with mock.patch(target, return_value=mocked_response):
            with app.test_request_context(
                "/books",
                method=method,
                json=payload,
            ):
                resource = Books()
                response, status_code = resource.post()
                return response, status_code
