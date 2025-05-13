from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import BotuserModel
from core.apps.api.serializers.botuser import CreateBotuserSerializer, ListBotuserSerializer, RetrieveBotuserSerializer


@extend_schema(tags=["botuser"])
class BotuserView(BaseViewSetMixin, ModelViewSet):
    queryset = BotuserModel.objects.all()
    serializer_class = ListBotuserSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListBotuserSerializer,
        "retrieve": RetrieveBotuserSerializer,
        "create": CreateBotuserSerializer,
    }
