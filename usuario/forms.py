from django import forms
from usuario.models import (
    custom_user,
)


class UserFormLogin(forms.ModelForm):
    class Meta:
        model = custom_user
        fields = ['username', 'password']
