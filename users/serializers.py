'''This module contains serializers for the User model.
It defines how the User model data is converted to and from JSON format,'''

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_admin', 'is_hr', 'is_manager', 'is_supervisor', 'company']
