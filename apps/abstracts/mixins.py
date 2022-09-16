from typing import Any

from rest_framework.response import Response


class ResponseMixin:
    """ResponseMixin."""

    def get_json_response(self, data: dict[Any, Any]) -> Response:

        return Response(
            {
                'results': data
            }
        )

    def get_http_response(self, data: dict[Any, Any]) -> Response:
        raise NotImplementedError
