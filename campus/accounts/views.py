from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from django.db import models
from django.contrib.auth import get_user_model
from . import forms

# Create your views here.
class SignUp(CreateView):
    form_class=forms.UserCreateForm
    success_url=reverse_lazy('login')
    template_name='accounts/signup.html'
