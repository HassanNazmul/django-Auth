# Register your models here.


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    # Define what fields to display in the admin interface
    list_display = ('email', 'name', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_active', 'is_superuser')

    # Fields to display on the form when creating or updating a user
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name',)}),
        ('Permissions', {'fields': (('is_active', 'is_staff', 'is_superuser'),)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', ('is_active', 'is_staff', 'is_superuser'))}
         ),
    )
    search_fields = ('email', 'name')
    ordering = ('email',)


# Register the model and the custom admin interface
admin.site.register(CustomUser, CustomUserAdmin)
