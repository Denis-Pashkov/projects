from .models import *
from django.forms import ModelForm, PasswordInput, TextInput
from django.contrib.auth.models import User


class RegisterUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя',
                'label': '1',
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            }),
        }
# https://www.youtube.com/watch?v=QK4qbVyY7oU&list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F&index=26&ab_channel=selfedu
