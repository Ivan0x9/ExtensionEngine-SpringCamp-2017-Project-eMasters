from django.shortcuts import render, redirect ,reverse
from registration.backends.simple.views import RegistrationView
from registration.forms import forms
from django.contrib.auth.decorators import login_required, user_passes_test
from courses.views import CreateView
from courses.models import *
from .forms import *



def home(request):
    context = {
        "title": "EMasters",
        }

    return render(request, "users/home.html", context)


