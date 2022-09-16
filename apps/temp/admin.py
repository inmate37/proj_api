from django.contrib import admin

from temp.models import TempModel


class TempModelAdmin(admin.ModelAdmin):
    """TempModelAdmin."""

    readonly_fields = (
        'name',
        'number',
        'is_activated',
        'datetime_created',
        'datetime_updated',
        'datetime_deleted',
    )


admin.site.register(
    TempModel, TempModelAdmin
)
