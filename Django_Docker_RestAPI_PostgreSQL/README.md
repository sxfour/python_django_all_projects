# Django_RestAPI_PostgreSQL 
# Запуск локально (перед запуском проекта)
    pip install -r requirements.txt
    python manage.py makemigrations PostgreSQL_app
    python manage.py migrate
- API отвечает за POST/GET/PUT/DELETE, вывод данных в формате JSON.
https://github.com/sxfour/python_django_all_projects/assets/112577182/e480a130-7776-4105-90c5-19c71f00f04a

# Запуск в docker (postgresql & django containers)
    chmod +x ./install.sh
    ./install.sh

# Очистка и удаление контейнеров
    docker stop #CURRENT_CONTAINER#
    docker system prune -a
