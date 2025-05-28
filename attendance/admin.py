'''attendance/admin.py
This file contains the admin configuration for the attendance app.
It registers the Location and CheckInRecord models with the Django admin site.
'''

from django.contrib import admin
from .models import Location, CheckInRecord

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "latitude", "longitude", "radius_meters")

admin.site.register(CheckInRecord)
