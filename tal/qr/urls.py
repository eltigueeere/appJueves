from django.urls import path
from .views import QrTarjeta, VerQr
urlpatterns = [
    path('', QrTarjeta.as_view(), name="qr"),
    path('verQr/', VerQr.as_view(), name="verQr"),
]