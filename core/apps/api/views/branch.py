from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import BranchModel
from core.apps.api.serializers.branch import CreateBranchSerializer, ListBranchSerializer, RetrieveBranchSerializer


@extend_schema(tags=["branch"])
class BranchView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = BranchModel.objects.all()
    serializer_class = ListBranchSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListBranchSerializer,
        "retrieve": RetrieveBranchSerializer,
        "create": CreateBranchSerializer,
    }
