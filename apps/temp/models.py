from typing import (
    Any,
    Optional,
)
from django.db.models import (
    CharField,
    IntegerField,
    BooleanField,
    QuerySet,
    F,
)
from abstracts.models import AbstractsDateTime


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


class TempModel(AbstractsDateTime):
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

    def save(self, *args: Any, **kwargs: Any) -> None:
        print(self)
        super().save(*args, **kwargs)

    def delete(self) -> None:
        self.datetime_deleted = datetime.now()
        self.save(
            update_field=['datetime_deleted']
        )
        # super().delete()

    def __str__(self) -> str:
        return f'Временная модель: {self.name}'
