from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    IntegerField,
    BooleanField,
)
from temp.models import TempModel


class TempSerializer(ModelSerializer):
    """TempSerializer."""

    name = CharField(required=False)
    number = IntegerField(required=False)
    is_activated = BooleanField(required=False)

    class Meta:
        model = TempModel
        fields = (
            'id',
            'name',
            'number',
            'is_activated',
        )
