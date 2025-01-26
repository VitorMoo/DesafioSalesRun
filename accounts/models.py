from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('corretor', 'Corretor'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='corretor')
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)
    total_points = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f'{self.username} ({self.get_role_display()})'