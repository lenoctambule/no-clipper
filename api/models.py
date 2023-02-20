from django.db import models

class Host(models.Model):
    ip = models.IPAddressField(unique=True)
    org = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    isp = models.CharField(max_length=100)
    discovered_on=models.DateTimeField(auto_now_add=True)
    lastscan_on=models.DateTimeField(auto_now_add=True)

class Service(models.Models):
    host = models.ForeignKey(Host, on_delete=models.CASCADE, related_name='host_services', null=False)
    banner = models.CharField()
    port = models.IntegerField()
    
