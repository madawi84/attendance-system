from django.urls import path
from .views import CheckInView, LocationCreateView   # LocationCreateView you already wrote


urlpatterns = [
    path("locations/", LocationCreateView.as_view(), name="location-create"),
    path("check-in/", CheckInView.as_view(), name="check-in"),
]
