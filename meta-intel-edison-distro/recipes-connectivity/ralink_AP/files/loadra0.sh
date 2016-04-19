#!/bin/sh
sleep 3
insmod /lib/modules/rtutil7601Uap.ko
insmod /lib/modules/mt7601Uap.ko
insmod /lib/modules/rtnet7601Uap.ko
sleep 8
ifconfig ra0 192.168.42.1 up