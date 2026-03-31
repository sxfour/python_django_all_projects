FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /cook_api
WORKDIR /cook_api

COPY requirements.txt /cook_api
RUN pip install -r requirements.txt

COPY . /cook_api

RUN python manage.py makemigrations && python manage.py migrate

# Создание суперпользователя
RUN DJANGO_SUPERUSER_PASSWORD=cookapiadmin python manage.py createsuperuser --noinput --username root --email levashoveg@ya.ru

# Установка Gunicorn
RUN pip install gunicorn

# Команда для запуска через Gunicorn
CMD ["gunicorn", "cookapi.wsgi:application", "--bind", "0.0.0.0:3278"]
