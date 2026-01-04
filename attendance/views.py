# attendance/views.py
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
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
        """
        Create a Location with correct multi-tenant rules:

        - Super admin (is_admin=True): can create a location for ANY company,
        but must provide `company` in the request payload.
        - Non-admin: must belong to a company; the location is forced to their company.
        """
        user = self.request.user

        # Super admin path: allow specifying company explicitly
        if getattr(user, "is_admin", False):
            # If company not provided in request data, return a clean 400
            if not serializer.validated_data.get("company"):
                raise ValidationError({"company": "Super admin must provide a company when creating a location."})
            serializer.save()
            return

        # Non-admin path: user must have a company
        if not getattr(user, "company", None):
            raise ValidationError({"company": "Cannot create location: user is not assigned to any company."})

        # Force company to the user's company (prevents cross-company creation)
        serializer.save(company=user.company)

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


