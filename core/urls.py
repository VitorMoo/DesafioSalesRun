from django.contrib import admin
from django.urls import path, include
from core import views as core_views, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my-challenges/', views.my_challenges, name='my_challenges'),

]
