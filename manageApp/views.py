from django.shortcuts import render

# Create your views here.
def homeView(response):
    return render(response, "manageApp/manageGroups.html", {})
