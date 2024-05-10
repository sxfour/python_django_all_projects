#!/bin/bash

docker run -m 100m --cpus="0.5" --name restapi_postgresql -p 5432:5432 -e POSTGRES_USER=django_rest_api -e POSTGRES_PASSWORD=resttest -e POSTGRES_DB=djangoRestAPI -d postgres:13.3-alpine
docker build --network="host" -t django_restapi_postgresql .
docker run --network="host" -m 200m --cpus="1" -it -p 8000:8000 django_restapi_postgresql
