FROM python:3.11-alpine

ENV  PYTHONDONTWRITEBYTECODE  1
ENV  PYTHONUNBUFFERED  1

RUN mkdir /restapi
WORKDIR  /restapi

COPY requirements.txt /restapi
RUN pip install -r requirements.txt

COPY . /restapi

RUN python manage.py makemigrations && python manage.py migrate
RUN DJANGO_SUPERUSER_PASSWORD=toor python manage.py createsuperuser --noinput --username root --email levashoveg@ya.ru

CMD python manage.py runserver 0.0.0.0:8000
