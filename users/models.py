from django.db import models
from django.contrib.auth.models import AbstractUser


class UserType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип пользователя'
        verbose_name_plural = 'Типы пользователей'
        ordering = ['id']


class UserStatus(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус пользователя'
        verbose_name_plural = 'Статусы пользователей'
        ordering = ['id']


class Group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(AbstractUser):
    Otchestvo = models.CharField(max_length=150, blank=True, verbose_name='Отчество')
    Group = models.ManyToManyField(Group, verbose_name='Группа', blank=True)
    Photo = models.ImageField(verbose_name='Фото', blank=True)
    Type = models.ForeignKey(UserType, on_delete=models.CASCADE, related_name='type', default=2)
    Status = models.ForeignKey(UserStatus, on_delete=models.CASCADE, related_name='status', default=1)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']
