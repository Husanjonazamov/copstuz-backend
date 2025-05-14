from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import ExcelfileModel


@register(ExcelfileModel)
class ExcelfileTranslation(TranslationOptions):
    fields = []
