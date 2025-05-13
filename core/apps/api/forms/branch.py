from django import forms

from core.apps.api.models import BranchModel


class BranchForm(forms.ModelForm):

    class Meta:
        model = BranchModel
        fields = "__all__"
