from django.contrib import admin

from temp.models import TempModel


class TempModelAdmin(admin.ModelAdmin):

    readonly_fields = (
        'is_activated',
    )


admin.site.register(
    TempModel, TempModelAdmin
)
