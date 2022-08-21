from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.http import HttpResponse

from .forms import RegistrationForm

# Create your views here.

def home(request):
    return render(request, 'account/base.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = RegistrationForm()
            
    return render(request, 'account/register.html', {'form': form, 'title': 'Register'})

def logout_user(request):
    username = request.user.username
    logout(request)
    messages.success(request, f'{username} has been logged out')
    return redirect('index')    