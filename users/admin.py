from django.contrib import admin
from .models import User, UserStatus, UserType
# Register your models here.

admin.site.register(UserStatus)
admin.site.register(UserType)


class UserAdmin(admin.ModelAdmin):
    models = User
    list_display = ('username', 'last_name', 'first_name', 'Type')
    search_fields = ['username', 'first_name', 'last_name']


admin.site.register(User, UserAdmin)
