from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from .models import User
from .forms import UserForm
from django.urls import reverse_lazy
from django.views import View

# Create your views here.

class Users(ListView):
    model = User
    template_name = "accounts/account_list.html"
    context_object_name = "users"

class Home(ListView):
    model = User
    template_name = "accounts/account_home.html"
    context_object_name = "users"

class novo(CreateView):
    model = User
    form_class = UserForm
    template_name = "accounts/add.html"
    success_url = reverse_lazy('users')

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'  
    redirect_authenticated_user = True     