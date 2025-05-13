from django import forms

from core.apps.api.models import BotuserModel


class BotuserForm(forms.ModelForm):

    class Meta:
        model = BotuserModel
        fields = "__all__"
