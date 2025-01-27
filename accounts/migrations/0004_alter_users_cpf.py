# Generated by Django 5.1.5 on 2025-01-27 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_users_total_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='cpf',
            field=models.CharField(default=0, help_text='Ex: 12345678901', max_length=11, unique=True),
            preserve_default=False,
        ),
    ]