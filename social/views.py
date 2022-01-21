from msilib.schema import Error
from urllib.error import HTTPError
from django.views import View
from django.views.generic import ListView 
from django.shortcuts import render , redirect
from social import models ,forms 
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
    def get_context_data(self,*args ,  **kwargs):
        data = super().get_context_data(*args , **kwargs)
        data['post_form'] = forms.FormPost()
        return data 


class Post(View):
  def post(self , request) :
    form = forms.FormPost(request.POST , request.FILES)
    if form.is_valid():
      print(form)
      post = form.save(commit=False)
      post.user  = request.user 
      post.save()
      return redirect('/home/')
    else:
      return redirect('/')
      



