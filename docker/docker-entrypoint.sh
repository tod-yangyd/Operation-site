#!/bin/bash




#python3 manager.py runserver --host 0.0.0.0:8000
#uwsgi --ini start.ini
gunicorn --config=gunicorn_config.py start:app