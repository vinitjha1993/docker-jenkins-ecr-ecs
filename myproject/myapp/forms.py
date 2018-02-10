from django import forms
from django.contrib.auth.forms import UserCreationForm  #using inbuilt forms of django
from django.contrib.auth.models import User             #using inbuilt models of django


class SignUpForm(UserCreationForm):    #creating extra fields and applying bootstrap here for registration page
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'user_name'}))

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'first_name'}))

    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'last_name'}))

    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'email'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'confirm_password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )







