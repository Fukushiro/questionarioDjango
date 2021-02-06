from django.contrib import admin
from questao.models import (
    Questionario,
    Questao,
    Opcao,
    Resposta,
)
# Register your models here.



admin.site.register(Questionario)
admin.site.register(Questao)
admin.site.register(Opcao)
admin.site.register(Resposta)