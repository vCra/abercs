from django.urls import path
from django.views.generic import RedirectView

from abercompsoc.events.views import EventList, EventDetail

app_name = "abercompsoc.events"

urlpatterns = [
    path("", view=RedirectView.as_view(pattern_name="events:future_event_list", permanent=True), name="event_list"),
    path("upcoming/", view=EventList.as_view(), name="future_event_list"),
    path("<int:event_id>/", view=EventDetail.as_view(), name="event_detail"),

]
