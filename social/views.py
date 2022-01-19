from django.views.generic import ListView
from django.shortcuts import render
from social import models
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class Wall(LoginRequiredMixin, ListView):
    queryset = models.Post.objects.all()
    context_object_name = 'posts' #this is to send values named posts
    template_name = 'social/wall.html'
    login_url = 'auth/login'




