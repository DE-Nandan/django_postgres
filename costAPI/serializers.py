from rest_framework import serializers
from .models import Organization, Item, Pricing, Zone

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'type', 'description']

class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ['id', 'zone', 'fix_price']

class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = ['id', 'organization', 'item', 'zone', 'base_distance_in_km', 'km_price']

class CalculatePriceRequestSerializer(serializers.Serializer):
    zone = serializers.CharField(max_length=100)
    oraganisation_id = serializers.CharField(max_length=100)
    total_distance = serializers.DecimalField(max_digits=10, decimal_places=2)
    item_type = serializers.CharField(max_length=20)


