# manager/forms.py
from django import forms
from .models import Note, Password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']

class PasswordForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ['website', 'username', 'password']
        
        
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
    