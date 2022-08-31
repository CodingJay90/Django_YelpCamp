import json
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import QueryDict

# Create your views here.


def register_view(request):
    print(request.method)
    if request.method == "POST":
        q_dict = QueryDict(request.body, mutable=True)
        username = q_dict.get('username')
        password = q_dict.get('password')
        user = User.objects.create_user(username, '', password)
        user.save()
        login(request, user)
        return redirect('campgrounds:home')
    return render(request, 'accounts/register.html')


def login_view(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/login.html')
