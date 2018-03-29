#!/bin/bash
set -e

docker build -t gcr.io/emerald-rhythm-199000/library:latest .
gcloud docker -- push gcr.io/emerald-rhythm-199000/library:latest
gcloud compute instances reset library-app
until (curl -s https://library.nuys.xyz > /dev/null); do sleep 1m; done

