from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Tasks


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"{username} has been registered")
            return redirect("index")
    form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})


@login_required
def index(request):
    if request.method == "POST":
        task = request.POST.get("task")
        print(task)
        new_task = Tasks.objects.create(name=task)
        new_task.save()
        tasks = Tasks.objects.all()
        return render(request, "index.html", {"tasks": tasks})
    return render(request, "index.html")
