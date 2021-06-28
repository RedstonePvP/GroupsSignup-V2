from django.shortcuts import render
from django.http import HttpResponse
from .models import group, event, externalEvent

def indexView(response):
    return HttpResponse("hi")
