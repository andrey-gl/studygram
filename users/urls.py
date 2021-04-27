from django.urls import path
from django.urls import include
from django.views.generic import TemplateView
from .views import auth, register
urlpatterns = [
    path('auth/', include('social_django.urls'),  name='social'),
    path('profile', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('login', auth),
    path('register', register)
]
