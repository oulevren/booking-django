from django.urls import path
from .views import *

urlpatterns = [
    path('otel-ekle/',otelEkle,name='otel-ekle'),
    path('tesis-ekle/',tesisEkle,name='tesis-ekle'),
]
