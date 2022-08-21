from django.contrib.auth.models import User
from django.db import models

# Create your models here.

def chat_avatar_path(instance, filename):
    return f'{instance.author.username}/{filename}'

class Chat(models.Model):
    name = models.CharField(max_length=100,verbose_name='Chat name')
    author = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='chats_created')
    members = models.ManyToManyField(to=User,related_name='user_chats')
    avatar = models.ImageField(upload_to=chat_avatar_path)


class Messages(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Author user')
    chat = models.ForeignKey(Chat,on_delete=models.CASCADE,verbose_name='Chat',related_name='messages')
    text = models.TextField(verbose_name='Text message')


