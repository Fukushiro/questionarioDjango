# Generated by Django 3.1.6 on 2021-02-06 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_remove_custom_user_ativo'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom_user',
            name='tipo',
            field=models.IntegerField(default=1),
        ),
    ]