#!/bin/sh
echo 82 > /sys/class/gpio/export                                                                                      
echo mode0 > /sys/kernel/debug/gpio_debug/gpio82/current_pinmux
echo high > /sys/class/gpio/gpio82/direction
echo 1 > /sys/class/gpio/gpio82/value
echo 0 > /sys/class/gpio/gpio82/value

rmmod g_multi
losetup -o 8192 /dev/loop0 /dev/disk/by-partlabel/update
mount /dev/loop0 /update

python /mostfun/panel/CPanel.py &
/mostfun/mjpgstreamer/mjpg_streamer -i "/mostfun/mjpgstreamer/input_uvc.so" -o "/mostfun/mjpgstreamer/output_file.so" &
