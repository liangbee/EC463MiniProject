from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    number_of_rooms = forms.IntegerField(help_text='Enter the number of rooms in your household', min_value=1)
