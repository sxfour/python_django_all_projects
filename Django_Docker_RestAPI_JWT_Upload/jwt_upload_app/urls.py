from django.urls import path
from jwt_upload_app import views

urlpatterns = [
    path('teploset_docs/', views.users_api),
]
