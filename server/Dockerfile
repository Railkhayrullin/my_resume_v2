FROM python:3.8-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update -qq && apt-get install -y postgresql-client

RUN pip install -U pip uwsgi

WORKDIR /srv/app/

COPY requirements.txt /srv/app/

RUN pip install -r requirements.txt

COPY . /srv/app/

ENTRYPOINT ["sh", "./scripts/entrypoint.sh"]
