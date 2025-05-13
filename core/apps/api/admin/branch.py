from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import BranchModel


@admin.register(BranchModel)
class BranchAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
