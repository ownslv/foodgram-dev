from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        unique=True, max_length=100,
        verbose_name='Логин',
    )
    password = models.CharField(
        max_length=255, 
        verbose_name='Пароль',
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name='Имя пользователя',
    )
    last_name = models.CharField(
        max_length=50, 
        verbose_name='Фамилия',
    )
    email = models.EmailField(
        unique=True, 
        max_length=50,
        verbose_name='Электронная почта',
    )
    is_subcribed = models.BooleanField(
        default=False,
        verbose_name='Подписка на автора',
    )

    class Meta:
        ordering = ['username']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
