FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /restapi_postgresql_jwt_upload
WORKDIR /restapi_postgresql_jwt_upload

COPY requirements.txt /restapi_postgresql_jwt_upload
RUN pip install -r requirements.txt

COPY . /restapi_postgresql_jwt_upload

RUN python manage.py makemigrations && python manage.py migrate
RUN DJANGO_SUPERUSER_PASSWORD=Teplos2022@#$ python manage.py createsuperuser --noinput --username cpp_client --email levashov.teploset@mail.ru

CMD python manage.py runserver 0.0.0.0:8000