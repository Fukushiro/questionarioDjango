from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms
from questao.models import (
    Questionario,
    Questao,
    Opcao,
)


class QuestionarioForm(forms.ModelForm):
    class Meta:
        model = Questionario
        fields = '__all__'


class QuestaoForm(BSModalModelForm):
    class Meta:
        model = Questao
        fields = ['enunciado', 'correta']


class QuestaoFormUpdate(forms.ModelForm):
    class Meta:
        model = Questao
        fields = ['enunciado', 'correta']


class OpcaoForm(BSModalModelForm):
    class Meta:
        model = Opcao
        fields = ['texto']
