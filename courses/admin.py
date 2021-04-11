from django.contrib import admin
from .models import Task, StatusTask, User, Course, StatusCourse


admin.site.register(StatusTask)
admin.site.register(Task)
admin.site.register(User)
admin.site.register(Course)
admin.site.register(StatusCourse)
