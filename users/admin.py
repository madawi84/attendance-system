from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


'''
This file contains the admin configuration for the custom user model.
The custom user model is registered with the Django admin site,
allowing for easy management of user accounts.

Enables managing users from the admin panel.
Adds extra checkboxes (for roles) in the user form.
Shows extra fields (like is_manager) in the list view.

'''
# Extend the default UserAdmin to support our custom User model
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'company', 'is_admin', 'is_hr', 'is_manager', 'is_supervisor')
    list_filter = ('company', 'is_admin', 'is_hr', 'is_manager', 'is_supervisor')

    fieldsets = BaseUserAdmin.fieldsets + (
        ('Custom Info', {
            'fields': ('company', 'is_admin', 'is_hr', 'is_manager', 'is_supervisor'),
        }),
    )


# Register the model and the custom admin class
admin.site.register(User, UserAdmin)

