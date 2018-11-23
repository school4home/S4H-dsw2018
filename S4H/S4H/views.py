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
        all_grades = request.user.s4h_user.grade_set.all()
        for grade in all_grades:
            if grade.grade_observer.message != '':
                messages.add_message(request, grade.grade_observer.message_type, grade.grade_observer.message)
                grade.grade_observer.clear()
        return render(request, 'S4H/home.html', {})
    else:
        return render(request, 'S4H/index.html', {'form': login_form})
