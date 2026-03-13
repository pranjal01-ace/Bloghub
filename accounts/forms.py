from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email','password1', 'password2']
        labels = {
            'username': 'Username',
            'first_name': 'Name',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password'
        }
        
