from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import ExcelfileModel
from core.apps.api.serializers.excelfile import (
    CreateExcelfileSerializer,
    ListExcelfileSerializer,
    RetrieveExcelfileSerializer,
)

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from django.core.files.storage import FileSystemStorage
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
import pandas as pd
from rest_framework import status


@extend_schema(tags=["ExcelFile"])
class ExcelfileView(BaseViewSetMixin, ModelViewSet):
    queryset = ExcelfileModel.objects.all()
    serializer_class = ListExcelfileSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListExcelfileSerializer,
        "retrieve": RetrieveExcelfileSerializer,
        "create": CreateExcelfileSerializer,
    }

    @action(detail=False, methods=['post'], url_path="me")
    def search_by_id(self, request, pk=None):
        excel_id = request.data.get("id")
        if not excel_id:
            return Response({"detail": "ID berilmagan."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            active_excel = ExcelfileModel.objects.filter(is_acivate=True).first()
            if not active_excel:
                return Response({"detail": "Faol Excel fayli topilmadi."}, status=status.HTTP_404_NOT_FOUND)
        except ExcelfileModel.DoesNotExist:
            return Response({"detail": "Excel fayli topilmadi."}, status=status.HTTP_404_NOT_FOUND)

        fs = FileSystemStorage()
        filepath = fs.path(active_excel.file.name)

        try:
            df = pd.read_excel(filepath)
        except Exception as e:
            return Response({"detail": f"Faylni o'qishda xatolik: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        df["TREK NUMBER"] = df["TREK NUMBER"].astype(str)
        excel_id = str(excel_id)

        matching_row = df[df["TREK NUMBER"] == excel_id]

        if matching_row.empty:
            return Response({"detail": "❌ Buyurtma mavjud emas."}, status=status.HTTP_404_NOT_FOUND)

        row = matching_row.iloc[0]

        result = {
            "KG": row["KG"],
            "Q-TY": row["Q-TY"],
            "DATE": row["DATE"],
            "TREK_NUMBER": row["TREK NUMBER"],
            
        }

        return Response({
            "detail": "✅ Buyurtma topildi!",
            "data": result
        }, status=status.HTTP_200_OK)

            


class ExcelUploadView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        uploaded_file = request.FILES.get('file')
        if not uploaded_file:
            return Response({"error": "Fayl yuborilmadi"}, status=400)

        excel_file = ExcelfileModel.objects.create(file=uploaded_file)
        return Response({"message": "Fayl saqlandi", "file_url": excel_file.file.url})

