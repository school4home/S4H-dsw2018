from django.shortcuts import render, redirect
from .forms import PasswordForm
from .forms import UserForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import S4HUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.views import View
from S4H.views import index

class NewUserView(FormView):
    template_name = "user/newUser.html"
    form_class = UserForm
    success_url = "/"

    def form_valid(self, form):
        form.insert()
        messages.success(self.request, 'Voce foi cadastrado')
        return super(NewUserView, self).form_valid(form)

class LoginView(FormView):
    template_name = "user/newUser.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        user = form.authenticate_user()
        login(self.request, user)
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        return index(self.request, login_form=form)

    def get(self, request, *args, **kwargs):
        return redirect('index')

def logout_user(request):
    if hasattr(request, 'user') and isinstance(request.user, User):
        logout(request)
        messages.success(request, 'Voce foi deslogado com sucesso!')
    return redirect('index')


def delete_user(request):
    if request.user.is_authenticated():
        request.user.delete()
        logout(request)
        return index(request)
    else:
        return index(request)
