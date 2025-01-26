from django.contrib import admin
from .models import Challenge, UserChallenge

@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('name', 'points')
    search_fields = ('name',)


@admin.register(UserChallenge)
class UserChallengeAdmin(admin.ModelAdmin):
    list_display = ('user', 'challenge', 'status')
    search_fields = ('user__username', 'challenge__name')