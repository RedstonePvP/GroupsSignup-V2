import datetime
from .forms import registerForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import group, event, externalEvent, regisration

def indexView(response):
    q1 = event.objects.filter(active=True)
    q1 = q1.filter(date__gte=datetime.date.today())
    
    q2 = externalEvent.objects.filter(active=True)
    q2 = q2.filter(date__gte=datetime.date.today())

    allEvents = list(q1)+list(q2)
    allEvents.sort(key=lambda x: x.date, reverse=False)
    eventsFormated = []
    for evnt in allEvents:
        eventsFormated.append([True if evnt._meta.db_table == "signupApp_event" else False
        , evnt.title, evnt.date])
        if eventsFormated[-1][0]:
            eventsFormated[-1].append([])
            for group in evnt.groups.all():
                eventsFormated[-1][-1].append([group.id, group.name,
                "disabled" if regisration.objects.filter(event=evnt, group=group).count() >= group.max else None])
        else:
            eventsFormated[-1].append(evnt.url)
        eventsFormated[-1].append(evnt.id)
    
    print(eventsFormated)
    for ev in eventsFormated:
        print(ev)
    return render(response, "signupApp/index.html", {"events": eventsFormated})

def registerView(response, eventID, groupID):
    evnt = event.objects.filter(pk=eventID).first()
    grp = group.objects.filter(pk=groupID).first()
    if not evnt or not grp or not evnt.active:
        return redirect("index")
    if regisration.objects.filter(event=evnt, group=grp).count() >= grp.max:
        return redirect("index")
    if response.method == "POST":
        form = registerForm(response.POST)
        if form.is_valid():
            qf = lambda x: form.cleaned_data[x]
            newReg = regisration(event=evnt, group=grp, firstName=qf("firstName"), 
            lastName=qf("lastName"), age=qf("age"), pickupName=qf("pickupName"), 
            parentLocation=qf("parentLocation"), allergies=qf("allergies"), 
            address=qf("address"))
            newReg.save()
            return redirect("confirm", registerID=newReg.id)
    form = registerForm()
    data = {"form": form, "event":evnt, "group":grp}
    return render(response, "signupApp/register.html", data)

def confirmationView(response, registerID):
    reg = regisration.objects.filter(pk=registerID).first()
    if not reg or reg.viewed:
        return redirect("index")
    reg.viewed = True
    reg.save()
    return render(response, "signupApp/confirmation.html", {"register":reg})
