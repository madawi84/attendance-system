'''
users/urls.py
This file contains the URL patterns for the users app.
It defines the URL for the UserListView, which retrieves and returns a list of users.
It is included in the main URL configuration of the project.

'''


from django.urls import path
from .views import UserListView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
]
