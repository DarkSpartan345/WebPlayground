from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    avatar=models.ImageField(null=True,blank=True,upload_to="profiles")
    bio= models.TextField(null=True,blank=True)
    link=models.URLField(null=True,blank=True,max_length=200)
    
# Create your models here.
