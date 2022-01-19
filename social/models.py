from django.db import models

# Create your models here.

from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now= True)
    content = models.TextField()
    image = models.ImageField() #for image need to install pillow

    def __str__(self) -> str:
        return '{}_post{}_{}..'.format(self.user , self.pk , self.content[:10])

class Likes(models.Model):
    post = models.ForeignKey('Post' ,on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

class comment(models.Model):
    post = models.ForeignKey('Post' ,on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    content = models.CharField(max_length=1024 )



class Friends(models.Model):
    person1 = models.ForeignKey(User , on_delete=models.CASCADE , related_name='person1')
    person2 = models.ForeignKey(User , on_delete=models.CASCADE , related_name='person2')
    #so if a and b are friend then they are friend with each other 
