from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("info/", views.info, name="info"),
    path("directions/",views.directions, name="directions"),
    path("rsvp/", views.rsvp, name="rsvp"),
    path("itinerary/", views.itinerary, name="itinerary"),
    path("photos/", views.photos, name="photos"),
    path("people/", views.people, name="people"),
    path('submit-rsvp/', views.submit_rsvp, name="submit_rsvp"),
    path('password_entry/', views.password_entry, name='password_entry'),
    path('get_invite/', views.get_invite, name='get_invite'),
    path('thanks_accepted/', views.thanks_accepted, name='thanks_accepted'),
    path('thanks_declined/', views.thanks_declined, name='thanks_declined'),
]