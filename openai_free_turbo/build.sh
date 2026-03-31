#!/bin/bash

docker build -t cookapi_free_turbo .
docker run -d --restart=always -p 3278:3278 -m 200m --cpus="1" --name cookapi_free_turbo cookapi_free_turbo
