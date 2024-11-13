from rest_framework import serializers
from api import models as api_models


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Service
        fields = ['id', 'title', 'short_description', 'image']
