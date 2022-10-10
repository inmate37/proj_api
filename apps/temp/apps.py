# Django
from django.apps import AppConfig


class TempConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'temp'

    def ready(self) -> None:
        import temp.signals  # noqa
