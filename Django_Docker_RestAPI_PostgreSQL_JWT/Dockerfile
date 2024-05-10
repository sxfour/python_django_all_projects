FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /restapi_postgresql_jwt
WORKDIR /restapi_postgresql_jwt

COPY requirements.txt /restapi_postgresql_jwt
RUN pip install -r requirements.txt

COPY . /restapi_postgresql_jwt

RUN python manage.py makemigrations && python manage.py migrate
RUN DJANGO_SUPERUSER_PASSWORD=toor python manage.py createsuperuser --noinput --username root --email levashoveg@ya.ru

CMD python manage.py runserver 0.0.0.0:8000