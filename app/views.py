from django.shortcuts import render, redirect
from django.views.generic import CreateView, View
from django.contrib import messages

from .forms import  CustomUserCreationForm
from .models import CustomUser

class HomePageView(View):
    template_name = 'userapp/index.html'

    def get(self, request):
        return render(request, self.template_name)
