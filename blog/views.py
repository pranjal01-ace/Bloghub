from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import date
# Create your views here.

def dashboard(request):
    if request.user.is_authenticated:
        username = request.user.username
        today = date.today()
        return render(request,"blog/dashboard.html",{'username': username, 'today': today})
    else:
        return HttpResponseRedirect("/auth/login/")