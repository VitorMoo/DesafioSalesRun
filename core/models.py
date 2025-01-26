from django.db import models
from django.conf import settings

class Challenge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    banner = models.ImageField(upload_to='banners/', blank=True, null=True)
    rule_description = models.TextField(help_text="Ex: 'A cada R$600 em vendas de Vida = 1 ponto'")
    created_at = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField(default=0)


    def __str__(self):
        return self.name

class UserChallenge(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pendente'),
        ('accepted', 'Aceito'),
        ('refused', 'Recusado'),
        ('completed', 'Concluído'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f'{self.user} - {self.challenge} ({self.status})'
