'''attendance/admin.py
This file contains the admin configuration for the attendance app.
It registers the Location and CheckInRecord models with the Django admin site.
'''

from django.contrib import admin
from .models import Location, CheckInRecord

admin.site.register(Location)
admin.site.register(CheckInRecord)


