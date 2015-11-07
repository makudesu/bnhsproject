from django import forms
from django.contrib.auth import get_user_model
from .models import MyUser 

class SignupForm(forms.ModelForm):
    class Meta:
        model = get_user_model
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'sex', 'date_of_birth' ]

    def save(self, user):
        user.save()
