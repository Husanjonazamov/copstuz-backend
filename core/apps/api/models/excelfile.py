from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class ExcelfileModel(AbstractBaseModel):
    file = models.FileField(
        verbose_name=_("Fayl"),
        upload_to="excel/file",
    )
    is_acivate = models.BooleanField(
        verbose_name=_("Faolmi ?"),
        default=True,
    )

    def __str__(self):
        return f"{self.is_acivate}"
    
    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "ExcelFile"
        verbose_name = _("ExcelfileModel")
        verbose_name_plural = _("ExcelfileModels")
