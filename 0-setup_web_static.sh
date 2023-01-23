#!/usr/bin/env bash
# a script that sets up your web servers for the deployment of web_static

mkdir -fp /data/web_static/releases/test/
mkdir -fp /data/web_static/shared/
echo "It is working" > /data/web_static/releases/test/index.html
ln -fs /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /redirect_me {
        return 301 http://example.com/;
    }

    location /hbnb_static {
       	alias /data/web_static/current/
	index index.html
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

service nginx restart
