#!/bin/sh
echo 82 > /sys/class/gpio/export                                                                                      
echo mode0 > /sys/kernel/debug/gpio_debug/gpio82/current_pinmux
echo high > /sys/class/gpio/gpio82/direction
echo 0 > /sys/class/gpio/gpio82/value

echo 14 > /sys/class/gpio/export
echo high > /sys/class/gpio/gpio14/direction

echo 183 > /sys/class/gpio/export
echo high > /sys/class/gpio/gpio183/direction
