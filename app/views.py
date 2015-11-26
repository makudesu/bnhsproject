from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import CustomUser

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class CustomUserUpdate(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ('first_name', 'middle_name', 'last_name', 'date_of_birth', 'sex',)

    def get_queryset(self):
        return CustomUser.objects.filter(email=self.request.user)

class CustomUserList(LoginRequiredMixin, ListView):
    model = CustomUser

    def get_queryset(self):
        return CustomUser.objects.filter(email=self.request.user)

class CustomUserDetail(LoginRequiredMixin, DetailView):
    model = CustomUser

    def get_queryset(self):
        return CustomUser.objects.filter(email=self.request.user)
