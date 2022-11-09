#!/bin/bash

echo "running uwsgi.sh file!"
echo "User: $USER"
echo "Present Dir: $PWD"

source env/bin/activate
pip3 install uwsgi

if [ -e /var/lib/jenkins/workspace/MainTF/logs/maintf_uwsgi.log ]
then
    echo "maintf_uwsgi.log file exists"
else
    echo "maintf_uwsgi.log file doesn't exists"
    touch logs/maintf_uwsgi.log
    echo "Created the maintf_uwsgi.log file into path: $PWD/logs/maintf_uwsgi.log"
fi

sudo systemctl daemon-reload
# sudo systemctl restart emperor.uwsgi.service
sudo systemctl status emperor.uwsgi.service
