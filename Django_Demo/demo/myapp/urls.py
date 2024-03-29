from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("todos/", views.todos, name="Todos"),
    path("info/", views.info, name="info"),
    path("rsvp/", views.rsvp, name="rsvp"),
    path('submit-rsvp/', views.submit_rsvp, name="submit_rsvp"),
    path('password_entry/', views.password_entry, name='password_entry'),
]