from rest_framework import serializers

from core.apps.api.models import BotuserModel


class BaseBotuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotuserModel
        fields = [
            "id",
            "name",
        ]


class ListBotuserSerializer(BaseBotuserSerializer):
    class Meta(BaseBotuserSerializer.Meta): ...


class RetrieveBotuserSerializer(BaseBotuserSerializer):
    class Meta(BaseBotuserSerializer.Meta): ...


class CreateBotuserSerializer(BaseBotuserSerializer):
    class Meta(BaseBotuserSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
