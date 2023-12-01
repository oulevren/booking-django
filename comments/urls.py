from django.urls import path
from .views import *

urlpatterns = [
    path('yorum-ekle',yorumEkle,name='yorum-ekle'),
]