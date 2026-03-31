from django.urls import path
from .views import CookAssistantView

urlpatterns = [
    path('cook/', CookAssistantView.as_view(), name='cook-assistant'),
    path('cook_gpt4/', CookGPT4View.as_view(), name='cook-gpt4'),
]