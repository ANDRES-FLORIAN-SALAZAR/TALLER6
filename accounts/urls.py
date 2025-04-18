from django.urls import path
from . import views
# from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("update/", views.update_view, name="update"),
]
