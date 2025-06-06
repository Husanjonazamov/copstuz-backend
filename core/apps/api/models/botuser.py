from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class LangChoice(models.TextChoices):
    UZ = "uz", _("Uzbek")
    RU = "ru", _("Russian")

class BotuserModel(AbstractBaseModel):
    user_id = models.BigIntegerField(
        verbose_name=_("Tg id"),
        default=0,
        unique=True,
        blank=True, null=True
    )
    lang = models.CharField(
        verbose_name=_("Til"),
        max_length=100,
        choices=LangChoice.choices,
        default=LangChoice.UZ,
    )
    name = models.CharField(
        verbose_name=_("Ism"),
        max_length=255,
        blank=True, null=True
    )
    phone = models.BigIntegerField(
        verbose_name=_("Telefon raqam"),
        blank=True, null=True
    )
    passport_id = models.CharField(
        verbose_name=_("Passport Id"),
        max_length=50,
        blank=True, null=True
    )
    passport_jsh = models.CharField(
        verbose_name=_("Passport Jshshr"),
        max_length=50,
        blank=True, null=True
    )
    birth_date = models.CharField(
        verbose_name=_("Tug'ilgan sana"),
        max_length=100,
        null=True, blank=True
    )
    address = models.TextField(
        verbose_name=_("Manzil"),
        blank=True, null=True
    )
    branch = models.ForeignKey(
        "api.BranchModel",
        on_delete=models.CASCADE,
        verbose_name=_("Shahar"),
        blank=True, null=True
    )
    passport_front = models.CharField(
        verbose_name=_("Old Rasm"),
        max_length=200,
        blank=True, null=True
    )
    passport_back = models.CharField(
        verbose_name=_("Orqa rasm"),
        max_length=200,
        blank=True, null=True
    )
    cargo_code = models.CharField(
        verbose_name=_("Yuk kodi"),
        max_length=255,
        default=0,
        blank=True, null=True
    )  

    def __str__(self):
        return self.name if self.name else "No name"

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "botuser"
        verbose_name = _("BotuserModel")
        verbose_name_plural = _("BotuserModels")
