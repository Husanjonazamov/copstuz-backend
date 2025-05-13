from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import BranchModel


@register(BranchModel)
class BranchTranslation(TranslationOptions):
    fields = []
