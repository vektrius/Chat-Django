import logging

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView

from .forms import CreatedChatForm, MessageForm
from .models import Chat


# Create your views here.


class ChatsView(View):
    def get(self,request):
        created_chat_form = CreatedChatForm(initial={'author' : request.user})
        context = {
            'created_chat_form' : created_chat_form
        }
        return render(request,'chats/chat.html',context)

    def post(self,request):
        created_chat_form = CreatedChatForm(request.POST)
        if created_chat_form.is_valid():
            chat = created_chat_form.save()
            chat.members.add(request.user)
        context = {
            'created_chat_form': created_chat_form
        }
        return render(request, 'chats/chat.html', context)


class ChatDetailView(DetailView):
    model = Chat
    template_name = 'chat/chat.html'
    context_object_name = 'chat'

    def post(self,request,pk):
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            message_form.save()
        context = {
            'message_form' : message_form
        }

        return HttpResponseRedirect(reverse('chat',kwargs={'pk' : pk }))

    def get_context_data(self, **kwargs):
        context = super(ChatDetailView, self).get_context_data()
        context['message_form'] = MessageForm(initial={
            'author' : self.request.user,
            'chat' : self.object
        })
        context['messages'] = self.object.messages.all().select_related('author').values('text','author__username')

        return context

