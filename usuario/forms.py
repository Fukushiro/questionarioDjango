from django import forms
from usuario.models import (
    custom_user,
)


class UserFormLogin(forms.ModelForm):
    class Meta:
        model = custom_user
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class UserFormRegister(forms.ModelForm):
    class Meta:
        model = custom_user
        fields = ['username', 'email', 'password', 'tipo']

        widgets = {
            'tipo': forms.Select(choices=[(1, 'usuario'), (2, 'cadastrador')]),
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        instance = super(UserFormRegister, self).save(commit=False)
        instance.set_password(self.cleaned_data['password'])

        if commit:
            instance.save()
        return instance
