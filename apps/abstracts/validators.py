from typing import Optional

from django.core.exceptions import ValidationError
from rest_framework.exceptions import APIException
from rest_framework.status import (HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN,
                                   HTTP_404_NOT_FOUND,
                                   HTTP_500_INTERNAL_SERVER_ERROR)


class APIValidator(APIException):
    """General-purpose validator for API."""

    status_code: Optional[int] = None
    status_map: dict[str, int] = {
        '500': HTTP_500_INTERNAL_SERVER_ERROR,
        '404': HTTP_404_NOT_FOUND,
        '403': HTTP_403_FORBIDDEN,
        '400': HTTP_400_BAD_REQUEST,
    }

    def __init__(
        self, message: str, field: str, code: str = '400'
    ) -> None:

        self.status_code = self.status_map.get(
            code, None
        )
        if not self.status_code:
            raise ValidationError(
                'Статус код неизвестен'
            )

        if message:
            self.detail = {
                field: message
            }
        else:
            self.detail = {
                'error': 'Сервер не отвечает'
            }
