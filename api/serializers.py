from rest_framework import serializers
from .models import Service, Host
        
class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ['ip', 'org', 'country', 'isp', 'open_ports']

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta : 
        model = Service
        fields = ['banner','port','host']