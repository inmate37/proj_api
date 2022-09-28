# DRF
from rest_framework.serializers import (
    BooleanField,
    CharField,
    IntegerField,
    ModelSerializer,
    SerializerMethodField
)

# First party
from temp.models import TempModel


class TempSerializer(ModelSerializer):
    """TempSerializer."""

    name = CharField(required=True)
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


class TempTwoSerializer(ModelSerializer):
    """TempTwoSerializer."""

    name = CharField(required=False)
    datetime_created = SerializerMethodField(
        method_name='get_datetime_created'
    )
    datetime_updated = SerializerMethodField(
        method_name='get_datetime_updated'
    )
    datetime_deleted = SerializerMethodField(
        method_name='get_datetime_deleted'
    )

    class Meta:
        model = TempModel
        fields = (
            'id',
            'name',
            'datetime_created',
            'datetime_updated',
            'datetime_deleted',
        )

    def get_datetime_created(self, obj: TempModel) -> str:
        if '.' in str(obj.datetime_created):
            return f'{obj.datetime_created}'[:-13]
        return f'{obj.datetime_created}'[:-9]

    def get_datetime_updated(self, obj: TempModel) -> str:
        if '.' in str(obj.datetime_updated):
            return f'{obj.datetime_updated}'[:-13]
        return f'{obj.datetime_updated}'[:-9]

    def get_datetime_deleted(self, obj: TempModel) -> str:
        if not obj.datetime_deleted:
            return 'Объект не удален'

        if '.' in str(obj.datetime_deleted):
            return f'{obj.datetime_deleted}'[:-13]
        return f'{obj.datetime_deleted}'[:-9]
