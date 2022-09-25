from django.shortcuts import render, redirect
from .forms import userRegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST":
        form = userRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created successfully")
            return redirect('/login')
    else:
        form = userRegisterForm()
    return render(request, "register/register.html", {"form": form})
