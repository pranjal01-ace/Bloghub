from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import signupform, loginform
from django.contrib.auth.decorators import login_required

# ---------------- REGISTER ---------------- #

def register(request):
    if request.method == 'POST':
        form = signupform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')   # redirect to login after signup

    else:
        form = signupform()

    return render(request, 'Register.html', {'form': form})


# ---------------- LOGIN ---------------- #

def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # redirect to dashboard if already logged in
    if request.method == 'POST':

        # AuthenticationForm requires request object
        form = loginform(request, data=request.POST)

        if form.is_valid():

            print("FORM VALID")

            uname = form.cleaned_data['username']
            pword = form.cleaned_data['password']

            user = authenticate(request, username=uname, password=pword)

            if user is not None:
                print("LOGIN SUCCESS")

                login(request, user)

                return redirect('dashboard')

            else:
                print("AUTH FAILED")

        else:
            print(form.errors)

    else:
        form = loginform()

    return render(request, 'login.html', {'form': form})


# ---------------- LOGOUT ---------------- #

def user_logout(request):
    logout(request)
    return redirect('login')


def user_profile(request):
    return render(request, 'User_Profile.html')