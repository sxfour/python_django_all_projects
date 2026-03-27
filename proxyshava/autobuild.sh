#!/bin/bash

docker build -t django_proxyshava .
docker run -it -p 8000:8000 django_proxyshava