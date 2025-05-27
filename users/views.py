'''
users/views.py
This file contains the views for the users app.
It defines the UserListView, which retrieves and returns a list of users.

'''


from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from .permissions import IsHR  # IsHR is defined in permissions.py

class UserListView(APIView):
    permission_classes = [IsAuthenticated, IsHR]    # Ensure that only authenticated users with HR permissions can access this view

    def get(self, request):
        print("HR flag =", request.user.is_hr)
        users = User.objects.filter(company=request.user.company)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
