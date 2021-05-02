from django.contrib import admin
from .models import User, UserStatus, UserType
# Register your models here.
from django.contrib.auth.admin import UserAdmin


admin.site.register(UserStatus)
admin.site.register(UserType)
admin.site.register(User, UserAdmin)
