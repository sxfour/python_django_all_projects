from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('PostgreSQL_app.urls')), # URL для вашего API
]