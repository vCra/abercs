from enum import Enum

from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import DateTimeRangeField
from django.db.models import Model, CharField, ManyToManyField, ForeignKey, CASCADE, IntegerField, TextField, \
    DateTimeField
from django.urls import reverse

User = get_user_model()


class Event(Model):

    event_name = CharField(max_length=255)
    date = DateTimeRangeField()
    attendees = ManyToManyField(User, through="events.UserEventAssociation")
    max_attendees = IntegerField(null=True)
    description = TextField()
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_name

    def get_absolute_url(self):
        return reverse("events:event_detail", kwargs={"event_id": self.id})


class EventTiming(Model):
    event = ForeignKey(Event, on_delete=CASCADE)
    details = TextField()
    time = DateTimeField()


class UserEventAssociationType(Enum):
    NA = "NoAssociation"
    IN = "Interested"
    WA = "WantingToAttend"
    WL = "Waiting"
    AT = "Attending"


class UserEventAssociation(Model):
    """
    A many to many linking table, which also s tores the users association to the event, such as
    if they are are attending, or are interested etc
    """

    event = ForeignKey(Event, on_delete=CASCADE)
    user = ForeignKey(User, on_delete=CASCADE)
    info = CharField(max_length=2, choices=[(i, i.value) for i in UserEventAssociationType], default="NA")
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)


