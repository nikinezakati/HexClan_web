from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from User.models import user
from django import forms
from .models import *


class SignupForm(UserCreationForm):
    class Meta:
        model = user
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
