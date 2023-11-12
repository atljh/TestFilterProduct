from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import FilterNumbers
from .serializers import ProductSerializer
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

class FilteredProductsView(APIView):
    def post(self, request, *args, **kwargs):
        products = request.data

        filter_numbers = FilterNumbers.objects.values_list('number', flat=True)
        print(filter_numbers)
        filtered_data = [item for item in products if item.get('productCode') in filter_numbers]
        print(filtered_data)
        return Response(filtered_data, status=status.HTTP_200_OK)
