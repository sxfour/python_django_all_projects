from django.contrib import staticfiles
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
]
