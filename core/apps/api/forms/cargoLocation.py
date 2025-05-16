from django import forms

from core.apps.api.models import CargolocationModel


class CargolocationForm(forms.ModelForm):

    class Meta:
        model = CargolocationModel
        fields = "__all__"
