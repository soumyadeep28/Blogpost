from django.views import View
from django.views.generic import ListView
from django.shortcuts import render
from social import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q 
# Create your views here.
class Wall(LoginRequiredMixin, ListView):
    #queryset = models.Post.objects.all()  #now we need to filter that
    context_object_name = 'posts' #this is to send values named posts
    template_name = 'social/wall.html'
    login_url = 'auth/login'

    def get_queryset(self) :
        return  models.Post.objects.filter(
          (Q(user__person1 = self.request.user.pk) | Q(user__person2 = self.request.user.pk))
          & ~Q(user = self.request.user)
            )

class Home(LoginRequiredMixin , ListView):
    context_object_name = 'posts'
    template_name = 'social/home.html'
    login_url = 'auth/login'
    def get_queryset(self):
        return models.Post.objects.filter(user = self.request.user.pk
        )



