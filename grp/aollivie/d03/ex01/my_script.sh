#!/bin/sh
pip -V;


pip3 install --upgrade --force-reinstall --target=local_lib git+https://github.com/jaraco/path.py.git --log install.log;

python3 my_program.py
