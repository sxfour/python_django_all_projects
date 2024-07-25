FROM python:3.11-alpine

ENV  PYTHONDONTWRITEBYTECODE  1
ENV  PYTHONUNBUFFERED  1

RUN mkdir /Django_Chat
WORKDIR  /Django_Chat

COPY requirements.txt /Django_Chat
RUN pip install -r requirements.txt

COPY . /Django_Chat

RUN python manage.py makemigrations && python manage.py migrate
RUN DJANGO_SUPERUSER_PASSWORD=toor python manage.py createsuperuser --noinput --username root --email levashov.teploset@mail.ru

CMD python manage.py runserver 0.0.0.0:80