#!/usr/bin/env bash
#sets up the web server for the deployment of web_static

apt update
apt install nginx -y

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "This shit is working" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

printf %s "server {
    listen 80;
    listen [::]:80;
    add_header X-Served-By $HOSTNAME;
    root /var/www/html;
    index index.html;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html;
    }
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

service nginx restart
