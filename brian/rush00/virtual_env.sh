#!/bin/bash
python3 -m venv django_venv;
. django_venv/bin/activate;
pip3 install -r requirements.txt;
exec /bin/zsh -i;
