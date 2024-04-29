# Django_JWT_Auth
- Используется версия Python 3.11.0
# Пример использования POST запроса к django для получения токена JWT
https://github.com/sxfour/Django_JWT_Auth/assets/112577182/58d639e2-8144-42aa-90fd-d13e4e39d33b
# Подключение к django с токеном JWT и получение response с успешным доступом
https://github.com/sxfour/Django_JWT_Auth/assets/112577182/97973044-6ad5-471c-b14c-ddbe06a62706
# Запуск локально
- Перед запуском проекта необходимо добавить базу данных, например стандартную sqlite
- python manage.py makemigrations && python manage.py migrate && python manage.py createsuperuser например (root:toor)
# Запуск docker
- Переходим в директорию jwt_config
- docker build -t django_restapi_jwt_auth .
- docker run -m 200m --cpus="1" -it -p 8000:8000 django_restapi_jwt_auth
# Очистка хранилища docker
- docker system prune -a
- docker system prune
- docker rm $(docker ps -q -f status=exited)
