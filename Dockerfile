FROM python:3.7-alpine
MAINTAINER Freez

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /blog
WORKDIR /blog
COPY ./blog /blog



RUN adduser -D user
USER user
