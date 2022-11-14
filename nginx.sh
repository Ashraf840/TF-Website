#!/bin/bash

echo "running nginx.sh file"
echo "User: $USER"
echo "Present Directory: $PWD"

NGINX_CONF_FILE=MainTechforing.conf
NGINX_SITES_AVAILABLE_DIR=/etc/nginx/sites-available
NGINX_SITES_ENABLED_DIR=/etc/nginx/sites-enabled

if [ -e logs/nginx_access.log ] && [ -e logs/nginx_error.log ]
then
    echo "'nginx_access.log' & 'nginx_error.log' files exist!"
else
    touch logs/nginx_access.log logs/nginx_error.log
    sudo chmod u+x logs/nginx_access.log logs/nginx_error.log
    echo "Created the 'nginx_access.log' & 'nginx_error.log' file!"
fi

# shellcheck disable=SC2232
sudo cp -rf $NGINX_CONF_FILE $NGINX_SITES_AVAILABLE_DIR/MainTechforing.conf
sudo chown -R jenkins $NGINX_SITES_AVAILABLE_DIR/MainTechforing.conf
echo "Copied the '$NGINX_CONF_FILE' file in path: $NGINX_SITES_AVAILABLE_DIR"
chmod 710 /var/lib/jenkins/workspace/MainTF

sudo ln -s $NGINX_SITES_AVAILABLE_DIR/MainTechforing.conf $NGINX_SITES_ENABLED_DIR
sudo chown -R root:www-data $NGINX_SITES_ENABLED_DIR/MainTechforing.conf
echo "Created symlink of '$NGINX_SITES_AVAILABLE_DIR/MainTechforing.conf' inside the path: $NGINX_SITES_ENABLED_DIR"

sudo systemctl start nginx
sudo systemctl enable nginx

echo "Nginx is started!"
sudo nginx -t
sudo systemctl status nginx

echo "Nginx setup finished!!"


