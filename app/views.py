from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib import messages

from .forms import  CustomUserChangeForm
from .models import CustomUser

class CustomUserUpdate(UpdateView):
    form = CustomUserChangeForm
    model = CustomUser
    fields = ('first_name', 'middle_name', 'last_name', 'date_of_birth', 'sex',)

class CustomUserDetail(DetailView):
    model = CustomUser
