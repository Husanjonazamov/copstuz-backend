from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class BranchModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "branch"
        verbose_name = _("BranchModel")
        verbose_name_plural = _("BranchModels")
