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

"""
@api_view(['GET','POST'])
def service_list(request):
    if request.method == 'POST' :
        data = json.loads(request.body)
        banner = Service(banner=data['banner'], host=data['host'], port=data['port'])
        banner.save()
        return Response(data, status=201)
    elif request.method == 'GET' :
        return Response(status=404)
"""