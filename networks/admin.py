from django.contrib import admin

from networks.models import NetworkNode, Product


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'node_type', 'supplier')
    list_filter = ('country', 'city')
    search_fields = ('country', 'city')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model')
    list_filter = ('name', 'model')
    search_fields = ('name', 'model')