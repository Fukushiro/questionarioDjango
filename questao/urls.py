from django.contrib import admin
from django.urls import path
from questao.views import (
    ver_questao,
    ver_nota,
    cadastrar_questionario,
    cadastrar_questao,
    cadastrar_ver_questionario,
    update_questionario,
    update_questao,
    cadastrar_opcao,
    home,
    home_usuario,
    ver_questionarios,
    delete_questionario,

)
from questao import views

urlpatterns = [
    path('home', home, name='home'),
    path('home_usuario', home_usuario, name='home_usuario'),
    path('ver/<int:id>', ver_questao, name='ver_questao'),
    path('ver/nota/<int:idQuestionario>', ver_nota, name='ver_nota'),
    path('ver/questionarios', ver_questionarios, name='ver_questionarios'),
    # cadastros
    path('cadastrar/questionario', cadastrar_questionario,
         name='cadastrar_questionario'),
    path('cadastrar/questionario/<int:idQuestionario>/questao',
         cadastrar_questao.as_view(), name='cadastrar_questao'),
    path('cadastrar/questionario/<int:idQuestionario>/questao/<int:idQuestao>/opcao',
         cadastrar_opcao.as_view(), name='cadastrar_opcao'),
    # visualizações
    path('cadastrar/ver/questionario', cadastrar_ver_questionario,
         name='cadastrar_ver_questionario'),

    # update
    path('update/questionario/<int:idQuestionario>',
         update_questionario, name='update_questionario'),
    path('update/questionario/<int:idQuestionario>/questao/<int:idQuestao>',
         update_questao, name='update_questao'),
    # delete
    path('delete/questionario/<int:idQuestionario>',
         delete_questionario, name='delete_questionario'),

]
