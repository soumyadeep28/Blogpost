from django.shortcuts import render
from django.contrib.auth.views import LoginView , LogoutView
from django.views import View
from django.contrib.auth.forms import UserCreationForm  # we are not using basic one we are updating that 
from auth import forms
# Create your views here.



class Login(LoginView):
    template_name = 'auth/index.html'
    redirect_authenticated_user = True

class Logout(LogoutView):
    pass 

class Signup(View):
    def get(self , request  ):
        context = {
            'form' :forms.Signupform()
        }
        return render(request , 'auth/signup.html' , context)
    
