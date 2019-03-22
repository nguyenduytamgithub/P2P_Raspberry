#!/bin/sh
hostname="$(cat /proc/sys/kernel/hostname)"  
rm -r /root/.node-red/flows_${hostname}.json
mv /root/.node-red/run/flows_raspberrypi2.json /root/.node-red/flows_${hostname}.json
exit 0
