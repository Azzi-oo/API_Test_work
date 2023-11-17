from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from general.models import CadastreRequest, ServerResponse
from .serializers import CadastreRequestSerializer, ServerResponseSerializer


class CadastreRequestView(APIView):
    def post(self, request):
        serializer = CadastreRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Response received and saved", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServerResponseView(APIView):
    def post(self, request):
        serializer = ServerResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Server response saved", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PingView(APIView):
    def get(self, request):
        return Response("Ping!", status=status.HTTP_200_OK)


class HistoryView(APIView):
    def get(self, request):
        history = CadastreRequest.objects.all()
        serializer = CadastreRequestSerializer(history, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
