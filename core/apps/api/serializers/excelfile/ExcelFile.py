from rest_framework import serializers

from core.apps.api.models import ExcelfileModel


class BaseExcelfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelfileModel
        fields = [
            "id",
            "name",
        ]


class ListExcelfileSerializer(BaseExcelfileSerializer):
    class Meta(BaseExcelfileSerializer.Meta): ...


class RetrieveExcelfileSerializer(BaseExcelfileSerializer):
    class Meta(BaseExcelfileSerializer.Meta): ...


class CreateExcelfileSerializer(BaseExcelfileSerializer):
    class Meta(BaseExcelfileSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
