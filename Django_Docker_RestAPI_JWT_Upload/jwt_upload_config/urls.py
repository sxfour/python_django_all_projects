"""
URL configuration for jwt_upload_config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework_simplejwt import views as jwt_views

from .secrets_panel import UrlCreate

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from django.urls import path, re_path, include


urlpatterns = [
                  path(f'{UrlCreate().get_url_create()}/', admin.site.urls),
                  path('teploset_api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('teploset_api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
                  re_path('^', include('jwt_upload_app.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "MTS"
admin.site.site_title = "MTS Admin panel"
admin.site.index_title = "Welcome to MTS Docs Admin panel"
