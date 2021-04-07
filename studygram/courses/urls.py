from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks_list, name='tasks'),
    path('task/<int:pk>/<teachers>/<students>', views.task_view, name='task'),
    path('create_task', views.CreateTask, name='create_task'),
    path('courses', views.courses_list, name='courses'),
    path('create_course', views.create_course, name='create_course')
]
