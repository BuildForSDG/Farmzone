# Create your views here.
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import NewUserForm

User = get_user_model()


def about(request):
    return render(request, 'aboutus.html')


def blog(request):
    return render(request, 'blog.html')


def faqs(request):
    return render(request, 'faqs.html')
