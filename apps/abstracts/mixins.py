# Python
from typing import Any

# DRF
from rest_framework.response import Response

# Django
from django.db.models import QuerySet

# First party
from abstracts.validators import APIValidator


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


class ValidationMixin:
    """ValidationMixin."""

    def get_obj_or_raise(
        self,
        queryset: QuerySet[Any],
        p_key: str
    ) -> Any:

        obj: Any = queryset.get_obj(
            p_key
        )
        if not obj:
            raise APIValidator(
                f'Объект не найден: {p_key}',
                'error',
                '404'
            )
        return obj
