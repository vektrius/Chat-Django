import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from ChatApp.models import Chat, Messages


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.chat_pk = self.scope['url_route']['kwargs']['chat_id']
        self.chat_group_name = f'chat{self.chat_pk}'
        async_to_sync(self.channel_layer.group_add)(
            self.chat_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.chat_group_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        data_dict = json.loads(text_data)
        user = self.scope['user']
        message_text = data_dict['message']
        chat = Chat.objects.filter(pk=self.chat_pk).first()
        Messages.objects.create(text=message_text,
                                chat=chat,
                                author=user)
        async_to_sync(self.channel_layer.group_send)(
            self.chat_group_name,
            {
                'type' : 'send_message_to_chat',
                'message_text' : message_text,
                'username_author' : user.username
            }
        )

    def send_message_to_chat(self,event):
        message_text = event['message_text']
        author = event['username_author']
        self.send(text_data=json.dumps({
            'message' : message_text,
            'author' : author,
        }))


