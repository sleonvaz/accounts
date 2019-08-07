FROM python:3.7-alpine
MAINTAINER Salvador Leon Vaz

ENV PYTHONUNBUFFERED 1

RUN apk add tzdata

RUN apk update
RUN pip install --upgrade pip
RUN pip install pipenv

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps\
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt

RUN apk del .tmp-build-deps
RUN apk add gcc
RUN apk add libc-dev
RUN apk add linux-headers
RUN apk add mariadb-dev
RUN apk add postgresql-dev
RUN apk add netcat-openbsd
RUN apk add curl


RUN mkdir /app
COPY ./src /app
WORKDIR /app
RUN chmod -R a+X /app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web



