# Future
from __future__ import annotations

# Python
import os
import sys
import json
from typing import (
    Any,
    Set
)
from datetime import (
    datetime,
    timedelta
)

# Third party
from bibtexparser.bparser import BibTexParser
from parsifal.reviews.models import Review
from pydantic import BaseModel

# DRF
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

# Django
from django.db.models import (
    CharField,
    F,
    Q,
    QuerySet
)
from django.urls import reverse_lazy

# First party
from abstracts.mixins import (
    ResponseMixin,
    ValidationMixin
)

# Local
from .models import TempModel
from .serializers import (
    TempSerializer,
    TempTwoSerializer
)


class TempViewSet(
    ValidationMixin,
    ResponseMixin,
    ViewSet
):
    """TempViewSet."""

    queryset: QuerySet[TempModel] = \
        TempModel.objects.all()

    @action(
        methods=['get'],
        detail=False,
        url_path='list-2',
        permission_classes=(
            AllowAny,
        )
    )
    def list_2(self, request: Request) -> Response:

        serializer: TempTwoSerializer = \
            TempTwoSerializer(
                self.queryset,
                many=True
            )
        return self.get_json_response(
            serializer.data
        )

    def list(self, request: Request) -> Response:

        serializer: TempSerializer = \
            TempSerializer(
                self.queryset.get_not_deleted(),
                many=True
            )
        return self.get_json_response(
            serializer.data
        )

    def retrieve(self, request: Request, pk: str) -> Response:

        obj: TempModel = self.get_obj_or_raise(
            self.queryset,
            pk
        )
        # obj: Optional[TempModel] = self.queryset.get_obj(
        #     pk
        # )
        # if not obj:
        #     return self.get_json_response(
        #         {
        #             'message': 'Объект не найден',
        #             'payload': {
        #                 'invalid_obj_id': f'{pk}'
        #             }
        #         }
        #     )
        serializer: TempSerializer = \
            TempSerializer(
                obj
            )
        return self.get_json_response(
            serializer.data
        )

    def destroy(self, request: Request, pk: str) -> Response:

        obj: TempModel = self.get_obj_or_raise(
            self.queryset,
            pk
        )
        # obj: Optional[TempModel] = self.queryset.get_obj(
        #     pk
        # )
        # if not obj:
        #     return self.get_json_response(
        #         {
        #             'message': 'Объект не найден',
        #             'payload': {
        #                 'invalid_obj_id': f'{pk}'
        #             }
        #         }
        #     )
        obj.delete()

        return self.get_json_response(
            {
                'message': 'Объект был удален',
                'payload': {
                    'obj_id': f'{obj.id}',
                    'obj_deleted': f'{obj.datetime_deleted}',
                }
            }
        )
