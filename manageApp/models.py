from django.db import models

# Create your models here. manageApp
class groupInfo(models.Model):
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.pk
