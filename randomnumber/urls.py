from .views import random_number
from django.urls import path

urlpatterns = [
    path('', random_number, name='random'),  
]