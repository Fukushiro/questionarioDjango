# Generated by Django 3.1.6 on 2021-02-08 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questao', '0009_auto_20210205_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questao',
            name='questionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questao.questionario'),
        ),
    ]
