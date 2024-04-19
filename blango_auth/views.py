from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def profile(request):
    return render(request, "blango_auth/profile.html")

def login(request):
    return render(request, "blango_auth/login.html")

def logout(request):
    return render(request, "blango_auth/logout.html")