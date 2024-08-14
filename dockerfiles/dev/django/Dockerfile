FROM python:3.10-slim-buster

LABEL maintainer="arzdex@gmail.com" 
ENV PYTHONUNBUFFERED=1

WORKDIR /user/src/app

COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./core .
