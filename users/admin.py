from django.contrib import admin
from .models import User, UserStatus, UserType
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm


class AccountAdmin(UserAdmin):
    add_form = UserCreationForm

    fieldsets = (
        (None, {'fields': ('email', 'password', 'Type')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'patronymic')}),
        ('Permissions', {'fields': ('groups', 'is_staff', 'is_superuser', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

    list_display = ('email', 'first_name', 'last_name', 'Type')
    readonly_fields = ('id', 'date_joined', 'last_login')
    search_fields = ('email', 'first_name', 'last_name', 'Type')
    ordering = ('email',)


admin.site.register(UserStatus)
admin.site.register(UserType)
admin.site.register(User, AccountAdmin)
