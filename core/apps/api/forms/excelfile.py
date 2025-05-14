from django import forms

from core.apps.api.models import ExcelfileModel


class ExcelfileForm(forms.ModelForm):

    class Meta:
        model = ExcelfileModel
        fields = "__all__"
