# Generated by Django 3.1.6 on 2021-02-02 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.CharField(max_length=200)),
                ('correta', models.IntegerField()),
                ('questionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questao.questionario')),
            ],
        ),
        migrations.CreateModel(
            name='Opcao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('texto', models.CharField(max_length=100)),
                ('questao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questao.questao')),
            ],
        ),
    ]
