#!/bin/bash

echo "running nginx.sh file"
echo "User: $USER"
echo "Present Directory: $PWD"

if [ -e logs/nginx_access.log ] && [ -e logs/nginx_error.log ]
then
    echo "'nginx_access.log' & 'nginx_error.log' files exist!"
else
    touch logs/nginx_access.log logs/nginx_error.log
    sudo chmod u+x logs/nginx_access.log logs/nginx_error.log
    echo "Created the 'nginx_access.log' & 'nginx_error.log' file!"
fi

sudo systemctl start nginx
sudo systemctl enable nginx

echo "Nginx is started!"
sudo nginx -t
sudo systemctl status nginx

echo "Nginx setup finished!!"


