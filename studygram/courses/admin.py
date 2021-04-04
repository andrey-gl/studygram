from django.contrib import admin
from .models import Task, Status


admin.site.register(Status)
admin.site.register(Task)