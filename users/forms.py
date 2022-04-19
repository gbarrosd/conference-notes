from django import forms
from logging import raiseExceptions
from localflavor.br.forms import BRCNPJField

from .models import (
    CustomUser,
)

class formUser(forms.ModelForm):
    cnpj = BRCNPJField()

    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de senha', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser

        fields = (
            'first_name',
            'last_name',
            'cnpj',
            'is_superuser',
            'password1',
            'password2',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não combinam!")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.username = user.cnpj
        if commit:
            user.save()
        return user

class UpdateUser(forms.ModelForm):
    cnpj = BRCNPJField()

    class Meta:
        model = CustomUser

        fields = (
            'first_name',
            'last_name',
            'cnpj',
            'is_superuser',
        )

class UpdateUserPassword(forms.ModelForm):

    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de senha', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser

        fields = (
            'password1',
            'password2',
        )

        def clean_password2(self):
            password1 = self.cleaned_data.get("password1")
            password2 = self.cleaned_data.get("password2")
            if password1 and password2 and password1 != password2:
                raise forms.ValidationError("As senhas não combinam!")
            return password2

        def save(self, commit=True):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data["password1"])
            if commit:
                user.save()
            return user

