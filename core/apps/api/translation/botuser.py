from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import BotuserModel


@register(BotuserModel)
class BotuserTranslation(TranslationOptions):
    fields = []
