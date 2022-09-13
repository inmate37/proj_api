from django.db.models import (
    Model,
    CharField,
    IntegerField,
    BooleanField,
)


class TempModel(Model):
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

    class Meta:
        ordering = (
            'number',
        )
        verbose_name = 'временная модель'
        verbose_name_plural = 'временные модели'

    def __str__(self) -> str:
        return f'Временная модель: {self.name}'
