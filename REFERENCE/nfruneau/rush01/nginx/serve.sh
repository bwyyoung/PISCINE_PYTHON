#!/bin/bash


APP_CONF=./rush01_nginx.conf
NGINX_CONF=$HOME/.brew/etc/nginx/nginx.conf
CURRENT_DATE=`date +"%Y-%m-%d_%H-%M-%S"`

# lien symbolique de la conf dans nginx
#mv $NGINX_CONF $NGINX_CONF_$CURRENT_DATE
cp $APP_CONF $NGINX_CONF

# restart nginx
nginx -s stop
nginx
nginx -s reload

# uwsgi
#uwsgi --socket d08.sock --module d08.wsgi --chmod-socket=664 --ini uwsgi_d08.ini
#uwsgi --http :1337 --module d08.wsgi --chmod-socket=664 --ini uwsgi_d08.ini
#uwsgi --http :1337 --module d08.wsgi --ini uwsgi_d08.ini
#uwsgi --socket :1337 --module d08.wsgi --ini uwsgi_d08.ini
uwsgi --socket 127.0.0.1:1337 --ini uwsgi_d08.ini #--protocol=http
