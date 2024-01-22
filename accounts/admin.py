# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import FgfUser

class CustomFgfUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('role',)  # Add 'role' to the list display

# Register the FgfUser model with the CustomFgfUserAdmin
admin.site.register(FgfUser, CustomFgfUserAdmin)
