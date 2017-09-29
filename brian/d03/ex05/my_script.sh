#!/bin/bash
python3 $HOME/Library/Python/2.7/lib/python/site-packages/virtualenv.py -p /usr/local/bin/python3 django_venv;
. django_venv/bin/activate;
pip3 install -r requirement.txt;
. django_venv/bin/activate; exec /bin/zsh -i;
