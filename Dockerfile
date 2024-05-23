FROM python:3.8-slim

RUN mkdir /shopping
WORKDIR /shopping

RUN apt-get update && apt-get install -y libpq-dev build-essential

COPY . /shopping

RUN test -d /shopping/instance || mkdir /shopping/instance

RUN chmod -R 777 /shopping/instance

COPY .env /shopping/.env

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

EXPOSE 5000
