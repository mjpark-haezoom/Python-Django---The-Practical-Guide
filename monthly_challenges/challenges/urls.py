from django.urls import path

from . import views

urlpatterns = [
 path("january", views.january),
 path("febrary", views.febrary),
 path("march", views.march)
]

