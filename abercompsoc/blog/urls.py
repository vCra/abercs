from django.urls import path
from django.views.generic import RedirectView

from abercompsoc.blog.views import BlogDetailView, BlogTableView
from abercompsoc.events.views import EventList, EventDetail

app_name = "abercompsoc.blog"

urlpatterns = [
    path("", BlogTableView.as_view(), name="blog_list"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:slug>/",
        BlogDetailView.as_view(),
        name='blog_detail',
    ),

]
