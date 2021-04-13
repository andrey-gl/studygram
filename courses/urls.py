from django.urls import path
from .views import *

urlpatterns = [
    path('', CoursesList.as_view(), name='main'),
    path('tasks', TasksList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskView.as_view(), name='task'),
    path('create_task', CreateTask.as_view(), name='create_task'),
    path('courses/', CoursesList.as_view(), name='courses'),
    path('course/<int:pk>', CourseView.as_view(), name='course'),
    path('create_course', CreateCourse.as_view(), name='create_course')
]
