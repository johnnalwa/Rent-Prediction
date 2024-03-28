
from django import forms
from .models import Users

class userForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'phone', 'email', 'username', 'password']  # Specify the fields you want to include in the form


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    
    

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)