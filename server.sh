#!/bin/sh

letsencrypt () {
    if [ -n "$1" ]; then
        sleep "$1"
    fi
    certbot renew --deploy-hook "kill -HUP 1"
    if [ -n "$1" ]; then
        letsencrypt "$1"
    fi
}

letsencrypt
letsencrypt 1d &
./manage.py migrate --no-input
exec uwsgi --ini uwsgi.ini
