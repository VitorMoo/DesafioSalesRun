from . models import Users
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(Users)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'role', 'cpf', 'is_staff']
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('role', 'cpf')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'cpf')}),
    )