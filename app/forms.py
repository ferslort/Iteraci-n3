from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FomRegister (UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'username', 'password1', 'password2']


class FormLogin (forms.Form):

    username = forms.CharField(
        label='Usuario',
        required=True
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput()
    )

class FormSupplier(forms.Form):
    razon = forms.CharField(max_length=100)
    address = forms.EmailField()
    phone = forms.CharField(max_length=10)
    email = forms.CharField(max_length=100)
