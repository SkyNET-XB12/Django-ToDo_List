
from django.contrib.auth.models import User
from django.shortcuts import render
 
from django.http import HttpResponse, HttpResponseRedirect
import datetime

# imports the forms
# imports the forms
from . import forms as portal_forms 
# Create your views here.

def login_template (request):
    # Lets ensure it's a GET request
    return render (request, "login.html")

def register_template (request):
    # Let's ensure it's a GET request 
    return render (request, "register.html")

def login ():
    # Accepts username and 
    # password during logins for authentications (are you who you said you are?👀)
    return

def register (request):
    # Accepts username
    # Accepts password
    if (request.method == "POST"):
        register_form = portal_forms.RegisterForm(request.POST)
        # Here, we verify whether the form is valid
        if (register_form.is_valid()):
            return HttpResponseRedirect("account/login")
    
    return render (request, "login.html",{"register_form": register_form})
