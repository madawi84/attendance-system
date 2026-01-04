from rest_framework import serializers
from companies.models import Company
from .models import CheckInRecord, Location

# ── HR creates new work-site ──────────────────────────
class LocationSerializer(serializers.ModelSerializer):
    company = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Company.objects.all()
    )

    class Meta:
        model = Location
        fields = '__all__'

# ── Employee check-in request ─────────────────────────
class CheckInSerializer(serializers.Serializer):
    latitude  = serializers.DecimalField(max_digits=9, decimal_places=6)
    longitude = serializers.DecimalField(max_digits=9, decimal_places=6)

    def create(self, validated):
        request  = self.context["request"]
        user     = request.user
        lat_u    = float(validated["latitude"])
        lon_u    = float(validated["longitude"])

        # all company sites
        from geopy.distance import distance
        from .models import Location

        for site in Location.objects.filter(company=user.company):
            d = distance((lat_u, lon_u), (site.latitude, site.longitude)).m
            if d <= site.radius_meters:
                # inside a geofence → save record
                return CheckInRecord.objects.create(
                    user=user,
                    location=site,
                    latitude=lat_u,
                    longitude=lon_u,
                    synced=True,
                )

        # none matched
        raise serializers.ValidationError("Outside any company work-site.")
