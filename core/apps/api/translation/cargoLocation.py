from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import CargolocationModel


@register(CargolocationModel)
class CargolocationTranslation(TranslationOptions):
    fields = []
