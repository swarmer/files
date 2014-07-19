#!/bin/sh
cd /home/{{ app_name }}/{{ app_name }}
. venv/bin/activate
exec gunicorn -b :{{ proxy_port }} {{ app_name }}.wsgi:application
