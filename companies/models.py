from django.db import models

# Create your models here.
'''
name: Company name

logo: Uploadable logo image

domain: Unique domain name (e.g., for custom branding)

max_users: Number of users allowed by their plan

created_at: Auto timestamp

__str__: Tells Django how to display this object in the admin panel
'''

class Company(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    domain = models.CharField(max_length=255, unique=True)
    max_users = models.PositiveIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
