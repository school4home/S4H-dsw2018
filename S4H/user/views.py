from django.shortcuts import render, redirect
from .forms import PasswordForm
from .forms import UserForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import S4HUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.views import View

class NewUserView(FormView):
    template_name = "user/newUser.html"
    form_class = UserForm
    success_url = "/"

    def form_valid(self, form):
        form.insert()
        messages.success(self.request, 'Voce foi cadastrado')
        return super(NewUserView, self).form_valid(form)
