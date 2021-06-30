from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexView, name="index"),
    path("register/<int:eventID>/<int:groupID>", views.registerView, name="register"),
]
