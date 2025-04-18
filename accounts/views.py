from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import RegisterForm, UpdateForm


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def update_view(request):
    if request.method == "POST":
        form = UpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UpdateForm(instance=request.user)
    return render(
        request, "registration/update.html", {"form": form, "user": request.user}
    )