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
        ]


class ListBotuserSerializer(BaseBotuserSerializer):
    class Meta(BaseBotuserSerializer.Meta): ...


class RetrieveBotuserSerializer(BaseBotuserSerializer):
    class Meta(BaseBotuserSerializer.Meta): ...



class CreateBotuserSerializer(serializers.ModelSerializer):
    branch = serializers.CharField()

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

    def create(self, validated_data):
        branch_name = validated_data.pop("branch")

        branch, _ = BranchModel.objects.get_or_create(name=branch_name)

        bot_user = BotuserModel.objects.create(branch=branch, **validated_data)
        return bot_user
