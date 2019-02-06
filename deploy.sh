#!/bin/bash
set -e

docker build -t gcr.io/emerald-rhythm-199000/library:latest .
docker push gcr.io/emerald-rhythm-199000/library:latest
gcloud compute instances reset library-app
until (curl -s https://library.nuys.xyz > /dev/null); do
    printf '.'
    sleep 1m;
done
printf 'Done.\n'
