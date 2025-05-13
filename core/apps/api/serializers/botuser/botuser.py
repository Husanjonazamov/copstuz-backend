from rest_framework import serializers

from core.apps.api.models import BotuserModel


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
        ]


class ListBotuserSerializer(BaseBotuserSerializer):
    class Meta(BaseBotuserSerializer.Meta): ...


class RetrieveBotuserSerializer(BaseBotuserSerializer):
    class Meta(BaseBotuserSerializer.Meta): ...


class CreateBotuserSerializer(BaseBotuserSerializer):
    class Meta(BaseBotuserSerializer.Meta):
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
        ]

    def create(self, validate_data):
        bot_user = BotuserModel.objects.create(**validate_data)
        return bot_user