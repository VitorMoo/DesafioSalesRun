# Generated by Django 5.1.5 on 2025-01-26 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_users_lastname_remove_users_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='total_points',
            field=models.PositiveIntegerField(default=0),
        ),
    ]