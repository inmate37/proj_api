from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response

from django.db.models import QuerySet

from temp.models import TempModel
from temp.serializers import TempSerializer


class TempViewSet(ViewSet):
    """TempViewSet."""

    queryset: QuerySet[TempModel] = \
        TempModel.objects.all()

    def list(self, request: Request) -> Response:
        serializer: TempSerializer = \
            TempSerializer(
                self.queryset, many=True
            )

        return Response(
            serializer.data
        )
