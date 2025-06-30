from rest_framework import viewsets, permissions, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from .models import NetworkNode, Product
from users.views import IsActiveEmployee
from .serializers import NetworkNodeSerializer, ProductSerializer


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all().select_related('supplier').select_related('products')
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveEmployee]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'country': ['exact'],
        'city': ['exact'],
    }
    search_fields = ['name', 'email', 'country', 'city']
    ordering_fields = ['name', 'created_at', 'debt']
    ordering = ['name']

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        if 'debt' in serializer.validated_data:
            del serializer.validated_data['debt']
        serializer.save()

    @action(detail=True, methods=['post'])
    def clear_debt(self, request, pk=None):
        node = self.get_object()
        node.debt = 0
        node.save()
        return Response({'status': 'debt cleared'})


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().select_related('network_node')
    serializer_class = ProductSerializer
    permission_classes = [IsActiveEmployee]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['network_node', 'release_date']
    search_fields = ['name', 'model']
