from django.contrib import admin
from .models import Company


# Register your models here.
'''
This allows you to manage companies from a browser interface

'''

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain', 'max_users', 'created_at')
    search_fields = ('name', 'domain')
