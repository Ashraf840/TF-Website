#!/bin/bash

echo "running uwsgi.sh file!"
echo "User: $USER"
echo "Present Dir: $PWD"

source env/bin/activate
pip3 install uwsgi

sudo systemctl daemon-reload
# sudo systemctl restart emperor.uwsgi.service
sudo systemctl status emperor.uwsgi.service
