from django.contrib import admin
from django.urls import path, include

from usuario.views import (
    login_view,
    register,
    usuario_logout,
)

urlpatterns = [
    path('login', login_view, name='login_view'),
    path('register', register, name='register'),
    path('logout', usuario_logout, name='usuario_logout'),
]
