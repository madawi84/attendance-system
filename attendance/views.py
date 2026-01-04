from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Location
from .serializers import LocationSerializer, CheckInSerializer
from users.permissions import IsHR          

# ────────────────────────────────────────────────────────────────
# HR-only: create a new work-site
# ────────────────────────────────────────────────────────────────
import logging
logger = logging.getLogger(__name__)

class LocationCreateView(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated, IsHR]

    def perform_create(self, serializer):
        logger.debug(f'User: {self.request.user}')
        logger.debug(f'Is Superuser: {self.request.user.is_superuser}')
        logger.debug(f'User has company: {hasattr(self.request.user, "company")}')
        
        if hasattr(self.request.user, 'company') and self.request.user.company:
            serializer.save(company=self.request.user.company)
        else:
            logger.error("This user does not have a company attached.")
            # You can either raise an error, or handle gracefully
            raise ValueError("Cannot create location: user is not assigned to any company.")

# ────────────────────────────────────────────────────────────────
# Employee check-in
# ────────────────────────────────────────────────────────────────
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


