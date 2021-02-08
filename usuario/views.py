from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from usuario.forms import (
    UserFormLogin,
    UserFormRegister,
)

from django.conf import settings

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        usuario = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if usuario != None:
            login(request, usuario)
            if usuario.tipo == 1:
                return redirect('home_usuario')
            elif usuario.tipo == 2:
                return redirect('home')

        return redirect('login')

    form = UserFormLogin()
    c = {
        'form': form,
    }
    return render(request, 'usuario/login/login.html', c)


def register(request):
    if request.method == 'POST':
        f = UserFormRegister(request.POST)
        if f.is_valid():
            f.save()
        return redirect('login_view')
    form = UserFormRegister()
    c = {
        'form': form,
    }
    return render(request, 'usuario/register/register.html', c)


def usuario_logout(request):
    logout(request)
    return redirect('login_view')
