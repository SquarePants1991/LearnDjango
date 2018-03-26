#!/usr/bin/env sh
nginx -s stop
sudo pkill -f 'uwsgi'
sudo uwsgi --ini /usr/local/etc/uwsgi9090.ini
nginx