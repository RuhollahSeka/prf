# pull official base image
FROM python:3.9.14-alpine


# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache --virtual .build-deps gcc musl-dev

# install python-dev
RUN apk update \
    && apk add --virtual .build-deps gcc libc-dev

RUN apk update && apk add postgresql-dev python3-dev

# install dependencies
RUN pip install --upgrade pip

# copy project
COPY . /usr/src/app/

RUN pip install -r /usr/src/app/requirements.txt
