from rest_framework import serializers

from core.apps.api.models import CargolocationModel


class BaseCargolocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargolocationModel
        fields = [
            "id",
            "cargo_type",
            "post_code",
            "is_active",
            "map_link"
        ]


class ListCargolocationSerializer(BaseCargolocationSerializer):
    class Meta(BaseCargolocationSerializer.Meta): ...


class RetrieveCargolocationSerializer(BaseCargolocationSerializer):
    class Meta(BaseCargolocationSerializer.Meta): ...


class CreateCargolocationSerializer(BaseCargolocationSerializer):
    class Meta(BaseCargolocationSerializer.Meta):
        fields = [
            "id",
            "cargo_type",
            "post_code",
            "is_active",
            "map_link"
        ]
