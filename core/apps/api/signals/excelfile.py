from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import ExcelfileModel


@receiver(post_save, sender=ExcelfileModel)
def ExcelfileSignal(sender, instance, created, **kwargs): ...
