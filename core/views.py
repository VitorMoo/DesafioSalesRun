from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q

from accounts.models import Users
from .models import UserChallenge
from django.shortcuts import render, redirect, get_object_or_404


@login_required
def my_challenges(request):
    user_challenges = UserChallenge.objects.filter(user=request.user)
    return render(request, 'core/my_challenges.html', {'user_challenges': user_challenges})

@login_required
def home(request):
    user = request.user

    desafios_resumo = UserChallenge.objects.filter(user=user).aggregate(
        pendentes=Count('id', filter=Q(status='pending')),
        aceitos=Count('id', filter=Q(status='accepted')),
        concluidos=Count('id', filter=Q(status='completed')),
    )
    total_pontos = user.total_points

    desafios = UserChallenge.objects.filter(user=user).select_related('challenge')

    context = {
        'desafios_resumo': desafios_resumo,
        'total_pontos': total_pontos,
        'desafios': desafios,
    }
    return render(request, 'core/home.html', context)


@login_required
def complete_challenge(request, challenge_id):
    user_challenge = get_object_or_404(UserChallenge, id=challenge_id, user=request.user)

    if user_challenge.status == 'accepted':
        user_challenge.status = 'completed'
        user_challenge.save()

        request.user.total_points += user_challenge.challenge.points
        request.user.save()

        messages.success(request, "Desafio concluído!")
    else:
        messages.error(request, "Você não pode concluir este desafio.")

    return redirect('my_challenges')


def decline_challenge(request, challenge_id):
    if request.method == 'POST':
        user_challenge = get_object_or_404(UserChallenge, id=challenge_id, user=request.user)
        user_challenge.status = 'declined'
        user_challenge.save()
        messages.warning(request, 'Você recusou participar do desafio.')
    return redirect('my_challenges')

@login_required
def accept_challenge(request, challenge_id):
    user_challenge = get_object_or_404(UserChallenge, id=challenge_id, user=request.user)

    user_challenge.status = 'accepted'
    user_challenge.save()
    return redirect('my_challenges')

@login_required
def ranking(request):
    users_ranking = Users.objects.filter(is_staff=False).order_by('-total_points')
    return render(request, 'core/ranking.html', {'users_ranking': users_ranking})
