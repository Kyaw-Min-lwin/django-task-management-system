from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'{username} has been registered')
            return redirect('index')
    form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def index(request):
    return render(request, 'index.html')
