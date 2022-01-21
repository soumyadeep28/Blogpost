from django import forms 
from social import models 

class FormPost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['content' , 'image']

