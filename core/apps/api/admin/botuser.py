from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import BotuserModel


@admin.register(BotuserModel)
class BotuserAdmin(ModelAdmin):
    list_display = (
        "id",
        'name',
        'branch',
        'phone',
        'lang'
    )
