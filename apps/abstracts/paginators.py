# Python
from typing import Any

# DRF
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
)
from rest_framework.response import Response


class AbstractPageNumberPaginator(PageNumberPagination):
    """AbstractPageNumberPaginator."""

    page_size_query_param: str = 'page_size'
    page_query_param: str = 'page'
    max_page_size: int = 10
    page_size: int = 2

    def get_paginated_response(self, data: list[Any]) -> Response:
        """Overriden method."""

        response: Response = \
            Response(
                {
                    'pagination': {
                        'next': self.get_next_link(),
                        'previous': self.get_previous_link(),
                        'count': self.page.paginator.num_pages,
                    },
                    'results': data
                }
            )
        return response


class AbstractLimitOffsetPaginator(LimitOffsetPagination):
    """AbstractLimitOffsetPaginator."""

    limit: int = 2
    offset: int = 0

    def get_paginated_response(self, data: list[Any]) -> Response:
        """Overriden method."""

        response: Response = \
            Response(
                {
                    'pagination': {
                        'next': self.get_next_link(),
                        'previous': self.get_previous_link(),
                    },
                    'results': data
                }
            )
        return response
