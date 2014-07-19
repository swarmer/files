#!/bin/sh
cd /home/{{ app_name }}/{{ app_name }}
. venv/bin/activate
./manage.py migrate

export DEBUG=False
export MEDIA_ROOT=/home/{{ app_name }}/media/
exec gunicorn -b :{{ proxy_port }} {{ app_name }}.wsgi:application
