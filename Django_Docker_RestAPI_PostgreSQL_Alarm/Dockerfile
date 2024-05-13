FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /restapi_postgresql_alarm
WORKDIR /restapi_postgresql_alarm

COPY requirements.txt /restapi_postgresql_alarm
RUN pip install -r requirements.txt

COPY . /restapi_postgresql_alarm

RUN python manage.py makemigrations && python manage.py migrate

CMD python manage.py runserver 0.0.0.0:8000