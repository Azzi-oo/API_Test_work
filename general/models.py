from django.db import models


class CadastreRequest(models.Model):
    cadastre_number = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    request_time = models.DateTimeField(auto_now_add=True)
    external_server_response = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f"CadastreRequest {self.id}"


class ServerResponse(models.Model):
    cadastre_request = models.ForeignKey(
        to=CadastreRequest,
        on_delete=models.CASCADE,
        related_name='server_response',
    )
    response = models.BooleanField()
    response_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ServerResponse for {self.cadastre_request_id}"
