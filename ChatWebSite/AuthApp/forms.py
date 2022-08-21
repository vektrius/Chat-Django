from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):

    password_confirm = forms.CharField(max_length=128,label='Password confirm',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password']
        help_texts = {
            'username' : ''
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username = username).values('id').exists():
            raise ValidationError("Users is exists")
        return username

    def clean_password_confirm(self):
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']
        if password_confirm != password:
            raise ValidationError("Passwords don't match")
        return password_confirm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255,label='Username')
    password = forms.CharField(max_length=128,label='Password',widget=forms.PasswordInput)