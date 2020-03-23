from django.urls import path
from road.views import road_controller

urlpatterns = [
    path('',road_controller),
]
