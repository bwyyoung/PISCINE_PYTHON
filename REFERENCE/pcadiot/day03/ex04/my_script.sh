#!/bin/zsh

python3 -m venv "/Users/pcadiot/Piscine-Python/day03/ex04/django_venv"


pip3 install -r django_venv/requirement.txt


cd django_venv

python3 manage.py runserver 127.0.0.1:8000


##source bin/activate


