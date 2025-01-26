from django.contrib import admin
from .models import Challenge, UserChallenge

@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']

@admin.register(UserChallenge)
class UserChallengeAdmin(admin.ModelAdmin):
    list_display = ['user', 'challenge', 'status', 'points']
    list_filter = ['status', 'challenge']
    search_fields = ['user__username', 'user__cpf', 'challenge__name']
