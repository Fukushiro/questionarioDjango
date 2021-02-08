from django.db import models
from usuario.models import (
    custom_user,
)
# Create your models here.


class Questionario(models.Model):
    nome = models.CharField(max_length=50)


class Opcao(models.Model):
    questao = models.ForeignKey("questao.Questao",  on_delete=models.CASCADE)
    numero = models.IntegerField(null=True)
    texto = models.CharField(max_length=100)

    def __str__(self):
        return self.texto


class Questao(models.Model):
    questionario = models.ForeignKey(
        Questionario,  on_delete=models.CASCADE)
    enunciado = models.CharField(max_length=200, null=False, blank=False)
    correta = models.ForeignKey("questao.Opcao", on_delete=models.DO_NOTHING,
                                null=True, related_name='questaocorreta', blank=True)


class Resposta(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    resposta = models.IntegerField()
    usuario = models.ForeignKey(
        custom_user, on_delete=models.CASCADE, null=True)


class Nota(models.Model):
    questionario = models.ForeignKey(
        Questionario, on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey(custom_user, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2)
