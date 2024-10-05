from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("info/", views.info, name="info"),
    path("directions/",views.directions, name="directions"),
    path("itinerary/", views.itinerary, name="itinerary"),
    path("photos/", views.photos, name="photos"),
    path("people/", views.people, name="people"),
    path('password_entry/', views.password_entry, name='password_entry'),
]