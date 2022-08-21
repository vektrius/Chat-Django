from django.urls import path

from .views import ChatsView, ChatDetailView

urlpatterns = [
    path('', ChatsView.as_view(), name='chats'),
    path('<int:pk>/', ChatDetailView.as_view(),name='chat')
]