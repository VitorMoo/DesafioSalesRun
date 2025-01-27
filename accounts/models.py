from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('corretor', 'Corretor'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='corretor')
    cpf = models.CharField(max_length=11, unique=True, blank=False, null=False, help_text="Ex: 12345678901")
    total_points = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f'{self.username} ({self.get_role_display()})'