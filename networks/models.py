from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


NULLBLE = {"blank": True, "null": True}

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    model = models.CharField(max_length=255, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода на рынок')

    def __str__(self):
        return f"{self.name} {self.model}"


class NetworkNode(models.Model):
    NODE_TYPES = (
        (0, 'Factory'),
        (1, 'Retail chain'),
        (2, 'Individual entrepreneur'),
    )

    name = models.CharField(max_length=255, verbose_name='Название')
    node_type = models.IntegerField(choices=NODE_TYPES, verbose_name='Тип звена')
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=20, verbose_name='Номер дома')
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,
                                 verbose_name='Поставщик', **NULLBLE)
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL,
                                 verbose_name='Поставщик', related_name='children', **NULLBLE)
    debt = models.DecimalField(max_digits=12, decimal_places=2, default=0.0,
                               verbose_name='Задолженность перед поставщиком')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    @property
    def hierarchy_level(self):
        if self.node_type == 0:  # Factory
            return 0
        if not self.supplier:
            return 1  # If no supplier but not a factory, assume it's level 1
        return self.supplier.hierarchy_level + 1

    def __str__(self):
        return f"{self.get_node_type_display()}: {self.name}"
