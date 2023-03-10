from django.contrib import admin
from .models import Host, Service

class HostAdmin(admin.ModelAdmin):
    search_fields = ['ip']
    list_display = ('ip', 'open_ports')

class ServiceAdmin(admin.ModelAdmin):
    search_fields = ['banner']
    list_display = ('host', 'port', 'banner')

admin.site.register(Host, HostAdmin)
admin.site.register(Service, ServiceAdmin)