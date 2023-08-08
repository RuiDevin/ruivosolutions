from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from solutions.views import ClienteViewSet, FuncionarioViewSet,FerramentaViewSet

router = DefaultRouter()
router.register(r"clientes", ClienteViewSet)
router.register(r"funcionarios", FuncionarioViewSet)
router.register(r"ferramentas", FerramentaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]