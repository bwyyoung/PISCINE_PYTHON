#!/bin/bash

echo -e "[ \033[0;33mRUN THIS UNDER VIRTUALENV\033[0m ]"

# rm dists directories
rm -fr app_example/dist
rm -fr myauth/dist
rm -fr forum/dist

# rm generated packages folders
rm -fr app_example/app_example.egg-info
rm -fr myauth/myauth.egg-info
rm -fr forum/forum.egg-info

# generating packages
python3 app_example/setup.py sdist
python3 myauth/setup.py sdist
python3 forum/setup.py sdist

echo -e "[ \033[0;33m now installing deployment app via pip\033[0m ]"

# install generated package via 'pip'
pip install --upgrade app_example/dist/app_example-1337.tar.gz
pip install --upgrade myauth/dist/myauth-0.1.tar.gz
pip install --upgrade forum/dist/forum-0.1.tar.gz
