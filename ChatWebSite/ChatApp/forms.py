from django import forms
from django.contrib.auth.models import User

from .models import Chat, Messages


class CreatedChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['name', 'author']
        widgets = {
            'author': forms.HiddenInput()
        }


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['text', 'author', 'chat']
        widgets = {
            'author': forms.HiddenInput(),
            'chat': forms.HiddenInput(),
        }
        labels = {
            'text': ''
        }

class AddUserToChatForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    chat_id = forms.IntegerField(widget=forms.HiddenInput())