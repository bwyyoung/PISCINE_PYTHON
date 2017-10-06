#!/bin/bash
python3 -m venv django_venv && source django_venv/bin/activate && pip3 install -r requirement.txt -t './django_venv' && /bin/sh && cd Django && python3 manage.py runserver 127.0.0.1:8000
