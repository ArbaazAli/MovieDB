from django import forms
from django.core import validators

class SignupForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, validators = [validators.MinLengthValidator(6)])
    confirm_password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)
