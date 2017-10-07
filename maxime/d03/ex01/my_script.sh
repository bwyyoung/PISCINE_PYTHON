#!/bin/sh

pip3 --version
pip3 install git+https://github.com/jaraco/path.py.git -t './local_lib' --upgrade --log 'pip.log' && python3 my_program.py
