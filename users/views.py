'''
users/views.py
This file contains the views for the users app.
It defines the UserListView, which retrieves and returns a list of users.

'''
# This view retrieves all users in the same company as the authenticated user.
# users/views.py
from rest_framework.permissions import IsAuthenticated
from .permissions import IsHR
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class UserListView(APIView):
    permission_classes = [IsAuthenticated, IsHR]

    def get(self, request):
        # return only active users in the same company
        qs = User.objects.filter(company=request.user.company)
        if request.query_params.get("active") == "true":
            qs = qs.filter(is_active=True)
        serializer = UserSerializer(qs, many=True)
        return Response(serializer.data)
