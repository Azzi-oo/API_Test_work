from django.urls import path
from .views import CadastreRequestView, ServerResponseView, PingView, HistoryView


urlpatterns = [
    path('query/', CadastreRequestView.as_view(), name='cadastre-request'),
    path('result/', ServerResponseView.as_view(), name='server-response'),
    path('ping/', PingView.as_view(), name='ping'),
    path('history/', HistoryView.as_view(), name='history'),
]
