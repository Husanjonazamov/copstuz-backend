from django_filters import rest_framework as filters

from core.apps.api.models import BranchModel


class BranchFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = BranchModel
        fields = [
            "name",
        ]
