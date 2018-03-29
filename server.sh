#!/bin/sh

letsencrypt () {
    if [ -n "$1" ]; then
        sleep "$1"
    fi
    certbot certonly --email info@northernutahyouthsymphony.org --agree-tos --no-eff-email --dns-google -d library.nuys.xyz -d www.nuys.xyz -d nuys.xyz
    if [ -n "$1" ]; then
        letsencrypt "$1"
    fi
}

letsencrypt
letsencrypt 30d &
./manage.py migrate --no-input
exec uwsgi --ini uwsgi.ini
