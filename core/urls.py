from django.contrib.auth.views import LogoutView
from django.urls import path, include
from core import views as core_views, views

urlpatterns = [
    path('', views.home, name='home'),
    path('my-challenges/', views.my_challenges, name='my_challenges'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('accept-challenge/<int:challenge_id>/', views.accept_challenge, name='accept_challenge'),
    path('decline-challenge/<int:challenge_id>/', views.decline_challenge, name='decline_challenge'),
    path('complete-challenge/<int:challenge_id>/', views.complete_challenge, name='complete_challenge'),
    path('ranking/', views.ranking, name='ranking'),

]
