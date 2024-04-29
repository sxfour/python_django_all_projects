# Django_JWT_Auth
- Используется версия Python 3.11.0
# Пример использования POST запроса к django для получения токена JWT

# Подключение к django с токеном JWT и получение response с успешным доступом

# Запуск локально
      python manage.py makemigrations && python manage.py migrate && python manage.py createsuperuser например (root:toor)
# Запуск docker, переходим в директорию jwt_config
      docker build -t django_restapi_jwt_auth .
      docker run -m 200m --cpus="1" -it -p 8000:8000 django_restapi_jwt_auth
# Очистка хранилища docker
      docker system prune -a
      docker system prune
      docker rm $(docker ps -q -f status=exited)
