How to setup
============

create venv and install packages:

    $ python3.9 -m venv .venv
    $ source .venv/bin/activate
    $ pip install -r requirements.txt

build:

    $ docker-compose build

run:

    $ docker-compose up

tests:

    $ docker-compose run backend pytest

Brief desc
==========

stack:
  - starlette (backend)
  - Kivy (mobile app)

DB:
  - postgres
