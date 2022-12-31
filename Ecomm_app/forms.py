from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordResetForm
from .models import *
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    Email = forms.CharField(label="Email",widget=forms.EmailInput(attrs={"autofocus":"True","class":"form-control"}))
    password1 = forms.CharField(label="Password1",widget=forms.PasswordInput(attrs={"autocomplete":"current-password","class":"form-control"}))

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"autofocus": "True", "class": "form-control"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(
        attrs={"class": "form-control"}))
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput(
        attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    
    
class PasswordResetForm(PasswordResetForm):
    pass
