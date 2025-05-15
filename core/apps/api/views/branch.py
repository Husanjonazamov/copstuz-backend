from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import BranchModel
from core.apps.api.serializers.branch import CreateBranchSerializer, ListBranchSerializer, RetrieveBranchSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status



@extend_schema(tags=["branch"])
class BranchView(BaseViewSetMixin, ModelViewSet):
    queryset = BranchModel.objects.all()
    serializer_class = ListBranchSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListBranchSerializer,
        "retrieve": RetrieveBranchSerializer,
        "create": CreateBranchSerializer,   
    }

    @action(detail=False, methods=['get'], url_path="(?P<branch_name>[^/.]+)")
    def get_name(self, request, branch_name=None):
        try:
            branch = BranchModel.objects.get(name=branch_name)
            
            return Response({"branch_id": branch.id}, status=status.HTTP_200_OK)
        
        except BranchModel.DoesNotExist:
            return Response({"error": "Branch not found"}, status=status.HTTP_404_NOT_FOUND) 
    
    
    
    @action(detail=False, methods=['get'], url_path="branch-id/(?P<branch_id>[^/.]+)")
    def get_name_by_id(self, request, branch_id=None):
        try:
            branch = BranchModel.objects.get(id=branch_id)
            return Response({"branch_name": branch.name}, status=status.HTTP_200_OK)
        except BranchModel.DoesNotExist:
            return Response({"error": "Branch not found"}, status=status.HTTP_404_NOT_FOUND)