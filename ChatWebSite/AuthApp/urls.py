from django.urls import path
from .views import RegistrationView, LoginView, logout_user

urlpatterns = [
    path('registration/',RegistrationView.as_view(),name='registration'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',logout_user,name='logout')
]