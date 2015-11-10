#!/bin/sh

python /mostfun/cpanel/CPanel.py &

sh /mostfun/mjpg-streamer/start.sh &

rmmod g_multi
losetup -o 8192 /dev/loop0 /dev/disk/by-partlabel/update
mount /dev/loop0 /update

echo 19 > /sys/class/gpio/export                               
                                                               
echo mode0 > /sys/kernel/debug/gpio_debug/gpio19/current_pinmux

echo high > /sys/class/gpio/gpio19/direction
echo 0 > /sys/class/gpio/gpio19/value

systemctl start hostapd

exit