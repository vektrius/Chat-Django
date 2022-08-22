from django.urls import path

from .views import ChatsView, ChatDetailView

urlpatterns = [
    path('', ChatsView.as_view(), name='chats'),
    path('<int:pk>/', ChatDetailView.as_view(),name='chat'),
    path('add-user-to-chat/<int:chat_id>/',ChatDetailView.add_user_to_chat,name='add-user-to-chat'),
]