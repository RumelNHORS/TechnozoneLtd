from django.shortcuts import render
from rest_framework import generics
from api import models as api_models
from api import serializers as api_serializers

# Create your views here.


class ServiceListView(generics.ListAPIView):
    queryset = api_models.Service.objects.all()
    serializer_class = api_serializers.ServiceSerializer


class ProjectListView(generics.ListAPIView):
    queryset = api_models.Project.objects.all()
    serializer_class = api_serializers.ProjectSerializer

class AboutUsListView(generics.ListAPIView):
    queryset = api_models.AboutUs.objects.all()
    serializer_class = api_serializers.AboutUsSerializer


