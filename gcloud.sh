#!/bin/bash
set -e
# gcloud compute firewall-rules create allow-http  --allow tcp:80  --target-tags web-server
# gcloud compute firewall-rules create allow-https --allow tcp:443 --target-tags web-server
gcloud beta compute instances create-with-container \
       library-app \
       --description "Symphony library app service" \
       --container-image gcr.io/emerald-rhythm-199000/library \
       --container-mount-host-path mount-path=/etc/letsencrypt,host-path=/mnt/stateful_partition/letsencrypt,mode=rw \
       --container-mount-host-path mount-path=/srv/db,host-path=/mnt/stateful_partition/db,mode=rw \
       --tags web-server \
       --public-dns \
       --machine-type f1-micro
