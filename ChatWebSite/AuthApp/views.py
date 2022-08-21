from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from .forms import RegistrationForm, LoginForm

def not_auth_or_redirect(func):
    def wrapper(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponse('You Login') #TODO Redirect to chats
        return func(self,request,*args,**kwargs)
    return wrapper

class RegistrationView(View):
    @not_auth_or_redirect
    def get(self,request):
        registration_form = RegistrationForm()
        context = {
            'registration_form' : registration_form
        }
        return render(request,'auth/registration.html',context)
    @not_auth_or_redirect
    def post(self,request):
        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid():
            username = registration_form.cleaned_data['username']
            password = registration_form.cleaned_data['password']
            user = User.objects.create_user(username=username,password=password)
            login(request,user)
            return HttpResponse("Succes") #TODO Redirect To Chat

        context = {
            'registration_form': registration_form
        }
        return render(request,'auth/registration.html',context)


class LoginView(View):
    @not_auth_or_redirect
    def get(self,request):
        login_form = LoginForm()
        context = {
            'login_form' : login_form
        }
        return render(request,'auth/login.html',context)
    @not_auth_or_redirect
    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponse('Succes') #TODO Redirect to chats
            else:
                login_form.add_error(None,ValidationError('username or password not corrected'))

        context = {
            'login_form' : login_form
        }
        return render(request, 'auth/login.html', context)



