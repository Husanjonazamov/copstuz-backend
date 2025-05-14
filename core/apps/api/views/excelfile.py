from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import ExcelfileModel
from core.apps.api.serializers.excelfile import (
    CreateExcelfileSerializer,
    ListExcelfileSerializer,
    RetrieveExcelfileSerializer,
)


@extend_schema(tags=["ExcelFile"])
class ExcelfileView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = ExcelfileModel.objects.all()
    serializer_class = ListExcelfileSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListExcelfileSerializer,
        "retrieve": RetrieveExcelfileSerializer,
        "create": CreateExcelfileSerializer,
    }
