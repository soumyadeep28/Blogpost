from dataclasses import field
from optparse import Option
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms

class Signupform(UserCreationForm):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    photo = forms.FileField(allow_empty_file=True)
    class Meta :
        model = User
        fields = ('firstname' , 'lastname' ,'username' , 'email' , 'password1' , 'password2' , 'photo')
