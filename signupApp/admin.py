from django.contrib import admin
from .models import group, event, externalEvent, regisration

# Register your models here.
admin.site.register(group)
admin.site.register(event)
admin.site.register(externalEvent)
admin.site.register(regisration)
