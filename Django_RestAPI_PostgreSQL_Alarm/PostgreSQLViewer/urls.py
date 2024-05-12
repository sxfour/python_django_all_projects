from django.urls import re_path
from PostgreSQLViewer import views

urlpatterns = [
    re_path(r'^users$', views.users_api),
    re_path(r'^users/([0-9]+)$', views.users_api),
]
