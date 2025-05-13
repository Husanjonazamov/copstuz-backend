from rest_framework import serializers

from core.apps.api.models import BranchModel


class BaseBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchModel
        fields = [
            "id",
            "name",
        ]


class ListBranchSerializer(BaseBranchSerializer):
    class Meta(BaseBranchSerializer.Meta): ...


class RetrieveBranchSerializer(BaseBranchSerializer):
    class Meta(BaseBranchSerializer.Meta): ...


class CreateBranchSerializer(BaseBranchSerializer):
    class Meta(BaseBranchSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
