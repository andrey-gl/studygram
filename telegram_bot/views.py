from django.dispatch import receiver
from django.db.models.signals import post_save
from social_django.models import UserSocialAuth
from .models import TelegramUserStates, States
from users.models import User
from django.db.models import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .bot import bot
from django.core.validators import validate_email
import json


@receiver(post_save, sender=UserSocialAuth)
def update_user_info(sender, **kwargs):
    user = sender.objects.all().last()
    try:
        user_state = TelegramUserStates.objects.get(user=user)
    except ObjectDoesNotExist:
        bot.send_message(user.uid, 'Пожалуйста, укажите ваш e-mail для обновления информации пользователя: ')
        print(user.user)
        TelegramUserStates.objects.create(user=user, state_id=1)


@csrf_exempt
def send_message(request):
    data = json.loads(request.body)
    uid = data["message"]["from"]["id"]
    user_state = TelegramUserStates.objects.get(user__uid=uid)
    social_user = UserSocialAuth.objects.get(uid=data["message"]["from"]["id"])
    if user_state.state.id == 1:
        # Проверяем тип текста сообщения
        if data["message"]["entities"][0]["type"] == 'email':
            """Проверяем наличие пользователя с заданным email в базе.
               Если есть, то меняем внешний ключ и удаляем пользователя, созданного виджетом.
               Иначе, просто задаём e-mail и пароль новому пользователю и отправляем пароль Telegram пользователю."""
            try:
                user = User.objects.get(email=data["message"]["text"])

                wrong_user = social_user.user.id

                # Меняем внешний ключ на нужного пользователя
                social_user.user = user
                social_user.save()

                # Удаляем пользователя, которого создал виджет авторизации
                user_to_delete = User.objects.get(id=wrong_user)
                user_to_delete.delete()

                # Обновляем статус телеграм пользователя
                user_state.state = States.objects.get(id=2)
                user_state.save()
            except ObjectDoesNotExist:
                # Добавляем e-mail пользователя и задаём случайны пароль
                user = User.objects.get(id=social_user.user.id)
                user.email = data["message"]["text"]
                password = User.objects.make_random_password()
                user.set_password(password)
                user.save()

                # Обновляем статус телеграм пользователя
                user_state.state = States.objects.get(id=2)
                user_state.save()

                bot.send_message(uid, f'Информация обновлена. \nВаш пароль для входа в систему: {password}.')
        else:
            bot.send_message(uid, 'Пожалуйста, введите правильный e-mail.')
    return HttpResponse(status=200)
