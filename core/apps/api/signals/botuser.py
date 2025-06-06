from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import BotuserModel


@receiver(post_save, sender=BotuserModel)
def BotuserSignal(sender, instance, created, **kwargs): ...
