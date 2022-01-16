from django.contrib import admin

# Register your models here.
from .models import Guest, Event, EventFinder

admin.site.register(Guest)
admin.site.register(Event)
admin.site.register(EventFinder)