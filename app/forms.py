from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'middle_name', 'last_name', 'date_of_birth', 'sex',)

class CustomUserChangeForm(UserChangeForm):
    
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'middle_name', 'last_name', 'date_of_birth', 'sex',)
    
class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={'placeholder':('First Name'), 'autofocus': 'autofocus'}))
    middle_name = forms.CharField(max_length=30, label='Middle Name', widget=forms.TextInput(attrs={'placeholder':('Middle Name')}))
    last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={'placeholder':('Last Name')}))
    
    def signup(self, request, CustomUser):
        CustomUser.first_name = self.cleaned_data['first_name']
        CustomUser.middle_name = self.cleaned_data['middle_name']
        CustomUser.last_name = self.cleaned_data['last_name']
        CustomUser.save()
