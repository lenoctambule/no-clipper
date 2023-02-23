from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
import json
from .models import *
from .serializers import *

class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.order_by('?')

    def create(self, request):
        data = json.loads(request.body)
        host, created = Host.objects.update_or_create(ip=data['host'])
        banner = Service(banner=data['banner'], host=host, port=data['port'])
        banner.save()
        return Response(data, status=201)