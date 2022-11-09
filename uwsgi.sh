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

if [ -d /etc/uwsgi/vassals ]
then
    echo "vassals dir exists"
else
    echo "vassals dir doesn't exists"
    sudo mkdir /etc/uwsgi/vassals
    echo "Created '/etc/uwsgi/vassals' dir!"
fi
sudo chown -R jenkins /etc/uwsgi/vassals

if [ -e /etc/uwsgi/emperor.ini ]
then
    echo "emperor.ini file exists"
else
    echo "emperor.ini file doesn't exists"
    sudo cp -rf emperor.ini /etc/uwsgi/emperor.ini
    echo "Copied the emperor.ini file into path: /etc/uwsgi/emperor.ini"
fi
sudo chown -R jenkins /etc/uwsgi/emperor.ini

sudo systemctl daemon-reload
# sudo systemctl restart emperor.uwsgi.service
sudo systemctl status emperor.uwsgi.service
