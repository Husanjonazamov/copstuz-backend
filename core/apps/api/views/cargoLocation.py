from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import CargolocationModel
from core.apps.api.serializers.cargoLocation import (
    CreateCargolocationSerializer,
    ListCargolocationSerializer,
    RetrieveCargolocationSerializer,
)


@extend_schema(tags=["CargoLocation"])
class CargolocationView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = CargolocationModel.objects.all()
    serializer_class = ListCargolocationSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListCargolocationSerializer,
        "retrieve": RetrieveCargolocationSerializer,
        "create": CreateCargolocationSerializer,
    }
