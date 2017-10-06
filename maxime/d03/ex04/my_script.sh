#!/bin/bash
# https://stackoverflow.com/questions/7369145/activating-a-virtualenv-using-a-shell-script-doesnt-seem-to-work
# https://stackoverflow.com/questions/43582257/shell-script-to-set-up-virtualenv-and-pip

python3 -m venv django_venv && . django_venv/bin/activate && django_venv/bin/pip install -r requirement.txt && /bin/sh
