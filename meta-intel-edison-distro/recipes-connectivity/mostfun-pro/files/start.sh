#!/bin/sh

nohup python /mostfun/cpanel/CPanel.py &

nohup sh /mostfun/mjpg-streamer/start.sh &

rmmod g_multi
losetup -o 8192 /dev/loop0 /dev/disk/by-partlabel/update
mount /dev/loop0 /update

exit