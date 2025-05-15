from rest_framework import serializers

from core.apps.api.models import BotuserModel, BranchModel


class BaseBotuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotuserModel
        fields = [
            "id",
            "lang",
            "user_id",
            "name",
            "phone",
            "passport_id",
            "passport_jsh",
            "birth_date",
            "address",
            "branch",
            "passport_front",
            "passport_back",
            "cargo_code"
        ]


class ListBotuserSerializer(BaseBotuserSerializer):
    class Meta(BaseBotuserSerializer.Meta): ...


class RetrieveBotuserSerializer(BaseBotuserSerializer):
    class Meta(BaseBotuserSerializer.Meta): ...



class CreateBotuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotuserModel
        fields = [
            "id",
            "lang",
            "user_id",
            "name",
            "phone",
            "passport_id",
            "passport_jsh",
            "birth_date",
            "address",
            "branch",
            "passport_front",
            "passport_back",
            "cargo_code"
        ]

    def create(self, validated_data):
        bot_user = BotuserModel.objects.create(**validated_data)
        return bot_user
