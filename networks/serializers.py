from rest_framework import serializers
from networks.models import NetworkNode, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'model', 'release_date',]
        read_only_fields = ['id']

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        fields = ['id', 'name', 'node_type']

class NetworkNodeSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    supplier = SupplierSerializer(read_only=True)
    supplier_id = serializers.PrimaryKeyRelatedField(
        queryset=NetworkNode.objects.all(),
        source='supplier',
        write_only=True,
        required=False,
        allow_null=True
    )
    hierarchy_level = serializers.IntegerField(read_only=True)

    class Meta:
        model = NetworkNode
        fields = [
            'id', 'name', 'node_type', 'email', 'country', 'city',
            'street', 'house_number', 'supplier', 'supplier_id', 'debt',
            'created_at', 'products', 'hierarchy_level'
        ]
        read_only_fields = ['debt', 'created_at', 'hierarchy_level']
