from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import ExcelfileModel


@admin.register(ExcelfileModel)
class ExcelfileAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
