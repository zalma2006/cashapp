from django.shortcuts import render
from .models import *
from django.views.generic import DetailView, ListView
from django.forms import Form
# Create your views here.


class UserView(ListView):
    model = Users


class BanksView(ListView):
    model = Banks
    context_object_name = 'users'
