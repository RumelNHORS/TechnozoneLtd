from django.shortcuts import render
from rest_framework import generics
from api import models as api_models
from api import serializers as api_serializers

# Create your views here.


class ServiceListView(generics.ListAPIView):
    queryset = api_models.Service.objects.all()
    serializer_class = api_serializers.ServiceSerializer

