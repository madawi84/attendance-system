from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import CheckInSerializer

class CheckInView(generics.CreateAPIView):
    serializer_class   = CheckInSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        record = serializer.save()
        return Response(
            {"message": "Checked-in", "location": record.location.name},
            status=status.HTTP_201_CREATED,
        )


