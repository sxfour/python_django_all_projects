FROM python:3.11-alpine

ENV  PYTHONDONTWRITEBYTECODE  1
ENV  PYTHONUNBUFFERED  1

RUN mkdir /proxyshava
WORKDIR  /proxyshava

COPY requirements.txt /proxyshava
RUN pip install -r requirements.txt

COPY . /proxyshava

RUN python manage.py makemigrations && python manage.py migrate

CMD python manage.py runserver 0.0.0.0:8000
