from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .pricing import calculate_delivery_cost
from drf_spectacular.utils import extend_schema
from rest_framework.generics import GenericAPIView
from rest_framework import serializers,views
from .serializers import CalculatePriceRequestSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView

response_schema_dict = {
    "200": openapi.Response(
        description="Expected 200 description",
        examples={
            "application/json": {
                "total_price": "200",
            }
        }
    ),
}


class CalculatePriceView(APIView):
    #serializer_class = CalculatePriceRequestSerializer
   
    
    @swagger_auto_schema(request_body=CalculatePriceRequestSerializer,
                         operation_description='''
Try it out using sample
 { 
"zone": "central",
"organization_id": "005",
"total_distance": "12", 
"item_type": "perishable" 
}
'''
                         ,
                         responses=response_schema_dict)                     
    def post(self, request, *args, **kwargs):
        
        
        data = request.data
        zone = data.get('zone')
        total_distance = float(data.get('total_distance'))
        item_type = data.get('item_type')
        
        # Validate input data (e.g., check for required fields)
        if not all([zone, total_distance, item_type]):
            return Response({'error': 'Missing required parameters'}, status=400)
        
        try:
            total_price = calculate_delivery_cost(zone, total_distance, item_type)
            return Response({'total_price': total_price})
        except Exception as e:
            return Response({'error': str(e)}, status=500)