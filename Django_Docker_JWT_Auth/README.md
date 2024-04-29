# Django_JWT_Auth
- Используется версия Python 3.11.0
# Пример использования POST запроса к django для получения токена JWT
https://github.com/sxfour/python_django_all_projects/assets/112577182/dd5dffac-53d8-435c-a459-4c726b319189

# Подключение к django с токеном JWT и получение response с успешным доступом
https://github.com/sxfour/python_django_all_projects/assets/112577182/109dfa08-0554-466d-9939-9b4799840669

# Запуск локально
      python manage.py makemigrations && python manage.py migrate && python manage.py createsuperuser
# Запуск docker, переходим в директорию jwt_config
      docker build -t django_restapi_jwt_auth .
      docker run -m 200m --cpus="1" -it -p 8000:8000 django_restapi_jwt_auth
# Очистка хранилища docker
      docker system prune -a
      docker system prune
      docker rm $(docker ps -q -f status=exited)
