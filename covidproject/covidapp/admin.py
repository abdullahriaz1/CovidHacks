from django.contrib import admin

# Register your models here.
from .models import Guest, Event

admin.site.register(Guest)
admin.site.register(Event)