# Python
from typing import Any

# Django
from django.core.mail import send_mail
from django.db.models.base import ModelBase
from django.db.models.signals import (
    post_delete,
    post_save,
    pre_delete,
    pre_save
)
from django.dispatch import receiver

# First party
from temp.models import TempModel


@receiver(
    post_save,
    sender=TempModel
)
def post_save_tempmodel(
    sender: ModelBase,
    instance: TempModel,
    created: bool,
    **kwargs: Any
) -> None:
    """Signal post-save TempModel."""

    obj_id: int = instance.id
    name: str = instance.name
    number: int = instance.number

    send_mail(
        'TempModel создан | POST_SAVE',
        f'ID: {obj_id} | Имя: {name} | Номер: {number} | Создан: {created}',
        'x.public.profile@gmail.com',
        ['x.public.profile@gmail.com'],
        fail_silently=False,
    )


@receiver(
    pre_save,
    sender=TempModel
)
def pre_save_tempmodel(
    sender: ModelBase,
    instance: TempModel,
    **kwargs: Any
) -> None:
    """Signal post-save TempModel."""

    name: str = instance.name
    number: int = instance.number

    send_mail(
        'TempModel создается | PRE_SAVE',
        f'Имя: {name} | Номер: {number}',
        'x.public.profile@gmail.com',
        ['x.public.profile@gmail.com'],
        fail_silently=False,
    )


@receiver(
    post_delete,
    sender=TempModel
)
def post_delete_tempmodel(
    sender: ModelBase,
    instance: TempModel,
    **kwargs: Any
) -> None:
    """Signal post-delete TempModel."""

    obj_id: int = instance.id
    name: str = instance.name
    number: int = instance.number

    send_mail(
        'TempModel удален | POST_DELETE',
        f'ID: {obj_id} | Имя: {name} | Номер: {number}',
        'x.public.profile@gmail.com',
        ['x.public.profile@gmail.com'],
        fail_silently=False,
    )


@receiver(
    pre_delete,
    sender=TempModel
)
def pre_delete_tempmodel(
    sender: ModelBase,
    instance: TempModel,
    **kwargs: Any
) -> None:
    """Signal post-delete TempModel."""

    name: str = instance.name
    number: int = instance.number

    send_mail(
        'TempModel удаляется | PRE_DELETE',
        f'Имя: {name} | Номер: {number}',
        'x.public.profile@gmail.com',
        ['x.public.profile@gmail.com'],
        fail_silently=False,
    )
