from rest_framework import serializers
from .models import Service, Host

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta : 
        model = Service
        fields = ['banner','port','host']