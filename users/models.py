# Import base user functionality from Django
from django.contrib.auth.models import AbstractUser
from django.db import models
from companies.models import Company  # Import Company model for foreign key relationship

'''
This file contains the custom user model for the attendance system.
The custom user model extends Django's default user model to include additional fields
and functionality specific to our application.

Extends Djangos built-in AbstractUser
Adds role-based fields like is_admin, is_hr, etc.
Keeps all standard fields like username, email, password

'''


# Custom User model that extends Django's default user
class User(AbstractUser):
    # Optional custom role flags for access control
    is_admin = models.BooleanField(default=False)       # For top-level admin users
    is_hr = models.BooleanField(default=False)          # For HR team members
    is_manager = models.BooleanField(default=False)     # For company managers
    is_supervisor = models.BooleanField(default=False)  # For team supervisors


    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True) # Foreign key to Company model


    # What will be shown when printing or listing a user instance
    def __str__(self):
        return self.username  # e.g., for admin display or logs
    



