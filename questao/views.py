from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from questao.models import (
    Questionario,
    Questao,
    Opcao,
    Resposta,
    Nota,
)

from questao.forms import (
    QuestionarioForm,
    QuestaoForm,
    QuestaoFormUpdate,
    OpcaoForm,
)
from django.contrib.auth.decorators import login_required
from bootstrap_modal_forms.forms import BSModalModelForm
from bootstrap_modal_forms.generic import BSModalCreateView
from django.urls import reverse_lazy
from django.template.loader import render_to_string

# Create your views here.


@login_required
def home(request):

    c = {
        'user': request.user,
    }
    return render(request, 'questao/home.html', c)


def home_usuario(request):

    c = {
        'user': request.user,
    }
    return render(request, 'questao/home_usuario.html', c)
# responder


def ver_questao(request, id):

    questionario = None
    questoes = None
    opcoes = None
    if Questionario.objects.filter(id=id).count() > 0:
        questionario = Questionario.objects.get(id=id)
        questoes = Questao.objects.filter(questionario=questionario)
        opcoes = Opcao.objects.filter(questao__in=questoes)

    if request.method == 'POST':
        certas = 0
        total = 0
        for questao in questoes:
            if Opcao.objects.filter(questao=questao).count() <= 0:
                continue
            resposta = request.POST[str(questao.id)]
            if Resposta.objects.filter(usuario=request.user).filter(questao=questao).count() > 0:
                r = Resposta.objects.filter(
                    usuario=request.user).filter(questao=questao)
                rr = r[0]
                rr.resposta = resposta
                rr.save()
            else:
                r = Resposta(questao=questao, resposta=resposta,
                             usuario=request.user)
                r.save()
            if int(resposta) == questao.correta.id:
                certas += 1
            total += 1
        nota = (certas * 100)/total
        if Nota.objects.filter(usuario=request.user).filter(questionario=questionario).count() > 0:
            nF = Nota.objects.filter(usuario=request.user).filter(
                questionario=questionario)
            n = nF[0]
            n.nota = nota
            n.save()
        else:
            n = Nota(usuario=request.user, nota=nota,
                     questionario=questionario)
            n.save()

    c = {
        'questionario': questionario,
        'questoes': questoes,
        'opcoes': opcoes,
    }
    return render(request, 'questao/ver_questao.html', c)


def ver_nota(request, idQuestionario):

    #total - x
    #certas - y
    #y = (certas * x)/total
    questionario = Questionario.objects.get(id=idQuestionario)
    n = Nota.objects.filter(usuario=request.user).filter(
        questionario=questionario)
    c = {
        'nota': nota,
    }
    return render(request, 'questao/ver_nota.html', c)


def ver_questionarios(request):
    questionarios = Questionario.objects.all()
    notas = Nota.objects.filter(usuario=request.user).filter(
        questionario__in=questionarios)

    # 1: {
    #       'questionarios': questionarios,
    #      'nota': notas,
    # }
    a = {

    }
    s = 0
    for questionario in questionarios:
        nota = None
        if notas.filter(questionario=questionario).count() > 0:
            nota = notas.get(questionario=questionario)

        a[str(s)] = {
            'questionarios': questionario,
            'nota': nota,
        }
        s += 1
    tamanho = (len(a))
    c = {
        'questionarios': questionarios,
        'a': a,
        'tamanho': range(tamanho),
        'notas': notas,
    }
    return render(request, 'questao/ver_questionarios.html', c)
# cadastrar


def cadastrar_questionario(request):

    if request.method == 'POST':

        f = QuestionarioForm(request.POST)
        if f.is_valid():
            f.save()
        return redirect('cadastrar_questionario')
    form = QuestionarioForm()
    c = {
        'form': form,
    }
    return render(request, 'questao/cadastrar/cadastrar_questionario.html', c)


