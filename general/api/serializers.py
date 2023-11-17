from rest_framework import serializers
from general.models import CadastreRequest, ServerResponse


class CadastreRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastreRequest
        fields = '__all__'


class ServerResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerResponse
        fields = '__all__'
