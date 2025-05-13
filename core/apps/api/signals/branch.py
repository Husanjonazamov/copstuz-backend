from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import BranchModel


@receiver(post_save, sender=BranchModel)
def BranchSignal(sender, instance, created, **kwargs): ...
