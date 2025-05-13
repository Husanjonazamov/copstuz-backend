from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.api.views import (
    BotuserView, 
    BranchView,
    CategoryView
)

router = DefaultRouter()
router.register(r"users", BotuserView, basename="botuser")
router.register(r"category", CategoryView, basename="category")
router.register(r"branch", BranchView, basename="branch")

urlpatterns = [
    path("", include(router.urls)),
]
