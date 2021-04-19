from django.contrib import admin
from .models import Task, StatusTask, Course, StatusCourse


admin.site.register(StatusTask)
admin.site.register(Task)
admin.site.register(Course)
admin.site.register(StatusCourse)
