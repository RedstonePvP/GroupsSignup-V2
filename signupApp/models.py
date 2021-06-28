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
