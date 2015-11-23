#!/bin/sh
echo 19 > /sys/class/gpio/export                                                                                      
echo mode0 > /sys/kernel/debug/gpio_debug/gpio19/current_pinmux
echo high > /sys/class/gpio/gpio19/direction
echo 0 > /sys/class/gpio/gpio19/value

rmmod g_multi
losetup -o 8192 /dev/loop0 /dev/disk/by-partlabel/update
mount /dev/loop0 /update

sh /mostfun/mjpg-streamer/start.sh &
sh /mostfun/mjpg-streamer/
python /mostfun/panel/CPanel.py &

systemctl start hostapd

exit