#!/bin/sh

pip3 --version
pip install git+https://github.com/jaraco/path.py.git -t './local_lib' --upgrade --no-deps --ignore-installed --log 'pip.log'
python3 my_program.py
