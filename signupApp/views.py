from django.shortcuts import render
from django.http import HttpResponse

def indexView(response):
    return HttpResponse("hi")
