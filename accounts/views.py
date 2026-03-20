from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import signupform, loginform,ProfileForm
from django.contrib.auth.decorators import login_required
from .models import BlogUser

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

                return redirect('all_posts')

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



@login_required
def user_profile(request):
    profile, created = BlogUser.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'User_Profile.html', {
        'profile': profile,
        'form': form
    })



@login_required
def edit_profile(request):
    # Get or create the profile for the logged-in user
    profile, created = BlogUser.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            # Redirect to the profile page after saving
            return redirect('profile')  # <-- use the correct URL name from urls.py
        else:
            print(form.errors)  # Shows form errors in console
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'Edit_Profile.html', {'form': form})