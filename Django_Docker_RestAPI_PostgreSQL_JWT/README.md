# Django_RestAPI_PostgreSQL_JWT

# RestAPI на Django с использованием токенов доступа в запросах к серверу c PostgreSQL
- requirements.txt
- Python 3.10
- RestAPI using PostgreSQL

# Конфигурация перед запуском проекта (локально)
      pip install -r requirements.txt
      python manage.py migrate PostgreSQL_JWT_App
      python manage.py createsuperuser
      
# Запуск в Docker
      chmod +x install.sh
      ./install.sh
      
![docker](https://github.com/sxfour/python_django_all_projects/assets/112577182/5de1383c-89fc-453f-8579-b242d5490e94)

# Очистка и удаление контейнеров
    docker stop #CURRENT_CONTAINER#
    docker system prune -a
