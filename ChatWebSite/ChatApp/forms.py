from django.forms import ModelForm, HiddenInput

from .models import Chat, Messages


class CreatedChatForm(ModelForm):
    class Meta:
        model = Chat
        fields = ['name','author']
        widgets = {
            'author' : HiddenInput()
        }



class MessageForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['text','author','chat']
        widgets = {
            'author' : HiddenInput(),
            'chat' : HiddenInput(),
        }
        labels = {
            'text' : ''
        }