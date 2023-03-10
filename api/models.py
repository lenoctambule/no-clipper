from django.db import models
from django.core.validators import validate_comma_separated_integer_list

class Host(models.Model):
    ip = models.GenericIPAddressField(unique=True, primary_key=True)
    org = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    isp = models.CharField(max_length=100)
    discovered_on=models.DateTimeField(auto_now_add=True)
    lastscan_on=models.DateTimeField(auto_now_add=True)
    open_ports = models.CharField(max_length=300,validators=[validate_comma_separated_integer_list])

class Service(models.Model):
    host = models.CharField(max_length=100)
    banner = models.TextField()
    port = models.IntegerField()
    
