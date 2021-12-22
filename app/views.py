from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from app.models import City, Street, Shop
from app.serializers import CitySerializer, StreetSerializer, ShopSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def cities_list(request):
    if request.method == 'GET':
        cities = City.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            cities = cities.filter(name__icontains=name)

        serializer = CitySerializer(cities, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)