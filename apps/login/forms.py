from django import forms
from .models import User

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=45, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=45, widget=forms.TextInput(attrs={'class': 'small-textinput', 'placeholder':'First'}), label="")
    last_name = forms.CharField(max_length=45, widget=forms.TextInput(attrs={'class': 'small-textinput', 'placeholder':'Last'}), label="")
    alias = forms.CharField(max_length=45, widget=forms.TextInput(attrs={'class': 'textinput', 'placeholder':'Alias'}), label="")
    email = forms.EmailField(max_length=45, widget=forms.TextInput(attrs={'class': 'textinput', 'placeholder':'Email'}), label="")
    password = forms.CharField(max_length=45, widget=forms.PasswordInput(attrs={'class': 'textinput', 'placeholder':'Password'}), label="")
    confirm_password = forms.CharField(max_length=45, widget=forms.PasswordInput(attrs={'class': 'textinput', 'placeholder':'Confirm Password'}), label="")
