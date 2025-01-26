from django.contrib.auth.decorators import login_required
from .models import UserChallenge
from django.shortcuts import render, redirect


@login_required
def my_challenges(request):
    user_challenges = UserChallenge.objects.filter(user=request.user)
    return render(request, 'core/my_challenges.html', {'user_challenges': user_challenges})

