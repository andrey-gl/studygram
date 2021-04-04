from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks_list, name='tasks'),
    path('task/<int:pk>', views.task_view, name='task')
]
