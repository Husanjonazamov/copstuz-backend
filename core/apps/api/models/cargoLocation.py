from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel

class AvtoChoice(models.TextChoices):
    avia = "avia", _("Avia")
    avto = "avto", _("Avto")


class CargolocationModel(AbstractBaseModel):
    cargo_type = models.CharField(
        verbose_name=_("Turi"),
        choices=AvtoChoice.choices,
        default=AvtoChoice.avia,
        max_length=255,
        blank=True, null=True
    )
    location = models.TextField(
        verbose_name=_("Manzil"),
        blank=True, null=True
    )
    is_active = models.BooleanField(
        verbose_name=_("faolmi ?"),
        default=True
    )


    def __str__(self):
        return self.cargo_type

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "CargoLocation"
        verbose_name = _("CargolocationModel")
        verbose_name_plural = _("CargolocationModels")
