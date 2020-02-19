from django.shortcuts import render, redirect
from .forms import CustomRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse


def register(request):
    if request.method == "POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New User Account Created."))
            return redirect('todolist')
    else:
        register_form = CustomRegisterForm()
    return render(request, 'register.html', {'register_from': register_form})
