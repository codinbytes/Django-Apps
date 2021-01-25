from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/dashboard")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "login.html", {"form": form, "msg" : msg})

def register_user(request):

        

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        print(form)

        if form.is_valid():
            form.save()
            msg     = 'User created.'
            success = True              
            return redirect('/login')

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "register.html", {"form": form, "msg" : msg, "success" : success })


