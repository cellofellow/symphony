#!/bin/sh
set -e
for app in contenttypes auth admin sessions library; do
    ./manage.py migrate --noinput --fake $app 0001
done
./manage.py migrate --noinput
