# Django_RestAPI_PostgreSQL 
# Запуск локально (перед запуском проекта)
    pip install -r requirements.txt
    python manage.py makemigrations PostgreSQL_app
    python manage.py migrate
- API отвечает за POST/GET/PUT/DELETE, вывод данных в формате JSON.
https://github.com/sxfour/django_all_projects/assets/112577182/0fd13ed8-fcaa-4cd7-8a27-09dc806ba69a

# Запуск в docker (postgresql & django containers)
    chmod +x ./install.sh
    ./install.sh

# Очистка и удаление контейнеров
    docker stop #CURRENT_CONTAINER#
    docker system prune -a
