from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed

class Message(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=["created"]
        
class ThereadManager(models.Manager):
    
    def find(self,user1,user2):
        queryset=self.filter(users=user1).filter(users=user2)
        if len(queryset)>0:
            return queryset[0]
        return None
    def find_or_create(self,user1,user2):
            thread=self.find(user1,user2)
            if thread is None:
                thread=Thread.objects.create()
                thread.users.add(user1,user2)
            return thread
class Thread(models.Model):
    
    users=models.ManyToManyField(User,related_name="threads")
    message=models.ManyToManyField(Message)
    objects=ThereadManager()
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=["-updated"]
        

def message_change(sender,**kwargs):
    instance=kwargs.pop("instance",None)
    action=kwargs.pop("action",None)
    pk_set=kwargs.pop("pk_set",None)
    false_pk_set=set()
    print(instance,action,pk_set)
    if action is "pre_add":
        for msg_pk in pk_set:
            msg=Message.objects.get(pk=msg_pk)
            if msg.user not in instance.users.all():
                print("el usuario ({}) no deberia estar en este hilo".format(msg.user))
                false_pk_set.add(msg_pk)
    # buscamos mensaje que se encuentren en false_pk_set y los borramos de pk_set
    pk_set.difference_update(false_pk_set)
    instance.save()
    
m2m_changed.connect(message_change,sender=Thread.message.through)