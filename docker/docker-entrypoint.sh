#!/bin/bash




#python3 manager.py runserver --host 0.0.0.0:8000
#uwsgi --ini start.ini
waitress-serve --port=8000  --call app:create_app