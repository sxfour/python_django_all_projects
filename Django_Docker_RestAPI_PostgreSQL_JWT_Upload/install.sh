#!/bin/bash

docker run -m 100m --cpus="0.5" --name restapi_postgresql_jwt_upload -p 5432:5432 -e POSTGRES_USER=django_rest_api -e POSTGRES_PASSWORD=24e8qdB -e POSTGRES_DB=djangoRestAPI_JWT_Upload -d postgres:13.3-alpine
docker build --network="host" -t django_restapi_postgresql_upload .
docker run --network="host" -m 200m --cpus="1" -it -p 8000:8000 django_restapi_postgresql_upload