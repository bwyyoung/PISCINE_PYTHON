#!/bin/bash
python3 -m venv django_venv;
. django_venv/bin/activate;
pip3 install -r requirement.txt;
. django_venv/bin/activate; exec /bin/zsh -i;
