from .models import Pricing, Item,Zone
from .serializers import PricingSerializer,ZoneSerializer
from rest_framework.exceptions import NotFound

def calculate_delivery_cost(zone, total_distance, item_type):
    try:
        
        zone = Zone.objects.get(zone=zone)
        zone_serializer = ZoneSerializer(zone)
        zone_data = zone_serializer.data
        base_price = float(zone_data['fix_price'])   
        
        
        # Retrieve pricing information from the database based on the provided item type
        pricing = Pricing.objects.get(item__type=item_type,zone=zone_data['id'])

        # Serialize the retrieved Pricing object to access pricing details
        serializer = PricingSerializer(pricing)
        serialized_data = serializer.data
        
        # Extract relevant pricing details from the serialized data
        
        item_type = serialized_data['item']
        
        km_price = 0

        if(item_type == 1):
            km_price = 1.5
        else:
            km_price = 1    

       
       

        # Calculate total price based on the provided specifications
        if total_distance <= serialized_data['base_distance_in_km']:
            total_price = base_price
        else:
            base_distance_cost = base_price
            additional_distance = total_distance - serialized_data['base_distance_in_km']
            additional_distance_cost = additional_distance * km_price
            total_price = base_distance_cost + additional_distance_cost

        
        return total_price

    except Pricing.DoesNotExist:
        raise NotFound("Pricing information not found")
