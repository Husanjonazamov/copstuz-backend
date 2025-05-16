from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import CargolocationModel


@receiver(post_save, sender=CargolocationModel)
def CargolocationSignal(sender, instance, created, **kwargs): ...
