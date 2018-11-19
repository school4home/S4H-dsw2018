from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.views import View
from user.forms import LoginForm

def index(request, login_form=LoginForm()):
    if hasattr(request, 'user') and request.user.is_authenticated:
        return render(request, 'S4H/home.html', {})
    else:
        return render(request, 'S4H/index.html', {'form': login_form})
