from django.contrib import admin
from .models import CadastreRequest, ServerResponse


@admin.register(CadastreRequest)
class CadastreRequestAdmin(admin.ModelAdmin):
    list_display = ('cadastre_number', 'latitude', 'longitude', 'request_time', 'external_server_response')
    search_fields = ('cadastre_number', 'latitude')
    list_filter = ('request_time',)


@admin.register(ServerResponse)
class ServerResponseAdmin(admin.ModelAdmin):
    list_display = ('cadastre_request', 'response', 'response_timestamp')
    search_fields = ('cadastre_request__cadastre_number', 'response_timestamp')
    list_filter = ('response_timestamp',)
