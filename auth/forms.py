
from django import forms

class LoginForm (forms.Form):
    pass

class RegisterForm (forms.Form):
    username = forms.CharField(label = "User Name", max_length = 150)
    password = forms.CharField (max_length = 256)

