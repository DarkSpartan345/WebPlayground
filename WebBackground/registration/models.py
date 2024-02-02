from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

def custom_upload_profile(instance,filename):
    old_instance=Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return "profile"+filename

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    avatar=models.ImageField(null=True,blank=True,upload_to=custom_upload_profile)
    bio= models.TextField(null=True,blank=True)
    link=models.URLField(null=True,blank=True,max_length=200)
    class Meta:
        ordering=["user__username"]
 
@receiver(post_save,sender=User)    
def ensure_profile_exists(sender,instance,**kwargs):
    if kwargs.get("created",False):
        Profile.objects.get_or_create(user=instance)
        #print("se ha creado existosamente el usuario y perfil enlazado")
    
