FROM ubuntu:18.04

RUN apt-get update -y
RUN apt-get install python3-pip -y

COPY ./alem_requirements.txt alem_requirements.txt
COPY . /opt/

RUN pip3 install -r alem_requirements.txt
WORKDIR /opt/

CMD ["alembic", "upgrade", "head"]
