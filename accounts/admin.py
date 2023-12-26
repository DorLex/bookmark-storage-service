from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('id', 'email', 'is_staff')
    list_display_links = ('id', 'email')
    search_fields = ('email',)
    ordering = ('id',)

    fieldsets = (
        (
            None,
            {
                'fields': ('email', 'password')
            }
        ),

        (
            'Personal info',
            {
                'fields': ('username', 'first_name', 'last_name')
            }
        ),

        (
            'Permissions',
            {
                'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)
            }
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2',)
            }
        ),
    )
