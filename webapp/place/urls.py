from django.urls import path, include
from .views import *


urlpatterns = [
    path('', place),
    path('<slug:cityid>/', city)
]