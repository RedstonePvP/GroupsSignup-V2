import datetime
from .forms import registerForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import group, event, externalEvent, regisration

def indexView(response):
    q1 = event.objects.filter(active=True)
    q1.filter(date__gte=datetime.date.today())
    
    q2 = externalEvent.objects.filter(active=True)
    q2.filter(date__gte=datetime.date.today())

    allEvents = list(q1)+list(q2)
    allEvents.sort(key=lambda x: x.date, reverse=False)
    print(allEvents[0]._meta.db_table)
    return render(response, "signupApp/index.html", {"events": allEvents})

def registerView(response, eventID, groupID):
    print(eventID)
    print(groupID)
    form = registerForm()
    return render(response, "signupApp/register.html", {"form": form})
