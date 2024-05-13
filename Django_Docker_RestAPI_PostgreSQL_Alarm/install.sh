#!/bin/bash

docker run -m 100m --cpus="0.5" --name restapi_postgresql_alarm -p 5432:5432 -e POSTGRES_PASSWORD=restalarm -e POSTGRES_DB=djangoRestAPIAlarm -d postgres:13.3-alpine
docker build --network="host" -t django_restapi_postgresql_alarm .
docker container ls --filter name=restapi_postgresql_alarm
docker container cp add_time.sql restapi_postgresql_alarm:/
docker container exec -it restapi_postgresql_alarm psql --dbname=djangoRestAPIAlarm --username=postgres -f /add_time.sql
docker run --network="host" -m 200m --cpus="1" -it -p 8000:8000 django_restapi_postgresql_alarm
