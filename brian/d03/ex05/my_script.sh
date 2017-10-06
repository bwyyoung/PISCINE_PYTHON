#!/bin/bash
python3 -m venv django_venv;
source django_venv/bin/activate;
pip3 install -r requirement.txt;
source django_venv/bin/activate;
##django-admin startproject Django;
cd Django;
##python3 manage.py startapp helloworld
python3 manage.py runserver 127.0.0.1:8000
