from django.contrib import admin

# Register your models here.
from .models import Event, EventTiming, UserEventAssociation

admin.site.register(Event)
admin.site.register(EventTiming)
admin.site.register(UserEventAssociation)
