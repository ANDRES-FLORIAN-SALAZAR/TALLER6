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

# Creacion de la vista delete
# Se crea la vista delete para que el usuario pueda eliminar su cuenta
@login_required
def delete_view(request):
    if request.method == "POST":
        request.user.delete()
        return redirect("home")
    return render(request, "registration/delete.html", {"user": request.user})

# Creacion de la vista insert
# Se crea la vista insert para que el usuario pueda agregar su nombre y apellido
@login_required
def insert(request):
    if request.method == "POST":
        form = UpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UpdateForm(instance=request.user)
    return render(
        request, "registration/insert.html", {"form": form, "user": request.user}
    )