# Django_RestAPI_PostgreSQL_JWT

# RestAPI на Django с использованием токенов доступа в запросах к серверу c PostgreSQL
- requirements.txt
- Python 3.10
- RestAPI using PostgreSQL

# Конфигурация перед запуском проекта
      pip install -r requirements.txt
      python manage.py migrate PostgreSQL_JWT_App
      python manage.py createsuperuser
      
# Запуск в Docker
      chmod +x install.sh
      ./install.sh

# Очистка и удаление контейнеров
    docker stop #CURRENT_CONTAINER#
    docker system prune -a
