from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import BotuserModel
from core.apps.api.serializers.botuser import CreateBotuserSerializer, ListBotuserSerializer, RetrieveBotuserSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


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
    
    @action(detail=False, methods=["get"], url_path="(?P<user_id>[^/.]+)")
    def by_user_id(self, request, user_id):
        users = BotuserModel.objects.filter(user_id=user_id)
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)
    
    
    
    @action(detail=False, methods=["patch"], url_path="update/(?P<user_id>[^/.]+)")
    def partial_update_user(self, request, user_id):
        try:
            user = BotuserModel.objects.get(user_id=user_id)
            serializer = self.get_serializer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        except BotuserModel.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
