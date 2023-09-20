from django.urls import path
from . import views

urlpatterns = [
    # path('', views.Weather.as_view(), name="weather"),
    path('', views.weather_trip, name="weather"),
    path("test/", views.ajax, name="test"),
]
