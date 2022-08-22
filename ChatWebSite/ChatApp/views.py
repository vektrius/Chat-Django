import logging

from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.decorators.http import require_http_methods
from django.views.generic import DetailView
from guardian.shortcuts import assign_perm

from .forms import CreatedChatForm, SendMessageForm, AddUserToChatForm
from .models import Chat
from ChatWebSite.settings import CHAT_VIEW_PERMISSION


# Create your views here.


class ChatsView(View):
    def get(self, request):
        created_chat_form = CreatedChatForm(initial={'author': request.user})
        context = {
            'created_chat_form': created_chat_form
        }
        return render(request, 'chat/chats.html', context)

    def post(self, request):
        created_chat_form = CreatedChatForm(request.POST)
        if created_chat_form.is_valid():
            chat = created_chat_form.save()
            user = request.user
            chat.members.add(user)
            assign_perm(CHAT_VIEW_PERMISSION, user, chat)

        context = {
            'created_chat_form': created_chat_form
        }
        return render(request, 'chat/chats.html', context)


class ChatDetailView(DetailView):
    model = Chat
    template_name = 'chat/chat.html'
    context_object_name = 'chat'
    def get(self, request, *args, **kwargs):
        response = super(ChatDetailView, self).get(request, *args, **kwargs)
        user = request.user
        if not user.has_perm(CHAT_VIEW_PERMISSION, self.object):
            return HttpResponseForbidden('No access')
        return response

    def get_context_data(self, **kwargs):
        context = super(ChatDetailView, self).get_context_data()

        context['message_form'] = SendMessageForm(initial={
            'author': self.request.user,
            'chat': self.object
        })

        if self.object.author == self.request.user:
            context['add_user_to_chat_form'] = AddUserToChatForm(initial={
                'chat_id': self.object.pk
            })

        context['messages'] = self.object.messages.all().select_related('author').values('text', 'author__username','date_created').order_by('date_created')

        return context

    # @staticmethod
    # @require_http_methods(['POST'])
    # def send_message_to_chat(request):
    #     message_form = SendMessageForm(request.POST)
    #
    #     if message_form.is_valid():
    #         message_form.save()
    #
    #     context = {
    #         'message_form': message_form
    #     }
    #     chat_pk = message_form.cleaned_data['chat'].pk
    #     return HttpResponseRedirect(reverse('chat', kwargs={'pk': chat_pk}))

    @staticmethod
    @require_http_methods(['POST'])
    def add_user_to_chat(request,chat_id):
        add_user_to_chat_form = AddUserToChatForm(request.POST)

        if add_user_to_chat_form.is_valid():
            user = add_user_to_chat_form.cleaned_data['user']
            chat = Chat.objects.filter(pk=chat_id).first()
            chat.members.add(user)
            assign_perm(CHAT_VIEW_PERMISSION, user,chat)

        print(add_user_to_chat_form.errors)
        return HttpResponseRedirect(reverse('chat', kwargs={'pk': chat_id}))
# TODO На завтра добавить django-chanels и сделать чат
