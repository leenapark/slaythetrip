from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurant, name='restaurant'),
    path("post/", views.ajax, name="post"),
    path('selapi/', views.selapi, name="selapi"),
]