from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter

from networks.apps import NetworksConfig
from networks.views import NetworkNodeViewSet, ProductViewSet

app_name = NetworksConfig.name

router = DefaultRouter()
router.register(r'network-node', NetworkNodeViewSet, basename='network-node')
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [

              ] + router.urls