class cadastrar_questao(BSModalCreateView):
    template_name = 'questao/cadastrar/cadastrar_questao.html'
    form_class = QuestaoForm
    success_message = 'Success: Book was created.'

    def get_success_url(self):
        # return reverse_lazy('update_questionario', kwargs={'idQuestionario' : self.idQuestionario})
        return redirect('update_questionario', self.idQuestionario)

    def dispatch(self, *args, **kwargs):
        self.idQuestionario = kwargs['idQuestionario']

        return super(cadastrar_questao, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        if not self.request.is_ajax():
            quest = Questionario.objects.get(id=self.idQuestionario)
            a = form.save(commit=False)
            a.questionario = quest
            a.save()
            form.save_m2m()

        return (self.get_success_url())
        # return redirect('update_questionario', self.idQuestionario)#HttpResponseRedirect(reverse_lazy('update_questionario', kwargs={'idQuestionario' : self.idQuestionario}))


class cadastrar_opcao(BSModalCreateView):
    template_name = 'questao/cadastrar/cadastrar_opcao.html'
    form_class = OpcaoForm
    success_message = 'Success: Book was created.'

    def get_success_url(self):
        # return reverse_lazy('update_questionario', kwargs={'idQuestionario' : self.idQuestionario})
        return redirect('update_questao', self.idQuestionario, self.idQuestao)

    def dispatch(self, *args, **kwargs):
        self.idQuestionario = kwargs['idQuestionario']
        self.idQuestao = kwargs['idQuestao']

        return super(cadastrar_opcao, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        if not self.request.is_ajax():
            questao = Questao.objects.get(id=self.idQuestao)
            a = form.save(commit=False)
            a.questao = questao
            a.save()
            form.save_m2m()

        return (self.get_success_url())


# ver cadastro

@login_required
def cadastrar_ver_questionario(request):
    questionarios = Questionario.objects.all()
    if request.method == 'POST':

        f = QuestionarioForm(request.POST)
        if f.is_valid():
            f.save()
        return redirect('cadastrar_ver_questionario')
    form = QuestionarioForm()
    c = {
        'questionarios': questionarios,
        'form': form,
    }
    return render(request, 'questao/cadastrar/ver/cadastrar_ver_questionarios.html', c)

# update


def update_questionario(request, idQuestionario):

    questionario = None
    questoes = None
    if Questionario.objects.filter(id=idQuestionario).count() > 0:
        questionario = Questionario.objects.get(id=idQuestionario)
        questoes = Questao.objects.filter(questionario=questionario)

    if request.method == 'POST':
        form = QuestionarioForm(request.POST, instance=questionario)
        if form.is_valid():
            form.save()
        return redirect('update_questionario', idQuestionario)
    form = QuestionarioForm(instance=questionario)

    c = {
        'questionario': questionario,
        'questoes': questoes,
        'form': form,
    }

    return render(request, 'questao/cadastrar/update/cadastrar_update_questionario.html', c)


def update_questao(request, idQuestionario, idQuestao):
    questao = Questao.objects.get(id=idQuestao)
    questionario = Questionario.objects.get(id=idQuestionario)
    opcoes = Opcao.objects.filter(questao=questao)
    if request.method == 'POST':
        f = QuestaoFormUpdate(request.POST, instance=questao)
        if f.is_valid():
            f.save()

        return redirect('update_questao', idQuestionario, idQuestao)
    form = QuestaoFormUpdate(instance=questao)
    form.fields['correta'].queryset = Opcao.objects.filter(questao=questao)
    c = {
        'questionario': questionario,
        'questao': questao,
        'opcoes': opcoes,
        'form': form,
    }

    return render(request, 'questao/cadastrar/update/cadastrar_update_questao.html', c)


# delete


def delete_questionario(request, idQuestionario):
    questionario = Questionario.objects.get(id=idQuestionario)
    if request.method == 'POST':
        questionario.delete()
        return redirect('cadastrar_ver_questionario')
    c = {
        'nome': questionario.nome,

    }
    return render(request, 'questao/delete_confirm.html', c)
