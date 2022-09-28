# Python
from typing import (
    Any,
    Optional
)
from datetime import datetime

# Django
from django.db.models import (
    BooleanField,
    CharField,
    F,
    IntegerField,
    QuerySet
)

# First party
from abstracts.models import AbstractsDateTime

# Local
from .validators import TempModelValidator


class TempModelQuerySet(QuerySet):
    """TempModelQuerySet."""

    def get_deleted(self) -> QuerySet['TempModel']:
        return self.filter(
            datetime_deleted__isnull=False
        )

    def get_not_deleted(self) -> QuerySet['TempModel']:
        return self.filter(
            datetime_deleted__isnull=True
        )

    def get_not_equal_updated(self) -> QuerySet['TempModel']:
        return self.exclude(
            datetime_updated=F('datetime_created')
        )

    def get_obj(self, p_key: str) -> Optional['TempModel']:
        try:
            return self.get(
                id=p_key
            )
        except TempModel.DoesNotExist:
            return None


class TempModel(
    TempModelValidator,
    AbstractsDateTime
):
    """TempModel."""

    name = CharField(
        verbose_name='имя',
        max_length=25
    )
    number = IntegerField(
        verbose_name='число',
    )
    is_activated = BooleanField(
        default=False
    )

    objects = TempModelQuerySet().as_manager()

    class Meta:
        ordering = (
            'number',
        )
        verbose_name = 'временная модель'
        verbose_name_plural = 'временные модели'

    def clean(self) -> None:
        self.validate_number(
            self.number
        )

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.full_clean()
        super().save(*args, **kwargs)

    def delete(self) -> None:
        self.datetime_deleted = datetime.now()
        self.save(
            update_fields=['datetime_deleted']
        )
        # super().delete()

    def __str__(self) -> str:
        return f'Временная модель: {self.name}'
