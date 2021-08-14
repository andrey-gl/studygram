from django.urls import path
from .views import send_message
urlpatterns = [
    path('', send_message, name='update')
]
