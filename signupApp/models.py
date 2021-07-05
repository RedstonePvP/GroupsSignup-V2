from django.db import models

# Create your models here.
class group(models.Model):
    name = models.CharField(max_length=200)
    max = models.IntegerField()
    active = models.BooleanField()

    def __str__(self):
        return self.name
    

class event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    groups = models.ManyToManyField(group)
    active = models.BooleanField()
    
    def __str__(self):
        return self.title

class externalEvent(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    url = models.URLField()
    active = models.BooleanField()

    def __str__(self):
        return self.title
    
class regisration(models.Model):
    event = models.ForeignKey(event, on_delete=models.CASCADE)
    group = models.ForeignKey(group, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    age = models.IntegerField()
    pickupName = models.CharField(max_length=100)
    parentLocation = models.CharField(max_length=100)
    allergies = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return self.firstName + " " + self.lastName

