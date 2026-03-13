from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from httpx import request
from .forms import signupform
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = signupform()
    
    return render(request, 'register.html', {'form': form})

# def login(request):
#     fm=loginform()  
#     return render(request, 'login.html', {'form': fm}) 