from django.urls import re_path, path
from PostgreSQL_JWT_app import views

urlpatterns = [
    # Тестовая страницы проверки JWT
    path('test_jwt_token/', views.TestJWTView.as_view(), name='test_jwt_token'),

    # Получение списка пользователей
    re_path('^users$', views.users_api),

    # Путь для удаления записи из бд и фильтрация последовательности до 9
    re_path('^users/(\d{1})$', views.users_api),
]

