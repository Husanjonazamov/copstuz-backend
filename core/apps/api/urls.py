from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.api.views import (
    BotuserView, 
    BranchView,
    CategoryView, 
    ExcelfileView,
    ExcelUploadView,
    CargolocationView
)

router = DefaultRouter()
router.register(r"users", BotuserView, basename="botuser")
router.register(r"category", CategoryView, basename="category")
router.register(r"branch", BranchView, basename="branch")
router.register(r"excel-file", ExcelfileView, basename="excel-file")
router.register(r"location", CargolocationView, basename="location")


urlpatterns = [
    path("", include(router.urls)),
    path("excel/create/", ExcelUploadView.as_view(), name="create")
]
