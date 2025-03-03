from django import forms
from .models import Comments
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text', 'username', 'day')
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Напишите текст'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}),
            'day': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

class RegisterForm(UserCreationForm):
    captcha = ReCaptchaField()
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}))
    class Meta:
        model = User
        fields = ('username', 'last_name', 'password1', 'password2', 'captcha')
