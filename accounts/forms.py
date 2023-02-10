from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import *
from django.contrib.auth.models import User
from django import forms
from .models import *


class register(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]



class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ["file"]