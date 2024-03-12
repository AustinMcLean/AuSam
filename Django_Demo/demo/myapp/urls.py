from django.urls import path
from . import views
from .views import submit_rsvp

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("todos/", views.todos, name="Todos"),
    path("info/", views.info, name="info"),
    path("rsvp/", views.rsvp, name="rsvp"),
    path('submit-rsvp/', submit_rsvp, name="submit_rsvp")
]