from django.db import models
from social_django.models import UserSocialAuth


# Create your models here.
class States(models.Model):
    state = models.CharField(max_length=30, verbose_name='Состояние')

    def __str__(self):
        return self.state


class TelegramUserStates(models.Model):
    user = models.ForeignKey(UserSocialAuth, on_delete=models.CASCADE, verbose_name='Пользователь')
    state = models.ForeignKey(States, on_delete=models.CASCADE, verbose_name='Состояние')

