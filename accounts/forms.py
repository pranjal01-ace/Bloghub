from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import BlogUser

class signupform(UserCreationForm):
    password2 = forms.CharField(max_length=100,label='Confirm Password',widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    password1 = forms.CharField(max_length=100,label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email','password1', 'password2']
        labels = {
            'username': 'Username',
            'first_name': 'Name',
            'email': 'Email',
        }
        
class loginform(AuthenticationForm):
    username = forms.CharField(max_length=100,label='Username',widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=100,label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
      
      
from django import forms
from .models import BlogUser

class ProfileForm(forms.ModelForm):
    class Meta:
        model = BlogUser
        fields = ['role', 'bio', 'profile_image', 'date_of_birth', 'website']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }