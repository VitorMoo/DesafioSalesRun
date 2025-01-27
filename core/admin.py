from django import forms
from django.contrib import admin
from .models import Challenge, UserChallenge
from accounts.models import Users

class UserChallengeForm(forms.ModelForm):
    class Meta:
        model = UserChallenge
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = Users.objects.all()
        self.fields['user'].label_from_instance = lambda obj: f"{obj.cpf or 'Sem CPF'}"

@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('name', 'points')
    search_fields = ('name',)

@admin.register(UserChallenge)
class UserChallengeAdmin(admin.ModelAdmin):
    form = UserChallengeForm
    list_display = ('user', 'challenge', 'status')
    search_fields = ('user__cpf', 'challenge__name')
