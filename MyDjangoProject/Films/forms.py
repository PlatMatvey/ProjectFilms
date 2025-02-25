from django import forms
from .models import Comments
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')