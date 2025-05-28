'''attendance/models.py
This file contains the models for the attendance app.
It defines the Location model for geofenced work-sites and the CheckInRecord model for employee check-in/out events.
'''


from django.db import models
from django.conf import settings
from companies.models import Company

class Location(models.Model):
    """
    One geofenced work-site per company.
    """
    company       = models.ForeignKey(Company, on_delete=models.CASCADE)
    name          = models.CharField(max_length=255)
    latitude      = models.DecimalField(max_digits=9, decimal_places=6)
    longitude     = models.DecimalField(max_digits=9, decimal_places=6)
    radius_meters = models.PositiveIntegerField(default=100)  # allowed radius

    def __str__(self):
        return f"{self.company.name} – {self.name}"

class CheckInRecord(models.Model):
    """
    One row per employee check-in/out event.
    """
    user      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location  = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    latitude  = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)
    synced    = models.BooleanField(default=True)   # false when captured offline

    def __str__(self):
        return f"{self.user.username} @ {self.timestamp:%Y-%m-%d %H:%M}"


