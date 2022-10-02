FROM python:3.9-buster

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --upgrade pip \
	&& pip install -r /app/requirements.txt