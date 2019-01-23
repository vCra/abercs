from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from django_tables2 import SingleTableView

from abercompsoc.events.models import Event
from abercompsoc.events.tables import EventTable


class EventList(SingleTableView):
    model = Event
    table_class = EventTable
    template_name = "events/event_list.html"


class EventDetail(DetailView):
    model = Event
    pk_url_kwarg = "event_id"

