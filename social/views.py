from http.client import HTTPResponse
from msilib.schema import Error
from urllib.error import HTTPError
from django.views import View
from django.views.generic import ListView 
from django.shortcuts import render , redirect
from social import models ,forms 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q 
from django.views.generic.detail import SingleObjectMixin

# Create your views here.
class Wall(LoginRequiredMixin, ListView):
    #queryset = models.Post.objects.all()  #now we need to filter that
    context_object_name = 'posts' #this is to send values named posts
    template_name = 'social/wall.html'
    login_url = 'auth/login'

    def get_queryset(self) :
      friendids = [ friend.person2.id for friend in models.Friends.objects.filter(person1 = self.request.user)]
      friendids = friendids + [ friend.person1.id for friend in models.Friends.objects.filter(person2 = self.request.user)]
      return models.Post.objects.filter(user__in = friendids).order_by('-created_at')
      '''
        return  models.Post.objects.filter(
          (Q(user__person1 = self.request.user.pk) | Q(user__person2 = self.request.user.pk))
          & ~Q(user = self.request.user)
            ).order_by('-created_at')
      '''

class Home(LoginRequiredMixin , ListView):
    context_object_name = 'posts'
    template_name = 'social/home.html'
    login_url = 'auth/login'
    def get_queryset(self):
        return models.Post.objects.filter(user = self.request.user.pk
        ).order_by('-created_at')
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
      

class PostLike(  View):
  model = models.Post

  def post(self , request ,pk) :
    post = self.model.objects.get(pk = pk )
    models.Likes.objects.create(post= post , user = request.user )    
    return HTTPResponse(code = 204)

class PostComment(View):
  pass 



