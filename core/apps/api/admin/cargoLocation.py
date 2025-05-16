from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import CargolocationModel


@admin.register(CargolocationModel)
class CargolocationAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
