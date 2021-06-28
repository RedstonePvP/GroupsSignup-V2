from django.shortcuts import render
from django.http import HttpResponse
from .models import group, event, externalEvent

def indexView(response):
    return render(response, "signupApp/index.html", {"name": "blabla"})
