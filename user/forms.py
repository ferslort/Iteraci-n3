from django import forms

from django.contrib.auth.forms import UserCreationForm
from user.models import User


class FomRegister (UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'username',
                  'last_name', 'email', 'address', 'phone', 'age')

        USERNAME_FIELD = 'email'


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


class RegisterForm (forms.Form):

    pass
