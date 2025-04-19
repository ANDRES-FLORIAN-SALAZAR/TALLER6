from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import RegisterForm, UpdateForm, FormularioInsertar, FormularioEliminar


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
        if "confirm" in request.POST:  # Check for confirmation
            request.user.delete()
            return redirect("home")
        else:
            return render(request, "registration/delete.html", {"user": request.user, "error": "Please confirm account deletion."})
    return render(request, "registration/delete.html", {"user": request.user})

# Se crea la vista para insertar un nuevo usuario
@login_required
def insert_view(request):
    if request.method == "POST":
        form = FormularioInsertar(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = FormularioInsertar()
    return render(request, "registration/insert.html", {"form": form})
# Se crea la vista para eliminar un usuario
@login_required
def delete_user_view(request):
    if request.method == "POST":
        form = FormularioEliminar(request.POST)
        if form.is_valid():
            form.guardar()
            return redirect("home")
    else:
        form = FormularioEliminar()
    return render(request, "registration/delete_user.html", {"form": form})
# Se crea la vista para actualizar un usuario