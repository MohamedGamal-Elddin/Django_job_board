from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class Signup_Form(UserCreationForm):
    class Meta:      
        model=User
        fields=['username','email','password1','password2']

class User_Form(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

class Profile_Form(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['city','image','phone_number']
