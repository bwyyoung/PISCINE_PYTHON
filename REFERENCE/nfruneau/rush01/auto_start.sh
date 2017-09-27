#!/bin/bash

# export PATH=/nfs/2013/c/cdivry/Library/Python/3.5/bin:$PATH
# brew install postgresql (pour psycopg2)
#python manage.py runserver localhost:8000

# var
ENV=env

# create virtualenv
echo -e "[\033[0;32m creation de l'environnement virtuel \033[0m]" && \
virtualenv $ENV && \

# activate virtualenv
echo -e "[\033[0;32m activation de l'environnement virtuel \033[0m]" && \
source $ENV/bin/activate && \

# install pip dependancies
echo -e "[\033[0;32m installation des dependances \033[0m]" && \
pip install -r requirement.txt && \

# apps deployment
echo -e "[\033[0;32m deploiement des applications \033[0m]" && \
( cd apps && ./deploy.sh && cd .. ) && \


echo -e "[\033[0;32m migration du projet \033[0m]" && \
python manage.py collectstatic && \


echo -e "[\033[0;32m migration du projet \033[0m]" && \
rm -fr db.sqlite3 && \
python manage.py makemigrations myauth forum userprofile && \
python manage.py migrate && \

# fin
echo -e "[\033[0;32m demarrage du serveur web via NGINX + WSGI \033[0m]" && \
echo -e "[\033[0;33m http://localhost:8000/ [NGINX] -> from :1337 [WSGI] \033[0m]" && \
echo -e "[\033[0;33m https://localhost:7777/ [HTTPS] \033[0m]" && \
( cd nginx && ./serve.sh && cd .. ) && \
bash
