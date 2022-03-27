from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core import validators
from captcha.fields import CaptchaField, CaptchaTextInput


class RegisterUserForm(ModelForm):
    username = forms.CharField(
        help_text='', min_length='2', validators=[validators.validate_slug], max_length='15', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    email = forms.CharField(
        help_text='', min_length='5', validators=[validators.validate_email], max_length='30', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(
        help_text='', min_length='8', validators=[validators.validate_slug], max_length='25', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(
        help_text='', validators=[validators.validate_slug], widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтверждение пароля'}))

    class CustomCaptchaTextInput(CaptchaTextInput):
        template_name = 'captchas/captcha_signup.html'

    captcha = CaptchaField(widget=CustomCaptchaTextInput(
        attrs={'class': 'form-control', 'placeholder': 'Капча'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].required = True

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise ValidationError('Пользователь с таким Email уже существует')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError('Пароли не совпадают')
        return password2


class UserRewiwesForm(ModelForm):
    title = forms.CharField(min_length='6', max_length='50', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Тема(Заголовок)'}))
    rewiew = forms.CharField(min_length='10', max_length='1000', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Текст отзыва'}))

    def __init__(self, *args, **kwargs):
        super(UserRewiwesForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].required = True

    class Meta:
        model = Reviews
        fields = ('title', 'rewiew',)
