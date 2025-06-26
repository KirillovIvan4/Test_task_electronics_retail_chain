from django.contrib.auth.models import AbstractUser
from django.db import models

NULLBLE = {"blank": True, "null": True}


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, **NULLBLE)
    is_active = models.BooleanField(default=True, verbose_name='Активный сотрудник')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
