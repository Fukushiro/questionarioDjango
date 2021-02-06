from django.shortcuts import render
from usuario.forms import UserFormLogin
# Create your views here.


def login(request):

    form = UserFormLogin()
    c = {
        'form': form,
    }
    return render(request, 'usuario/login/login.html', c)
