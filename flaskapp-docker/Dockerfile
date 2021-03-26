FROM ubuntu:18.04
MAINTAINER chiragr83@gmail.com

RUN apt-get update -y
RUN apt-get install python3-pip -y
RUN apt-get install gunicorn3 -y

COPY ./requirements.txt requirements.txt
COPY ./ /application

RUN pip3 install -r requirements.txt
WORKDIR /application
ENV PYTHONPATH /application

EXPOSE 8000
