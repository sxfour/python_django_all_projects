FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /vkys_api
WORKDIR /vkys_api

COPY requirements.txt /vkys_api
RUN pip install -r requirements.txt

COPY . /vkys_api

RUN python manage.py makemigrations && python manage.py migrate
RUN DJANGO_SUPERUSER_PASSWORD=vkysapiadmin python manage.py createsuperuser --noinput --username root --email levashoveg@ya.ru

CMD python manage.py runserver 0.0.0.0:7899