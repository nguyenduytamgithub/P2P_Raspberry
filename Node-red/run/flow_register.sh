#!/bin/sh
hostname="$(cat /proc/sys/kernel/hostname)" 
mv /root/.node-red/flows_${hostname}.json /root/.node-red/config.json
mv /root/.node-red/run/main_flow.json /root/.node-red/flow_${hostname}.json
exit 0

