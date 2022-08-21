from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Chat(models.Model):
    author = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='chats')
